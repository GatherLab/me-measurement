from PySide2 import QtCore

import time
import datetime as dt
import numpy as np
import pandas as pd
import math

import core_functions as cf
import physics_functions as pf


class FrequencyScan(QtCore.QThread):
    """
    Class thread that handles the spectrum measurement
    """

    # Define costum signals
    # https://stackoverflow.com/questions/36434706/pyqt-proper-use-of-emit-and-pyqtsignal
    # With pyside2 https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    update_spectrum_signal = QtCore.Signal(list, list, list, list)
    update_progress_bar = QtCore.Signal(str, float)

    def __init__(
        self,
        arduino,
        source,
        oscilloscope,
        measurement_parameters,
        setup_parameters,
        parent=None,
    ):
        super(FrequencyScan, self).__init__()
        # Variable to kill thread

        # Assign hardware and reset
        self.arduino = arduino
        self.arduino.init_serial_connection()
        self.source = source
        self.oscilloscope = oscilloscope
        self.parent = parent

        self.measurement_parameters = measurement_parameters
        self.setup_parameters = setup_parameters

        self.global_parameters = cf.read_global_settings()

        # Connect signal to the updater from the parent class
        self.update_spectrum_signal.connect(parent.update_spectrum)
        self.update_progress_bar.connect(parent.progressBar.setProperty)

        # Define dataframe to store data in
        self.df_data = pd.DataFrame(
            columns=["frequency", "voltage", "current", "magnetic_field", "vmax"]
        )

        self.is_killed = False

    def run(self):
        """
        Class that does a frequency sweep
        """
        # self.parent.setup_thread.pause = True
        # self.parent.oscilloscope_thread.pause = True

        # First define the frequencies the program shall sweep over
        # self.df_data["frequency"] = np.arange(
        # self.measurement_parameters["minimum_frequency"],
        # self.measurement_parameters["maximum_frequency"],
        # self.measurement_parameters["frequency_step"],
        # )
        import pydevd

        pydevd.settrace(suspend=False)

        self.parent.oscilloscope_thread.pause = True

        # Set voltage and current (they shall remain constant over the entire sweep)
        self.source.set_voltage(self.measurement_parameters["voltage"])
        self.source.set_current(self.measurement_parameters["current_compliance"])
        self.source.output(True)

        # Define arrays in which the data shall be stored in
        i = 0

        # Sweep over all frequencies
        frequencies = np.arange(
            self.measurement_parameters["minimum_frequency"],
            self.measurement_parameters["maximum_frequency"],
            self.measurement_parameters["frequency_step"],
        )
        for frequency in frequencies:
            # for frequency in self.df_data["frequency"]:
            cf.log_message("Frequency set to " + str(frequency) + " kHz")

            # Set frequency
            self.arduino.set_frequency(
                frequency, self.measurement_parameters["autoset_capacitance"]
            )

            # Wait a bit (wait longer for the first frequency, so that the PID
            # of the source can adjust to ensure the set current output)
            if math.isclose(frequency, frequencies[0]):
                time.sleep(4)
            else:
                time.sleep(self.measurement_parameters["frequency_settling_time"])

            # Measure the voltage and current (and posssibly paramters on the osci)
            voltage, current, mode = self.source.read_values()

            # Now measure Vpp from channel one on the oscilloscope (and save in mT)
            magnetic_field = (
                pf.calculate_magnetic_field_from_Vind(
                    4,
                    20e-3,
                    float(self.oscilloscope.measure_vmax("CHAN1")),
                    frequency * 1e3,
                )
                * 1e3
            )
            vmax = float(self.oscilloscope.measure_vmax("CHAN2"))

            # Set the variables in the dataframe
            self.df_data.loc[i, "voltage"] = voltage
            self.df_data.loc[i, "current"] = current
            self.df_data.loc[i, "frequency"] = frequency
            self.df_data.loc[i, "magnetic_field"] = magnetic_field
            self.df_data.loc[i, "vmax"] = vmax

            # Update progress bar
            self.update_progress_bar.emit(
                "value", int((i + 1) / len(frequencies) * 100)
            )

            self.update_spectrum_signal.emit(
                self.df_data["frequency"],
                self.df_data["current"],
                self.df_data["magnetic_field"],
                self.df_data["vmax"],
            )

            # Now compute the slope to adjust the step hight on the fly
            if i > 0:
                slope = abs(
                    (
                        self.df_data.loc[i, "current"]
                        - self.df_data.loc[i - 1, "current"]
                    )
                    / (
                        self.df_data.loc[i, "frequency"]
                        - self.df_data.loc[i - 1, "frequency"]
                    )
                )

                # The higher the slope, the smaller the step
                # if slope > 0:
                #     frequency = frequency + max(
                #         [
                #             self.measurement_parameters["frequency_step"]
                #             / (slope * 100 * 2),
                #             0.2,
                #         ]
                #     )
                # else:
                #     frequency = (
                #         frequency + self.measurement_parameters["frequency_step"]
                #     )

            frequency = frequency + self.measurement_parameters["frequency_step"]

            i += 1

            if self.is_killed:
                # Close the connection to the spectrometer
                self.source.output(False)
                self.source.set_voltage(5)
                self.parent.oscilloscope_thread.pause = False
                self.quit()
                return

        self.source.output(False)
        self.save_data()
        self.parent.specw_start_measurement_pushButton.setChecked(False)

        self.parent.oscilloscope_thread.pause = False
        # self.parent.setup_thread.pause = False
        # self.parent.oscilloscope_thread.pause = False

    def kill(self):
        """
        Kill thread while running
        """
        self.is_killed = True

    def save_data(self):
        """
        Function to save the measured data to file. This should probably be
        integrated into the AutotubeMeasurement class
        """

        # Define Header
        line02 = (
            "Base Capacitance:"
            + str(self.global_parameters["base_capacitance"])
            + " pF\t Coil Inductance:"
            + str(self.global_parameters["coil_inductance"])
            + " mH"
        )
        line03 = (
            "Voltage:   "
            + str(self.measurement_parameters["voltage"])
            + " V   "
            + "Current:   "
            + str(self.measurement_parameters["current_compliance"])
        )
        line04 = (
            "Min. Frequency:   "
            + str(self.measurement_parameters["minimum_frequency"])
            + " kHz \t"
            + "Max. Frequency:   "
            + str(self.measurement_parameters["maximum_frequency"])
            + " kHz \t"
            + "Frequency Step:   "
            + str(self.measurement_parameters["frequency_step"])
            + " kHz \t"
        )
        line05 = "### Measurement data ###"
        line06 = "Frequency\t Voltage\t Current\t Magnetic Field\t Vmax_ind"
        line07 = "Hz\t V\t A\t mT\t V\n"

        header_lines = [
            line02,
            line03,
            line04,
            line05,
            line06,
            line07,
        ]

        # Write header lines to file
        file_path = (
            self.setup_parameters["folder_path"]
            + dt.date.today().strftime("%Y-%m-%d_")
            + self.setup_parameters["batch_name"]
            + "_d"
            + str(self.setup_parameters["device_number"])
            + ".csv"
        )
        cf.save_file(self.df_data, file_path, header_lines)

        # with open(file_path, "a") as the_file:
        #     the_file.write("\n".join(header_lines))

        # # Now write pandas dataframe to file
        # self.df_data.to_csv(file_path, index=False, mode="a", header=False, sep="\t")
