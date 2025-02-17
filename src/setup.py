from PySide6 import QtCore

import time


class SetupThread(QtCore.QThread):
    """
    Class thread that manages the constant read out of current, voltage and frequency
    """

    # Define costum signals
    # https://stackoverflow.com/questions/36434706/pyqt-proper-use-of-emit-and-pyqtsignal
    # With pyside2 https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    update_display = QtCore.Signal(float, float, float, float)

    def __init__(self, source, arduino, parent=None):
        super(SetupThread, self).__init__()
        # Variable to kill thread
        self.is_killed = False
        self.pause = False

        # Assign hardware and reset
        self.arduino = arduino
        self.arduino.init_serial_connection()
        self.source = source
        # self.oscilloscope = oscilloscope

        # Connect signal to the updater from the parent class
        self.update_display.connect(parent.update_display)

    def run(self):
        """
        Class that continuously measures the spectrum
        """

        import pydevd

        pydevd.settrace(suspend=False)

        while True:
            reference_time = time.time()
            # Measure
            voltage, current = self.source.read_values(channel=2)
            dc_voltage, dc_current, dc_magnetic_field = self.source.read_values(
                channel=1
            )
            # frequency = self.arduino.read_frequency()

            self.update_display.emit(voltage, current, dc_current, dc_magnetic_field)
            print("elapsed time: " + str(time.time() - reference_time))

            # The sleep time here is very important because if it is chosen too
            # short, the program may crash. Currently 1 s seems to be save (one
            # can at least go down to 0.5s). The reason is the latency of the
            # hf_source.
            time.sleep(1)

            if self.pause:
                while True:
                    time.sleep(0.5)

                    if not self.pause:
                        break

            if self.is_killed:
                self.quit()
                break

    def kill(self):
        """
        Kill this thread by stopping the loop
        """
        self.arduino.close_serial_connection()

        # Turn hf_source off
        self.source.output(False, channel=1)
        self.source.output(False, channel=2)

        # Trigger interruption of run sequence
        self.is_killed = True
