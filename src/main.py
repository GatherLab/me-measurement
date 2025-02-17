from UI_main_window import Ui_MainWindow
from settings import Settings
from loading_window import LoadingWindow

from frequency_measurement import FrequencyScan
from bias_field_measurement import BiasScan

from hf_field_measurement import HFScan

# from osci_frequency_scan import HFScan
from capacitance_measurement import CapacitanceScan
from setup import SetupThread
from oscilloscope_measurement import OscilloscopeThread
from lifetime_measurement import LTScan
from pid_tuning import PIDScan
from pulsing_sweep import PulsingSweep

from hardware import (
    KoradKD3305PSource,
    RigolOscilloscope,
    Arduino,
)

import core_functions as cf
import physics_functions as pf

from PySide6 import QtCore, QtGui, QtWidgets

import time
import os
import sys
import datetime as dt
import logging
from logging.handlers import RotatingFileHandler

import numpy as np
import pandas as pd
import math

import webbrowser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    This class contains the logic of the program and is explicitly seperated
    from the UI classes. However, it is a child class of Ui_MainWindow.
    """

    def __init__(self):
        """
        Initialise instance
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # -------------------------------------------------------------------- #
        # -------------------------- Hardware Setup -------------------------- #
        # -------------------------------------------------------------------- #
        self.t = 0

        # Execute initialisation thread
        oscilloscope_address = "USB0::0x1AB1::0x0517::DS1ZE223304729::INSTR"
        # source_address = "ASRL4::INSTR"
        # arduino_address = "ASRL6::INSTR"
        loading_window = LoadingWindow(self)

        # Execute loading dialog
        loading_window.exec()

        # -------------------------------------------------------------------- #
        # ------------------------------ General ----------------------------- #
        # -------------------------------------------------------------------- #

        # Update statusbar
        cf.log_message("Initialising Program")
        self.tabWidget.currentChanged.connect(self.changed_tab_widget)

        # Hide by default and only show if a process is running
        self.progressBar.hide()

        # -------------------------------------------------------------------- #
        # --------------------------- Menubar -------------------------------- #
        # -------------------------------------------------------------------- #
        self.actionOptions.triggered.connect(self.show_settings)

        # Open the documentation in the browser (maybe in the future directly
        # open the readme file in the folder but currently this is so much
        # easier and prettier)
        self.actionDocumentation.triggered.connect(
            lambda: webbrowser.open(
                "https://github.com/GatherLab/me-measurement/blob/main/README.md"
            )
        )

        self.actionOpen_Log.triggered.connect(lambda: self.open_file("./usr/log.out"))

        # -------------------------------------------------------------------- #
        # --------------------------- Setup Widget --------------------------- #
        # -------------------------------------------------------------------- #
        # This two variables are needed to update the HF field strength
        self.initial_global_parameters = cf.read_global_settings()
        self.previous_current = 0

        self.sw_browse_pushButton.clicked.connect(self.browse_folder)

        # Setup and start setup thread that continuously reads out the voltage
        # and current of the hf_source as well as the frequency of the Arduino
        self.setup_thread = SetupThread(self.source, self.arduino, self)
        self.setup_thread.start()

        self.sw_voltage_spinBox.valueChanged.connect(self.voltage_changed)
        self.sw_current_spinBox.valueChanged.connect(self.current_changed)
        self.sw_frequency_spinBox.valueChanged.connect(self.frequency_changed)
        self.sw_capacitance_spinBox.valueChanged.connect(self.capacitance_changed)
        self.sw_dc_current_spinBox.valueChanged.connect(self.dc_current_changed)
        # self.sw_resistance_spinBox.valueChanged.connect(self.resistance_changed)

        self.sw_source_output_pushButton.clicked.connect(self.toggle_source_output)
        self.sw_source_output_pushButton.setCheckable(True)

        # -------------------------------------------------------------------- #
        # ------------------------ Pulsing Widget ---------------------------- #
        # -------------------------------------------------------------------- #
        self.pulsew_browse_pushButton.clicked.connect(self.pulsing_browse_folder)
        self.pulsew_start_measurement_pushButton.setCheckable(True)

        self.pulsew_start_measurement_pushButton.clicked.connect(
            self.start_pulsing_sweep
        )

        self.pulsew_constant_parameter_mode_toggleSwitch.clicked.connect(
            self.toggle_pulsing_constant_parameter_mode
        )

        self.pulsew_constant_parameter_mode_toggleSwitch.setChecked(False)

        # -------------------------------------------------------------------- #
        # -------------------- Frequency Sweep Widget ------------------------ #
        # -------------------------------------------------------------------- #
        self.specw_start_measurement_pushButton.clicked.connect(
            self.start_frequency_sweep
        )
        self.specw_start_measurement_pushButton.setCheckable(True)
        self.specw_constant_magnetic_field_mode_toggleSwitch.clicked.connect(
            self.change_current_to_magnetic_field
        )

        # -------------------------------------------------------------------- #
        # -------------------- Bias Field Sweep Widget ----------------------- #
        # -------------------------------------------------------------------- #
        self.bw_start_measurement_pushButton.clicked.connect(self.start_dc_field_sweep)
        self.bw_start_measurement_pushButton.setCheckable(True)
        self.bw_constant_magnetic_field_mode_toggleSwitch.clicked.connect(
            self.change_current_to_magnetic_field
        )

        # -------------------------------------------------------------------- #
        # --------------------- HF Field Sweep Widget ------------------------ #
        # -------------------------------------------------------------------- #
        self.hfw_start_measurement_pushButton.clicked.connect(self.start_hf_field_sweep)
        self.hfw_start_measurement_pushButton.setCheckable(True)
        # self.hfw_constant_magnetic_field_mode_toggleSwitch.clicked.connect(
        # self.change_current_to_magnetic_field
        # )

        # -------------------------------------------------------------------- #
        # ------------------------- Lifetime Widget -------------------------- #
        # -------------------------------------------------------------------- #
        self.ltw_start_measurement_pushButton.clicked.connect(self.start_lt_sweep)
        self.ltw_start_measurement_pushButton.setCheckable(True)
        # self.hfw_constant_magnetic_field_mode_toggleSwitch.clicked.connect(
        # self.change_current_to_magnetic_field
        # )

        # -------------------------------------------------------------------- #
        # ------------------ Capacitance Sweep Widget ------------------------ #
        # -------------------------------------------------------------------- #
        self.capw_start_measurement_pushButton.clicked.connect(
            self.start_capacitance_sweep
        )
        self.capw_start_measurement_pushButton.setCheckable(True)

        # -------------------------------------------------------------------- #
        # ----------------------- Osciloscope Widget ------------------------- #
        # -------------------------------------------------------------------- #
        self.oscilloscope_thread = OscilloscopeThread(self.oscilloscope, parent=self)
        self.oscilloscope_thread.start()

        self.ow_stop_pushButton.clicked.connect(self.stop_osci)
        self.ow_auto_scale_pushButton.clicked.connect(self.auto_scale_osci)
        self.ow_start_measurement_pushButton.clicked.connect(self.save_osci)

        # -------------------------------------------------------------------- #
        # -------------------- Frequency Sweep Widget ------------------------ #
        # -------------------------------------------------------------------- #
        self.pidw_start_measurement_pushButton.clicked.connect(
            self.start_pid_measurement
        )
        self.pidw_start_measurement_pushButton.setCheckable(True)

        # -------------------------------------------------------------------- #
        # --------------------- Set Standard Parameters ---------------------- #
        # -------------------------------------------------------------------- #

        # Set standard parameters for setup
        self.sw_frequency_spinBox.setMinimum(2)
        self.sw_frequency_spinBox.setMaximum(150000)
        self.sw_frequency_spinBox.setKeyboardTracking(False)
        self.sw_frequency_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sw_frequency_spinBox.setValue(1000)

        self.sw_capacitance_spinBox.setMinimum(0)
        self.sw_capacitance_spinBox.setMaximum(500000)
        self.sw_capacitance_spinBox.setKeyboardTracking(False)
        self.sw_capacitance_spinBox.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons
        )
        self.sw_capacitance_spinBox.setValue(0)

        self.sw_voltage_spinBox.setMinimum(0)
        self.sw_voltage_spinBox.setMaximum(30)
        self.sw_voltage_spinBox.setDecimals(1)
        self.sw_voltage_spinBox.setSingleStep(0.1)
        self.sw_voltage_spinBox.setKeyboardTracking(False)
        self.sw_voltage_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sw_voltage_spinBox.setValue(5)

        self.sw_current_spinBox.setMinimum(0)
        self.sw_current_spinBox.setMaximum(5)
        self.sw_current_spinBox.setDecimals(1)
        self.sw_current_spinBox.setSingleStep(0.1)
        self.sw_current_spinBox.setKeyboardTracking(False)
        self.sw_current_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sw_current_spinBox.setValue(0.1)

        self.sw_dc_current_spinBox.setMinimum(0)
        self.sw_dc_current_spinBox.setMaximum(5)
        self.sw_dc_current_spinBox.setDecimals(3)
        self.sw_dc_current_spinBox.setSingleStep(0.1)
        self.sw_dc_current_spinBox.setKeyboardTracking(False)
        self.sw_dc_current_spinBox.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons
        )
        self.sw_dc_current_spinBox.setValue(0)

        # self.sw_resistance_spinBox.setMinimum(70)
        # self.sw_resistance_spinBox.setMaximum(2600)
        # self.sw_resistance_spinBox.setKeyboardTracking(False)
        # self.sw_resistance_spinBox.setButtonSymbols(
        # QtWidgets.QAbstractSpinBox.NoButtons
        # )
        # self.sw_resistance_spinBox.setValue(500)
        # self.sw_resistance_spinBox.setSingleStep(10)

        self.sw_autoset_capacitance_toggleSwitch.setChecked(True)

        # Set standard parameters for spectral measurement
        self.specw_voltage_spinBox.setMinimum(0)
        self.specw_voltage_spinBox.setMaximum(33)
        self.specw_voltage_spinBox.setValue(5)

        self.specw_current_spinBox.setMinimum(0)
        self.specw_current_spinBox.setMaximum(12)
        self.specw_current_spinBox.setValue(0.5)

        self.specw_minimum_frequency_spinBox.setMinimum(2)
        self.specw_minimum_frequency_spinBox.setMaximum(150000)
        self.specw_minimum_frequency_spinBox.setValue(135)

        self.specw_maximum_frequency_spinBox.setMinimum(2)
        self.specw_maximum_frequency_spinBox.setMaximum(150000)
        self.specw_maximum_frequency_spinBox.setValue(310)

        self.specw_frequency_step_spinBox.setMinimum(0.05)
        self.specw_frequency_step_spinBox.setMaximum(180)
        self.specw_frequency_step_spinBox.setValue(1)

        self.specw_frequency_settling_time_spinBox.setMinimum(0.01)
        self.specw_frequency_settling_time_spinBox.setMaximum(10)
        self.specw_frequency_settling_time_spinBox.setValue(1)

        self.specw_dc_magnetic_field_spinBox.setMinimum(0)
        self.specw_dc_magnetic_field_spinBox.setValue(10)
        self.specw_dc_magnetic_field_spinBox.setValue(1.5)

        self.specw_constant_magnetic_field_mode_toggleSwitch.setChecked(True)
        self.specw_autoset_capacitance_toggleSwitch.setChecked(True)
        self.specw_autoset_frequency_step_toggleSwitch.setChecked(False)

        # Set standard parameters for bias field measurement
        self.bw_voltage_spinBox.setMinimum(0)
        self.bw_voltage_spinBox.setMaximum(33)
        self.bw_voltage_spinBox.setValue(5)

        self.bw_current_spinBox.setMinimum(0)
        self.bw_current_spinBox.setMaximum(12)
        self.bw_current_spinBox.setValue(0.5)

        self.bw_frequency_spinBox.setMinimum(2)
        self.bw_frequency_spinBox.setMaximum(150000)
        self.bw_frequency_spinBox.setValue(145)

        self.bw_minimum_dc_magnetic_field_spinBox.setMinimum(0)
        self.bw_minimum_dc_magnetic_field_spinBox.setMaximum(10)
        self.bw_minimum_dc_magnetic_field_spinBox.setValue(0)

        self.bw_maximum_dc_magnetic_field_spinBox.setMinimum(0)
        self.bw_maximum_dc_magnetic_field_spinBox.setMaximum(10)
        self.bw_maximum_dc_magnetic_field_spinBox.setValue(8)

        self.bw_dc_magnetic_field_step_spinBox.setMinimum(0.1)
        self.bw_dc_magnetic_field_step_spinBox.setMaximum(10)
        self.bw_dc_magnetic_field_step_spinBox.setSingleStep(0.1)
        self.bw_dc_magnetic_field_step_spinBox.setValue(0.1)

        self.bw_dc_magnetic_field_settling_time_spinBox.setMinimum(0.01)
        self.bw_dc_magnetic_field_settling_time_spinBox.setMaximum(10)
        self.bw_dc_magnetic_field_settling_time_spinBox.setValue(0.5)

        self.bw_constant_magnetic_field_mode_toggleSwitch.setChecked(True)
        self.bw_autoset_capacitance_toggleSwitch.setChecked(True)
        self.bw_reverse_sweep_toggleSwitch.setChecked(True)

        # Set standard parameters for hf field measurement
        self.hfw_voltage_compliance_spinBox.setMinimum(0)
        self.hfw_voltage_compliance_spinBox.setMaximum(33)
        self.hfw_voltage_compliance_spinBox.setValue(5)

        self.hfw_dc_magnetic_field_spinBox.setMinimum(0)
        self.hfw_dc_magnetic_field_spinBox.setMaximum(10)
        self.hfw_dc_magnetic_field_spinBox.setValue(1.5)

        self.hfw_frequency_spinBox.setMinimum(1)
        self.hfw_frequency_spinBox.setMaximum(150000)
        self.hfw_frequency_spinBox.setValue(145)

        self.hfw_minimum_voltage_spinBox.setMinimum(0)
        self.hfw_minimum_voltage_spinBox.setMaximum(1000)
        self.hfw_minimum_voltage_spinBox.setValue(2)

        self.hfw_maximum_voltage_spinBox.setMinimum(0)
        self.hfw_maximum_voltage_spinBox.setMaximum(1000)
        self.hfw_maximum_voltage_spinBox.setValue(10)

        self.hfw_voltage_step_spinBox.setMinimum(0)
        self.hfw_voltage_step_spinBox.setMaximum(1000)
        self.hfw_voltage_step_spinBox.setValue(0.5)

        self.hfw_voltage_settling_time_spinBox.setMinimum(0)
        self.hfw_voltage_settling_time_spinBox.setMaximum(1000)
        self.hfw_voltage_settling_time_spinBox.setValue(1)

        # Set standard parameters for hf field measurement
        self.ltw_voltage_compliance_spinBox.setMinimum(0)
        self.ltw_voltage_compliance_spinBox.setMaximum(33)
        self.ltw_voltage_compliance_spinBox.setValue(12)

        self.ltw_dc_magnetic_field_spinBox.setMinimum(0)
        self.ltw_dc_magnetic_field_spinBox.setMaximum(10)
        self.ltw_dc_magnetic_field_spinBox.setValue(1.5)

        self.ltw_frequency_spinBox.setMinimum(2)
        self.ltw_frequency_spinBox.setMaximum(150000)
        self.ltw_frequency_spinBox.setValue(150)

        self.ltw_total_time_spinBox.setMinimum(0)
        self.ltw_total_time_spinBox.setMaximum(100000)
        self.ltw_total_time_spinBox.setValue(120)

        self.ltw_time_step_spinBox.setMinimum(0)
        self.ltw_time_step_spinBox.setMaximum(100000)
        self.ltw_time_step_spinBox.setValue(60)

        self.ltw_hf_magnetic_field_spinBox.setMinimum(0)
        self.ltw_hf_magnetic_field_spinBox.setMaximum(20)
        self.ltw_hf_magnetic_field_spinBox.setValue(10)

        # Set standard parameters for capacitance measurement
        self.capw_voltage_spinBox.setMinimum(0)
        self.capw_voltage_spinBox.setMaximum(33)
        self.capw_voltage_spinBox.setValue(2)

        self.capw_current_spinBox.setMinimum(0)
        self.capw_current_spinBox.setMaximum(12)
        self.capw_current_spinBox.setValue(1)

        self.capw_minimum_frequency_spinBox.setMinimum(2)
        self.capw_minimum_frequency_spinBox.setMaximum(150000)
        self.capw_minimum_frequency_spinBox.setValue(62)

        self.capw_maximum_frequency_spinBox.setMinimum(2)
        self.capw_maximum_frequency_spinBox.setMaximum(150000)
        self.capw_maximum_frequency_spinBox.setValue(350)

        self.capw_frequency_step_spinBox.setMinimum(0.05)
        self.capw_frequency_step_spinBox.setMaximum(1000)
        self.capw_frequency_step_spinBox.setValue(1)

        self.capw_resonance_frequency_step_spinBox.setMinimum(0)
        self.capw_resonance_frequency_step_spinBox.setMaximum(100)
        self.capw_resonance_frequency_step_spinBox.setValue(1)

        self.capw_frequency_margin_spinBox.setMinimum(0)
        self.capw_frequency_margin_spinBox.setMaximum(1000)
        self.capw_frequency_margin_spinBox.setValue(15)

        self.capw_frequency_settling_time_spinBox.setMinimum(0.01)
        self.capw_frequency_settling_time_spinBox.setMaximum(10)
        self.capw_frequency_settling_time_spinBox.setValue(0.5)

        # Set standard parameters for pid adjustment
        self.pidw_voltage_spinBox.setMinimum(0)
        self.pidw_voltage_spinBox.setMaximum(33)
        self.pidw_voltage_spinBox.setValue(5)

        self.pidw_current_spinBox.setMinimum(0)
        self.pidw_current_spinBox.setMaximum(12)
        self.pidw_current_spinBox.setValue(0.5)

        self.pidw_frequency_spinBox.setMinimum(2)
        self.pidw_frequency_spinBox.setMaximum(150000)
        self.pidw_frequency_spinBox.setValue(105)

        self.pidw_autoset_capacitance_toggleSwitch.setChecked(True)

    # -------------------------------------------------------------------- #
    # ------------------------- Global Functions ------------------------- #
    # -------------------------------------------------------------------- #
    def make_format(self, current, other):
        """
        function to allow display of both coordinates for figures with two axis
        """

        # current and other are axes
        def format_coord(x, y):
            # x, y are data coordinates
            # convert to display coords
            display_coord = current.transData.transform((x, y))
            inv = other.transData.inverted()
            # convert back to data coords with respect to ax
            ax_coord = inv.transform(display_coord)
            coords = [ax_coord, (x, y)]
            return "Left: {:<40}    Right: {:<}".format(
                *["({:.3f}, {:.3f})".format(x, y) for x, y in coords]
            )

        return format_coord

    def browse_folder(self):
        """
        Open file dialog to browse through directories
        """
        global_variables = cf.read_global_settings()

        self.global_path = QtWidgets.QFileDialog.getExistingDirectory(
            QtWidgets.QFileDialog(),
            "Select a Folder",
            global_variables["default_saving_path"],
            QtWidgets.QFileDialog.ShowDirsOnly,
        )
        # print(self.global_path)
        # file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)

        # if file_dialog1.exec():
        #     # Set global path to selected path
        #     self.global_path = file_dialog1.selectedFiles()

        #     # Set the according line edit
        self.sw_folder_path_lineEdit.setText(self.global_path + "/")

    def show_settings(self):
        """
        Shows the settings
        """
        self.settings_window = Settings(self)
        # ui = Ui_Settings()
        # ui.setupUi(self.settings_window, parent=self)

        p = (
            self.frameGeometry().center()
            - QtCore.QRect(QtCore.QPoint(), self.settings_window.sizeHint()).center()
        )

        self.settings_window.move(p)

        # self.settings_window.show()

        result = self.settings_window.exec()

    @QtCore.Slot(RigolOscilloscope)
    def init_oscilloscope(self, oscilloscope_object):
        """
        Inits oscilloscope
        """
        self.oscilloscope = oscilloscope_object

    @QtCore.Slot(KoradKD3305PSource)
    def init_source(self, source_object):
        """
        Receives a hf_source object from the init thread
        """
        self.source = source_object

    @QtCore.Slot(Arduino)
    def init_arduino(self, arduino_object):
        """
        Receives an arduino object from the init thread
        """
        self.arduino = arduino_object

    def open_file(self, path):
        """
        Opens a file on the machine with the standard program
        https://stackoverflow.com/questions/6045679/open-file-with-pyqt
        """
        if sys.platform.startswith("linux"):
            subprocess.call(["xdg-open", path])
        else:
            os.startfile(path)

    def closeEvent(self, event):
        """
        Function that shall allow for save closing of the program
        """

        cf.log_message("Program closed")

        # Kill threads here
        self.setup_thread.kill()
        self.oscilloscope_thread.kill()

        # Kill Osci
        try:
            self.oscilloscope.close()
        except Exception as e:
            cf.log_message("Oscilloscope thread could not be killed")
            cf.log_message(e)

        # Kill arduino connection
        try:
            self.arduino.close()
        except Exception as e:
            cf.log_message("Arduino connection could not be savely killed")
            cf.log_message(e)

        # if can_exit:
        event.accept()  # let the window close
        # else:
        #     event.ignore()

    def changed_tab_widget(self):
        """
        Function that shall manage the threads that are running when we are
        on a certain tab. For instance the spectrum thread really only must
        run when the user is on the spectrum tab. Otherwise it can be paused.
        This might become important in the future. The best idea is probably
        to just kill all unused threads when we change the tab.
        """
        if self.tabWidget.currentIndex() == 0:
            self.setup_thread.pause = False
            self.oscilloscope_thread.pause = True
        if self.tabWidget.currentIndex() == 1:
            self.setup_thread.pause = True
            self.oscilloscope_thread.pause = False
        if self.tabWidget.currentIndex() >= 2:
            self.setup_thread.pause = True
            self.oscilloscope_thread.pause = True

        cf.log_message(
            "Switched to tab widget no. " + str(self.tabWidget.currentIndex())
        )

        return

    # -------------------------------------------------------------------- #
    # --------------------------- Setup Thread --------------------------- #
    # -------------------------------------------------------------------- #
    @QtCore.Slot(float, float)
    def update_display(self, voltage, current, dc_current, dc_field):
        """
        Function to update the readings of the LCD panels that serve as an
        overview to yield the current value of voltage, current and frequency
        """
        # self.sw_frequency_lcdNumber.display(frequency)
        self.sw_voltage_lcdNumber.display(voltage)
        self.sw_current_lcdNumber.display(current)

        # Update dc source parameters
        self.sw_dc_current_lcdNumber.display(dc_current)
        self.sw_dc_field_lcdNumber.display(dc_field)

        # Only calculate the magnetic field if the current changed (otherwise it
        # is too time consuming to measure vmax from the osci)
        if not math.isclose(current, self.previous_current, abs_tol=0.001):
            magnetic_field = round(
                (
                    pf.calculate_magnetic_field_from_Vind(
                        self.initial_global_parameters["pickup_coil_windings"],
                        self.initial_global_parameters["pickup_coil_radius"] * 1e-3,
                        float(self.oscilloscope.measure_vmax(1)),
                        self.arduino.frequency * 1e3,
                    )
                    * 1e3
                ),
                2,
            )
            # print(magnetic_field)
            self.sw_hf_field_lcdNumber.display(magnetic_field)

        self.previous_current = current

    def voltage_changed(self):
        """
        Function that changes voltage on hf_source when it is changed on spinbox
        """
        if self.t < 2:
            self.t += 1
            return
        else:
            voltage = self.sw_voltage_spinBox.value()
            self.source.set_voltage(voltage, channel=2)
            # self.hf_source.output(True)
            # cf.log_message("Source voltage set to " + str(voltage) + " V")

    def current_changed(self):
        """
        Function that changes current on hf_source when it is changed on spinbox
        """
        if self.t < 2:
            self.t += 1
            return
        else:
            current = self.sw_current_spinBox.value()
            self.source.set_current(current, channel=2)
            cf.log_message("Source current set to " + str(current) + " A")

    def frequency_changed(self):
        """
        Function that changes frequency on arduino when it is changed on spinbox
        """
        frequency = self.sw_frequency_spinBox.value()
        self.arduino.trigger_frequency_generation(False)

        self.arduino.set_frequency(
            frequency,
            set_capacitance=self.sw_autoset_capacitance_toggleSwitch.isChecked(),
        )

        self.sw_frequency_lcdNumber.display(frequency)

        self.arduino.trigger_frequency_generation(True)

        if self.sw_autoset_capacitance_toggleSwitch.isChecked():
            self.sw_capacitance_lcdNumber.display(self.arduino.real_capacitance)

        cf.log_message("Arduino frequency set to " + str(frequency) + " kHz")

    def capacitance_changed(self):
        """
        Function that changes capacitance on arduino when it is changed on spinbox
        """
        capacitance = self.sw_capacitance_spinBox.value()
        self.arduino.set_capacitance(capacitance)

        self.sw_capacitance_lcdNumber.display(self.arduino.real_capacitance)

        # cf.log_message("Capacitance set to " + str(self.arduino.real_capacitance) + " pF")

    def dc_current_changed(self):
        """
        Function that changes dc current on dc hf_source when it is changed on spinbox
        """
        dc_current = self.sw_dc_current_spinBox.value()
        self.source.set_current(dc_current, channel=1)

        if dc_current > 0 and self.source.dc_output_state == False:
            self.source.output(True, channel=1)
        elif dc_current == 0 and self.source.dc_output_state == True:
            self.source.output(False, channel=1)

        self.sw_dc_current_lcdNumber.display(str(dc_current))
        self.sw_dc_field_lcdNumber.display(str(dc_current * 0.37))
        # self.sw_resistance_lcdNumber.display(str(self.arduino.read_resistance()))

    """
    def resistance_changed(self):
        # Function that changes resistance on arduino when it is changed on spinbox
        resistance = self.sw_resistance_spinBox.value()
        self.arduino.set_resistance(resistance)

        self.sw_resistance_lcdNumber.display(str(resistance))
        # self.sw_resistance_lcdNumber.display(str(self.arduino.read_resistance()))
    """

    def safe_read_setup_parameters(self):
        """
        Read setup parameters and if any important field is missing, return a qmessagebox
        """

        # Read out measurement and setup parameters from GUI
        try:
            setup_parameters = self.read_setup_parameters()
        except ValueError:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(
                "Please set valid device dimensions first in the format 11.5,3.5"
            )
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.setStyleSheet(
                "background-color: rgb(44, 49, 60);\n"
                "color: rgb(255, 255, 255);\n"
                'font: 63 bold 10pt "Segoe UI";\n'
                ""
            )
            msgBox.exec()

            self.specw_start_measurement_pushButton.setChecked(False)

            cf.log_message("No valid device dimensions given")
            raise UserWarning(
                "Please set valid device dimensions first in the format 11.5,3.5"
            )

        # Check if folder path exists
        if (
            setup_parameters["folder_path"] == ""
            or setup_parameters["batch_name"] == ""
        ):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(
                "Please set folder path, batch name and device dimensions first!"
            )
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.setStyleSheet(
                "background-color: rgb(44, 49, 60);\n"
                "color: rgb(255, 255, 255);\n"
                'font: 63 bold 10pt "Segoe UI";\n'
                ""
            )
            msgBox.exec()

            self.specw_start_measurement_pushButton.setChecked(False)

            cf.log_message("Folder path or batchname not defined")
            raise UserWarning(
                "Please set folder path, batchname and device dimensions first!"
            )

        # Now check if the folder path ends on a / otherwise try to add it
        if not setup_parameters["folder_path"][-1] == "/":
            setup_parameters["folder_path"] = setup_parameters["folder_path"] + "/"
            self.sw_folder_path_lineEdit.setText(setup_parameters["folder_path"])

        # Now check if the read out path is a valid path
        if not os.path.isdir(setup_parameters["folder_path"]):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Please enter a valid folder path")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.setStyleSheet(
                "background-color: rgb(44, 49, 60);\n"
                "color: rgb(255, 255, 255);\n"
                'font: 63 bold 10pt "Segoe UI";\n'
                ""
            )
            msgBox.exec()

            self.specw_start_measurement_pushButton.setChecked(False)

            cf.log_message("Folder path not valid")
            raise UserWarning("Please enter a valid folder path!")

        return setup_parameters

    def read_setup_parameters(self):
        """
        Function to read out the current fields entered in the setup tab
        """
        setup_parameters = {
            "folder_path": self.sw_folder_path_lineEdit.text(),
            "batch_name": self.sw_batch_name_lineEdit.text(),
            "device_number": self.sw_device_number_spinBox.value(),
            "device_size": [
                float(x) for x in self.sw_device_size_lineEdit.text().split(",")
            ],
        }

        # Update statusbar
        cf.log_message("Setup parameters read")

        return setup_parameters

    def toggle_source_output(self):
        """
        Function to toggle hf_source output on or off
        """
        # Currently this only works independently of other functions but it
        # checks for the true state of the hf_source
        if self.source.hf_output_state:
            self.source.output(False, channel=2)
            self.specw_start_measurement_pushButton.setChecked(False)
        else:
            self.source.output(True, channel=2)
            self.specw_start_measurement_pushButton.setChecked(True)

    # -------------------------------------------------------------------- #
    # -------------------------- Pulsing Widget -------------------------- #
    # -------------------------------------------------------------------- #
    def toggle_pulsing_constant_parameter_mode(self):
        """
        Toggle the pulsing
        """
        if self.pulsew_constant_parameter_mode_toggleSwitch.isChecked():
            # Update the plot
            pulsing_data = self.read_pulse()
            pulsing_data.loc[pulsing_data.signal == "ON", "hf_field"] = float(
                self.sw_voltage_spinBox.value()
            )
            pulsing_data.loc[pulsing_data.signal == "ON", "dc_field"] = float(
                self.sw_dc_current_spinBox.value()
            )
            pulsing_data.loc[pulsing_data.signal == "ON", "frequency"] = float(
                self.sw_frequency_spinBox.value()
            )
            self.update_pulse_plot(pulsing_data)
            self.statusbar.showMessage(
                "All pulsing information other than timing is ignored. Currently set magnitudes are chosen instead.",
                60,
            )
        else:
            # Update the plot
            pulsing_data = self.read_pulse()
            self.update_pulse_plot(pulsing_data)
            self.statusbar.showMessage(
                "Pulsing information is taken solely from file.", 60
            )

    def pulsing_browse_folder(self):
        """
        Open file dialog to browse through directories
        """
        global_variables = cf.read_global_settings()

        file_path = QtWidgets.QFileDialog.getOpenFileName(
            QtWidgets.QFileDialog(),
            "Select a Pulsing File",
            global_variables["default_saving_path"],
        )
        self.pulsew_folder_path_lineEdit.setText(file_path[0])

        pulsing_data = self.read_pulse()

        self.update_pulse_plot(pulsing_data)
        self.update_time_position(0)

    def read_pulse(self):
        """
        Function that translates the pulse code to time vs magnetic field data
        """
        # Read in data
        # raw_pulsing_data=pd.read_csv("C:\\Users\\GatherLab-Julian\\Desktop\\pulsing.txt", delimiter="\t")
        pulsing_data = pd.read_csv(
            self.pulsew_folder_path_lineEdit.text(), delimiter="\t", skiprows=1
        )

        # Set the fields to zero in case of off state
        pulsing_data.loc[pulsing_data["signal"] == "OFF", "hf_field"] = 0
        pulsing_data.loc[pulsing_data["signal"] == "OFF", "dc_field"] = 0
        pulsing_data["time"] = np.cumsum(pulsing_data["time"].to_numpy())
        return pulsing_data

    def update_pulse_plot(self, pulsing_data):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            lines = self.pulsew_ax.get_lines()
            lines[-1].remove()
        except:
            cf.log_message("Pulsing line can not be deleted")

        # Only for plotting we have to add a line with the zeros
        time = np.append([0], pulsing_data.time.to_list())
        hf_field = np.append([0], pulsing_data.hf_field.to_list())

        # Set x and y limit
        self.pulsew_ax.set_xlim([min(time), max(time)])
        self.pulsew_ax.set_ylim([0, max(hf_field) + 1])

        # Do plotting
        self.pulsew_ax.step(
            time,
            hf_field,
            where="pre",
            color=(85 / 255, 170 / 255, 255 / 255),
        )

        self.pulsew_fig.draw()

    def read_pulsing_sweep_parameters(self):
        """
        Function to read out the current fields entered in the frequency sweep tab
        """
        pulsing_sweep_parameters = {
            "constant_mode": self.pulsew_constant_parameter_mode_toggleSwitch.isChecked(),
        }

        # Update statusbar
        cf.log_message("Pulsing mode parameters read")

        return pulsing_sweep_parameters

    def start_pulsing_sweep(self):
        """
        Function that saves the spectrum (probably by doing another
        measurement and shortly turning on the OLED for a background
        measurement and then saving this into a single file)
        """
        if not self.pulsew_start_measurement_pushButton.isChecked():
            self.pulsing_sweep.kill()
            return

        self.progressBar.show()

        pulsing_sweep_parameters = self.read_pulsing_sweep_parameters()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        pulsing_data = self.read_pulse()

        self.pulsing_sweep = PulsingSweep(
            self.arduino,
            self.source,
            self.oscilloscope,
            pulsing_data,
            pulsing_sweep_parameters,
            parent=self,
        )

        self.pulsing_sweep.start()

    @QtCore.Slot(float)
    def update_time_position(self, current_time):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Do plotting
        vline = self.pulsew_ax.vlines(current_time, 0, 20, color="red")

        self.pulsew_fig.draw()

        vline.remove()

    # -------------------------------------------------------------------- #
    # -------------------------- Frequency Sweep ------------------------- #
    # -------------------------------------------------------------------- #

    def change_current_to_magnetic_field(self):
        """
        Function to toggle hf_source output on or off
        """
        _translate = QtCore.QCoreApplication.translate

        if self.specw_constant_magnetic_field_mode_toggleSwitch.isChecked():
            self.specw_current_label.setText(
                _translate("MainWindow", "Magnetic Field (mT)")
            )
            self.specw_current_spinBox.setSuffix(_translate("MainWindow", " mT"))

        else:
            self.specw_current_label.setText(
                _translate("MainWindow", "Maximum Current (A)")
            )
            self.specw_current_spinBox.setSuffix(_translate("MainWindow", " A"))

    def read_frequency_sweep_parameters(self):
        """
        Function to read out the current fields entered in the frequency sweep tab
        """
        frequency_sweep_parameters = {
            "voltage": self.specw_voltage_spinBox.value(),
            "current_compliance": self.specw_current_spinBox.value(),
            "minimum_frequency": self.specw_minimum_frequency_spinBox.value(),
            "maximum_frequency": self.specw_maximum_frequency_spinBox.value(),
            "autoset_frequency_step": self.specw_autoset_frequency_step_toggleSwitch.isChecked(),
            "frequency_step": self.specw_frequency_step_spinBox.value(),
            "frequency_settling_time": self.specw_frequency_settling_time_spinBox.value(),
            "autoset_capacitance": self.specw_autoset_capacitance_toggleSwitch.isChecked(),
            "constant_magnetic_field_mode": self.specw_constant_magnetic_field_mode_toggleSwitch.isChecked(),
            "dc_magnetic_field": self.specw_dc_magnetic_field_spinBox.value(),
        }

        # Update statusbar
        cf.log_message("Frequency sweep parameters read")

        return frequency_sweep_parameters

    def start_frequency_sweep(self):
        """
        Function that saves the spectrum (probably by doing another
        measurement and shortly turning on the OLED for a background
        measurement and then saving this into a single file)
        """
        if not self.specw_start_measurement_pushButton.isChecked():
            self.frequency_sweep.kill()
            return

        # Load in setup parameters and make sure that the parameters make sense
        setup_parameters = self.safe_read_setup_parameters()
        frequency_sweep_parameters = self.read_frequency_sweep_parameters()

        self.progressBar.show()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        self.frequency_sweep = FrequencyScan(
            self.arduino,
            self.source,
            self.oscilloscope,
            frequency_sweep_parameters,
            setup_parameters,
            parent=self,
        )

        self.frequency_sweep.start()

    @QtCore.Slot(list, list, list, list)
    def update_spectrum(self, frequency, current, magnetic_field, vmax):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            # Delete two times zero because after the first deletion the first element will be element zero
            lines = self.specw_ax.get_lines()
            lines[-1].remove()
            lines2 = self.specw_ax2.get_lines()
            lines2[-1].remove()
            lines2[-2].remove()
        except:
            cf.log_message("Oscilloscope line can not be deleted")

        # Set x and y limit
        self.specw_ax.set_xlim([min(frequency), max(frequency)])
        self.specw_ax.set_ylim([0, max(vmax) + 0.05])

        self.specw_ax2.set_ylim(
            [
                min(np.append(magnetic_field, current)) - 0.05,
                max(np.append(magnetic_field, current)) + 0.05,
            ]
        )

        # Do plotting
        self.specw_ax.plot(
            frequency,
            vmax,
            marker="o",
            color="black",
            label="Vmax, ME (V)",
        )

        self.specw_ax2.plot(
            frequency,
            magnetic_field,
            color=(85 / 255, 170 / 255, 255 / 255),
            marker="o",
            label="Magnetic Field (mT)",
        )

        self.specw_ax2.plot(
            frequency,
            current,
            color="red",
            marker="o",
            label="Current (A)",
        )
        self.specw_ax2.format_coord = self.make_format(self.specw_ax2, self.specw_ax)

        lines, labels = self.specw_ax.get_legend_handles_labels()
        lines2, labels2 = self.specw_ax2.get_legend_handles_labels()
        legend = self.specw_ax2.legend(lines + lines2, labels + labels2, loc="best")
        legend.set_draggable(True)

        self.specw_fig.draw()

    # -------------------------------------------------------------------- #
    # -------------------------- Bias Field Sweep ------------------------ #
    # -------------------------------------------------------------------- #

    def read_dc_field_sweep_parameters(self):
        """
        Function to read out the current fields entered in the frequency sweep tab
        """
        dc_sweep_parameters = {
            "voltage": self.bw_voltage_spinBox.value(),
            "current_compliance": self.bw_current_spinBox.value(),
            "frequency": self.bw_frequency_spinBox.value(),
            "minimum_dc_field": self.bw_minimum_dc_magnetic_field_spinBox.value(),
            "maximum_dc_field": self.bw_maximum_dc_magnetic_field_spinBox.value(),
            "dc_field_step": self.bw_dc_magnetic_field_step_spinBox.value(),
            "bias_field_settling_time": self.bw_dc_magnetic_field_settling_time_spinBox.value(),
            "autoset_capacitance": self.bw_autoset_capacitance_toggleSwitch.isChecked(),
            "constant_magnetic_field_mode": self.bw_constant_magnetic_field_mode_toggleSwitch.isChecked(),
            "reverse_sweep": self.bw_reverse_sweep_toggleSwitch.isChecked(),
        }

        # Update statusbar
        cf.log_message("Bias field sweep parameters read")

        return dc_sweep_parameters

    def start_dc_field_sweep(self):
        """
        Function to start the dc field measurement
        """
        if not self.bw_start_measurement_pushButton.isChecked():
            self.bias_field_sweep.kill()
            return

        # Load in setup parameters and make sure that the parameters make sense
        setup_parameters = self.safe_read_setup_parameters()
        dc_sweep_parameters = self.read_dc_field_sweep_parameters()

        self.progressBar.show()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        self.bias_field_sweep = BiasScan(
            self.arduino,
            self.source,
            self.oscilloscope,
            dc_sweep_parameters,
            setup_parameters,
            parent=self,
        )

        self.bias_field_sweep.start()

    @QtCore.Slot(list, list, list, list)
    def update_bias_plot(self, current, dc_field, me_voltage, hf_magnetic_field):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            # Delete two times zero because after the first deletion the first element will be element zero
            lines = self.bw_ax.get_lines()
            lines[-1].remove()
            lines2 = self.bw_ax2.get_lines()
            lines2[-1].remove()
        except:
            cf.log_message("Plot lines could not be deleted")

        # Set x and y limit
        self.bw_ax.set_xlim([min(dc_field), max(dc_field)])
        self.bw_ax.set_ylim([0, max(np.append(me_voltage, hf_magnetic_field)) + 0.05])

        # Plot current
        self.bw_ax.plot(
            dc_field,
            me_voltage,
            color="black",
            marker="o",
        )

        self.bw_ax2.plot(
            dc_field,
            hf_magnetic_field,
            color=(85 / 255, 170 / 255, 255 / 255),
            marker="o",
        )

        # lines, labels = self.bw_ax.legend(loc="best")
        self.bw_ax2.format_coord = self.make_format(self.bw_ax2, self.bw_ax)

        self.bw_fig.draw()

    # -------------------------------------------------------------------- #
    # -------------------------- HF Field Scan --------------------------- #
    # -------------------------------------------------------------------- #

    def read_hf_field_sweep_parameters(self):
        """
        Function to read out the current fields entered in the frequency sweep tab
        """
        hf_sweep_parameters = {
            "voltage_compliance": self.hfw_voltage_compliance_spinBox.value(),
            "dc_magnetic_field": self.hfw_dc_magnetic_field_spinBox.value(),
            "frequency": self.hfw_frequency_spinBox.value(),
            "minimum_hf_voltage": self.hfw_minimum_voltage_spinBox.value(),
            "maximum_hf_voltage": self.hfw_maximum_voltage_spinBox.value(),
            "hf_voltage_step": self.hfw_voltage_step_spinBox.value(),
            "hf_field_settling_time": self.hfw_voltage_settling_time_spinBox.value(),
            "autoset_capacitance": self.hfw_autoset_capacitance_toggleSwitch.isChecked(),
            "constant_magnetic_field_mode": self.hfw_constant_magnetic_field_mode_toggleSwitch.isChecked(),
        }

        # Update statusbar
        cf.log_message("HF field sweep parameters read")

        return hf_sweep_parameters

    def start_hf_field_sweep(self):
        """
        Function to start the power measurement
        """
        if not self.hfw_start_measurement_pushButton.isChecked():
            self.hf_field_sweep.kill()
            return

        # Load in setup parameters and make sure that the parameters make sense
        setup_parameters = self.safe_read_setup_parameters()
        hf_field_sweep_parameters = self.read_hf_field_sweep_parameters()

        self.progressBar.show()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        self.hf_field_sweep = HFScan(
            self.arduino,
            self.source,
            self.oscilloscope,
            hf_field_sweep_parameters,
            setup_parameters,
            parent=self,
        )

        self.hf_field_sweep.start()

    @QtCore.Slot(list, list, list, list)
    def update_hf_plot(self, hf_field, me_voltage):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            # Delete two times zero because after the first deletion the first element will be element zero
            lines = self.hfw_ax.get_lines()
            lines[-1].remove()
            # del self.hfw_ax2.lines[0]
        except:
            cf.log_message("Plot lines could not be deleted")

        # Set x and y limit
        self.hfw_ax.set_xlim([min(hf_field), max(hf_field)])
        self.hfw_ax.set_ylim([0, max(me_voltage) + 0.05])

        # Plot current
        self.hfw_ax.plot(
            hf_field,
            me_voltage,
            color="black",
            marker="o",
        )

        # self.hfw_ax2.plot(
        #     hf_field,
        #     hf_magnetic_field,
        #     color=(85 / 255, 170 / 255, 255 / 255),
        #     marker="o",
        # )

        # lines, labels = self.hfw_ax.legend(loc="best")

        self.hfw_fig.draw()

    @QtCore.Slot(str)
    def pause_hf_measurement(self, status):
        """
        Function to ask to turn the PL lamp on before continuing
        """
        msgBox = QtWidgets.QMessageBox()
        # Now check which message to display (turn on or off the lamp)
        if status == "on":
            msgBox.setText("You can now insert the OLED")
        elif status == "off":
            msgBox.setText("You can now take out the OLED")

        msgBox.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel
        )
        msgBox.setStyleSheet(
            "QWidget {\n"
            "            background-color: rgb(44, 49, 60);\n"
            "            color: rgb(255, 255, 255);\n"
            '            font: 63 10pt "Segoe UI";\n'
            "}\n"
            "QPushButton {\n"
            "            border: 2px solid rgb(52, 59, 72);\n"
            "            border-radius: 5px;\n"
            "            background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:hover {\n"
            "            background-color: rgb(57, 65, 80);\n"
            "            border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "            background-color: rgb(35, 40, 49);\n"
            "            border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "QPushButton:checked {\n"
            "            background-color: rgb(35, 40, 49);\n"
            "            border: 2px solid rgb(85, 170, 255);\n"
            "}"
        )
        button = msgBox.exec()

        if button == QtWidgets.QMessageBox.Ok:
            self.hf_field_sweep.pause = "break"
        elif button == QtWidgets.QMessageBox.Cancel:
            self.hf_field_sweep.pause = "return"
            self.hfw_start_measurement_pushButton.setChecked(False)

    # -------------------------------------------------------------------- #
    # -------------------------- Lifetime Scan --------------------------- #
    # -------------------------------------------------------------------- #

    def read_lt_sweep_parameters(self):
        """
        Function to read out the current fields entered in the frequency sweep tab
        """
        dc_sweep_parameters = {
            "voltage_compliance": self.ltw_voltage_compliance_spinBox.value(),
            "dc_magnetic_field": self.ltw_dc_magnetic_field_spinBox.value(),
            "frequency": self.ltw_frequency_spinBox.value(),
            "hf_voltage": self.ltw_hf_magnetic_field_spinBox.value(),
            "total_time": self.ltw_total_time_spinBox.value(),
            "time_step": self.ltw_time_step_spinBox.value(),
            "autoset_capacitance": self.ltw_autoset_capacitance_toggleSwitch.isChecked(),
            "constant_magnetic_field_mode": self.ltw_constant_magnetic_field_mode_toggleSwitch.isChecked(),
        }

        # Update statusbar
        cf.log_message("Power sweep parameters read")

        return dc_sweep_parameters

    def start_lt_sweep(self):
        """
        Function to start the power measurement
        """
        if not self.ltw_start_measurement_pushButton.isChecked():
            self.lt_sweep.kill()
            return

        # Load in setup parameters and make sure that the parameters make sense
        setup_parameters = self.safe_read_setup_parameters()
        lt_sweep_parameters = self.read_lt_sweep_parameters()

        self.progressBar.show()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        self.lt_sweep = LTScan(
            self.arduino,
            self.source,
            self.oscilloscope,
            lt_sweep_parameters,
            setup_parameters,
            parent=self,
        )

        self.lt_sweep.start()

    @QtCore.Slot(list, list, list)
    def update_lt_plot(self, time, me_voltage, magnetic_field):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            # Delete two times zero because after the first deletion the first element will be element zero
            lines = self.ltw_ax.get_lines()
            lines[-1].remove()
            lines2 = self.ltw_ax2.get_lines()
            lines2[-1].remove()
            # del self.ltw_ax2.lines[0]
        except:
            cf.log_message("Plot lines could not be deleted")

        # Set x and y limit
        self.ltw_ax.set_xlim([min(time), max(time)])
        self.ltw_ax.set_ylim([0, max(me_voltage) * 1.01])

        # Plot current
        self.ltw_ax.plot(
            time,
            me_voltage,
            color="black",
            marker="o",
        )

        self.ltw_ax2.plot(
            time,
            magnetic_field,
            color=(85 / 255, 170 / 255, 255 / 255),
            marker="o",
            label="Magnetic Field (mT)",
        )

        # self.ltw_ax2.plot(
        #     hf_field,
        #     hf_magnetic_field,
        #     color=(85 / 255, 170 / 255, 255 / 255),
        #     marker="o",
        # )

        # lines, labels = self.ltw_ax.legend(loc="best")

        self.ltw_ax2.format_coord = self.make_format(self.ltw_ax2, self.ltw_ax)

        lines, labels = self.ltw_ax.get_legend_handles_labels()
        lines2, labels2 = self.ltw_ax2.get_legend_handles_labels()
        legend = self.ltw_ax2.legend(lines + lines2, labels + labels2, loc="best")
        legend.set_draggable(True)

        self.ltw_fig.draw()

    @QtCore.Slot(str)
    def pause_lt_measurement(self, status):
        """
        Function to ask to turn the PL lamp on before continuing
        """
        msgBox = QtWidgets.QMessageBox()
        # Now check which message to display (turn on or off the lamp)
        if status == "on":
            msgBox.setText("You can now insert the OLED")
        elif status == "off":
            msgBox.setText("You can now take out the OLED")

        msgBox.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel
        )
        msgBox.setStyleSheet(
            "QWidget {\n"
            "            background-color: rgb(44, 49, 60);\n"
            "            color: rgb(255, 255, 255);\n"
            '            font: 63 10pt "Segoe UI";\n'
            "}\n"
            "QPushButton {\n"
            "            border: 2px solid rgb(52, 59, 72);\n"
            "            border-radius: 5px;\n"
            "            background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:hover {\n"
            "            background-color: rgb(57, 65, 80);\n"
            "            border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "            background-color: rgb(35, 40, 49);\n"
            "            border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "QPushButton:checked {\n"
            "            background-color: rgb(35, 40, 49);\n"
            "            border: 2px solid rgb(85, 170, 255);\n"
            "}"
        )
        button = msgBox.exec()

        if button == QtWidgets.QMessageBox.Ok:
            self.lt_sweep.pause = "break"
        elif button == QtWidgets.QMessageBox.Cancel:
            self.lt_sweep.pause = "return"
            self.ltw_start_measurement_pushButton.setChecked(False)

    # -------------------------------------------------------------------- #
    # -------------------------- Capacitor Sweep ------------------------- #
    # -------------------------------------------------------------------- #
    def read_capacitance_sweep_parameters(self):
        """
        Function to read out the current fields entered in the capacitance sweep tab
        """
        capacitance_sweep_parameters = {
            "voltage": self.capw_voltage_spinBox.value(),
            "current_compliance": self.capw_current_spinBox.value(),
            "minimum_frequency": self.capw_minimum_frequency_spinBox.value(),
            "maximum_frequency": self.capw_maximum_frequency_spinBox.value(),
            "frequency_step": self.capw_frequency_step_spinBox.value(),
            "resonance_frequency_step": self.capw_resonance_frequency_step_spinBox.value(),
            "frequency_margin": self.capw_frequency_margin_spinBox.value(),
            "frequency_settling_time": self.capw_frequency_settling_time_spinBox.value(),
        }

        # Update statusbar
        cf.log_message("Capacitance sweep parameters read")

        return capacitance_sweep_parameters

    def start_capacitance_sweep(self):
        """
        Function that saves the spectrum (probably by doing another
        measurement and shortly turning on the OLED for a background
        measurement and then saving this into a single file)
        """
        if not self.capw_start_measurement_pushButton.isChecked():
            self.capacitance_sweep.kill()
            return

        # Load in setup parameters and make sure that the parameters make sense
        setup_parameters = self.safe_read_setup_parameters()
        capacitance_sweep_parameters = self.read_capacitance_sweep_parameters()

        self.progressBar.show()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        self.capacitance_sweep = CapacitanceScan(
            self.arduino,
            self.source,
            # self.oscilloscope,
            capacitance_sweep_parameters,
            setup_parameters,
            parent=self,
        )

        self.capacitance_sweep.start()

    @QtCore.Slot(list, list, list, str, bool, str, bool)
    def update_capacitance_spectrum(
        self, frequency, current, limits, label, first_bool, color, fit
    ):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        # Always delete the last line except when first_bool = True which is
        # the case, for the first time a new capacitor is introduced
        if not first_bool:
            try:
                lines = self.capw_ax.get_lines()
                lines[-1].remove()
                # del self.specw_ax.lines[0]
            except:
                cf.log_message("Spectrum line can not be deleted")

        # Set x and y limit
        self.capw_ax.set_xlim([limits[0], limits[1]])
        # self.capw_ax.set_ylim([min(current) - 0.2, max(current) + 0.2])

        # self.specw_ax2.set_ylim([min(vpp) - 0.2, max(vpp) + 0.2])

        # Plot current
        if fit == True:
            self.capw_ax.plot(frequency, current, color=color)
        else:
            # Plot with linewidth zero is chosen instead of scatter to ensure that lines can be deleted correctly
            self.capw_ax.plot(
                frequency, current, marker="o", linewidth=0, color=color, label=label
            )

        # Only regenerate the legend if the line is the first
        if first_bool:
            legend = self.capw_ax.legend()
            legend.set_draggable(True)

        # self.specw_ax2.plot(
        #     frequency,
        #     vpp,
        #     color=(85 / 255, 170 / 255, 255 / 255),
        #     marker="o",
        # )

        self.capw_fig.draw()

    # -------------------------------------------------------------------- #
    # -------------------------- Oscilloscope ---------------------------- #
    # -------------------------------------------------------------------- #
    @QtCore.Slot(list, list, list)
    def plot_oscilloscope(self, time, voltage, time2, voltage2):
        """
        Function that plots the oscilloscope image
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            lines = self.ow_ax.get_lines()
            lines[-1].remove()
            lines[-2].remove()
        except:
            cf.log_message("Oscilloscope line can not be deleted")

        # Set x and y limit
        self.ow_ax.set_xlim([min(time), max(time)])
        self.ow_ax.set_ylim(
            [
                min(np.append(voltage, voltage2)) * 1.05,
                max(np.append(voltage, voltage2)) * 1.05,
            ]
        )

        # Plot current
        self.ow_ax.plot(
            time,
            voltage,
            color="orange",
            label="CHAN1"
            # marker="o",
        )

        self.ow_ax.plot(
            time2,
            voltage2,
            color=(85 / 255, 170 / 255, 255 / 255),
            label="CHAN2"
            # marker="o",
        )

        legend = self.ow_ax.legend(loc="best")

        self.ow_fig.draw()

        self.ow_vmax_chan1_lcdNumber.display(max(voltage))
        self.ow_vmax_chan2_lcdNumber.display(max(voltage2))

    def stop_osci(self):
        """
        Function to start and stop the oscilloscope
        """

        # Start and stop the oscilloscope
        if self.ow_stop_pushButton.isChecked():
            self.oscilloscope.stop()
            self.oscilloscope_thread.pause = True
            # self.ow_stop_pushButton.setChecked(False)
        else:
            self.oscilloscope.run()
            self.oscilloscope_thread.pause = False
            # self.ow_stop_pushButton.setChecked(True)

    def auto_scale_osci(self):
        """
        Function to call the autoscale function of the oscilloscope
        """
        self.oscilloscope.auto_scale()

    def save_osci(self):
        """
        Save Data that is currently visible on oscilloscope to file
        """
        # Read parameters
        setup_parameters = self.safe_read_setup_parameters()

        # Read data
        time_data, data = self.oscilloscope.get_data("CHAN1")
        time_data2, data2 = self.oscilloscope.get_data("CHAN2")
        df = pd.DataFrame(
            columns=["time_chan1", "voltage_chan1", "time_chan2", "voltage_chan2"]
        )
        df.time_chan1 = time_data
        df.voltage_chan1 = data
        df.time_chan2 = time_data2
        df.voltage_chan2 = data2

        variables = self.oscilloscope.measure()

        # Define Header
        line01 = "VPP:   " + str(variables[0]) + " V \t"
        line02 = "### Measurement data ###"
        line03 = (
            "Time Channel 1\t Voltage Channel 1\t Time Channel 2\t Voltage Channel 2"
        )
        line04 = "s\t V\t s\t V\n"

        header_lines = [
            line01,
            line02,
            line03,
            line04,
        ]

        # Write header lines to file
        file_path = (
            setup_parameters["folder_path"]
            + dt.date.today().strftime("%Y-%m-%d_")
            + setup_parameters["batch_name"]
            + "_d"
            + str(setup_parameters["device_number"])
            + "_osci"
            + ".csv"
        )

        cf.save_file(df, file_path, header_lines)

    ################################################################################
    ############################ PID Tuning ########################################
    ################################################################################

    def read_pid_sweep_parameters(self):
        """
        Function to read out the current fields entered in the frequency sweep tab
        """
        pid_sweep_parameters = {
            "voltage": self.pidw_voltage_spinBox.value(),
            "magnetic_field": self.pidw_current_spinBox.value(),
            "frequency": self.pidw_frequency_spinBox.value(),
            # "frequency_settling_time": self.pidw_frequency_settling_time_spinBox.value(),
            "autoset_capacitance": self.pidw_autoset_capacitance_toggleSwitch.isChecked(),
        }

        # Update statusbar
        cf.log_message("PID sweep parameters read")

        return pid_sweep_parameters

    def start_pid_measurement(self):
        """
        Function that saves the spectrum (probably by doing another
        measurement and shortly turning on the OLED for a background
        measurement and then saving this into a single file)
        """
        if not self.pidw_start_measurement_pushButton.isChecked():
            self.pid_sweep.kill()
            return

        # Load in setup parameters and make sure that the parameters make sense
        # setup_parameters = self.safe_read_setup_parameters()
        pid_parameters = self.read_pid_sweep_parameters()

        self.progressBar.show()

        # self.arduino.set_capacitance(False)
        time.sleep(1)

        self.pid_sweep = PIDScan(
            self.arduino,
            self.source,
            self.oscilloscope,
            pid_parameters,
            # setup_parameters,
            parent=self,
        )

        self.pid_sweep.start()

    @QtCore.Slot(list, list, list, list)
    def update_pid_graph(self, time, magnetic_field):
        """
        Function that is continuously evoked when the spectrum is updated by
        the other thread
        """
        # Clear plot
        # self.specw_ax.cla()
        try:
            # Delete two times zero because after the first deletion the first element will be element zero
            lines = self.pidw_ax.get_lines()
            lines[-1].remove()
            lines[-2].remove()
            # del self.pidw_ax2.lines[0]
        except:
            pass

        # Set x and y limit
        self.pidw_ax.set_xlim([min(time), max(time)])
        self.pidw_ax.set_ylim([0, max(magnetic_field) + 0.05])

        # self.pidw_ax2.set_ylim(
        #     [
        #         min(vmax) - 0.05,
        #         max(vmax) + 0.05,
        #     ]
        # )

        # Plot current
        self.pidw_ax.plot(
            time,
            magnetic_field,
            color="black",
            marker="o",
            label="Magnetic Field",
        )

        # self.pidw_ax.plot(
        #     time,
        #     current,
        #     color="red",
        #     marker="o",
        #     label="Current (A)",
        # )

        # self.pidw_ax2.plot(
        #     time,
        #     vmax,
        #     color=(85 / 255, 170 / 255, 255 / 255),
        #     marker="o",
        #     label="Vmax Induced",
        # )

        lines, labels = self.pidw_ax.get_legend_handles_labels()
        # lines2, labels2 = self.pidw_ax2.get_legend_handles_labels()
        # legend = self.pidw_ax2.legend(lines + lines2, labels + labels2, loc="best")
        # legend.set_draggable(True)

        self.pidw_fig.draw()


# Logging
# Prepare file path etc. for logging
LOG_FILENAME = "./usr/log.out"
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format=(
        "%(asctime)s - [%(levelname)s] -"
        " (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    ),
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# Activate log_rotate to rotate log files after it reached 1 MB size ()
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=1000000)
logging.getLogger("Rotating Log").addHandler(handler)


# ---------------------------------------------------------------------------- #
# -------------------- This is to execute the program ------------------------ #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()

    # Icon (see https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105)
    import ctypes

    # myappid = u"mycompan.myproduct.subproduct.version"  # arbitrary string
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app_icon = QtGui.QIcon()
    app_icon.addFile("./icons/program_icon.png", QtCore.QSize(256, 256))
    app.setWindowIcon(app_icon)

    ui.show()
    sys.exit(app.exec())
