from UI_toggle_switch import ToggleSwitch

from PySide6 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure


# ---------------------------------------------------------------------------- #
# --------------------------- Define Main Window ----------------------------- #
# ---------------------------------------------------------------------------- #
class Ui_MainWindow(object):
    """
    Class that contains all information about the main window
    """

    def setupUi(self, MainWindow):
        """
        Setup that sets all gui widgets at their place
        """

        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(
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
            "QLineEdit {\n"
            "            border: 2px solid rgb(61, 70, 86);\n"
            "            border-radius: 5px;\n"
            "            background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSpinBox {\n"
            "            border: 2px solid rgb(61, 70, 86);\n"
            "            border-radius: 5px;\n"
            "            background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QDoubleSpinBox {\n"
            "            border: 2px solid rgb(61, 70, 86);\n"
            "            border-radius: 5px;\n"
            "            background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QScrollArea {\n"
            "            border: 2px solid rgb(61, 70, 86);\n"
            "            border-radius: 5px;\n"
            "}\n"
            "QScrollBar {\n"
            "            border-radius: 5px;\n"
            "            background: rgb(61, 70, 86);\n"
            "}\n"
            "QScrollBar:add-page {\n"
            "            background: rgb(52, 59, 72);\n"
            "}\n"
            "QScrollBar:sub-page {\n"
            "            background: rgb(52, 59, 72);\n"
            "}\n"
        )

        self.center()

        # Define central widget of the MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setStyleSheet(
        #     "QLineEdit {\n"
        #     "            border: 2px solid rgb(61, 70, 86);\n"
        #     "            border-radius: 5px;\n"
        #     "            background-color: rgb(52, 59, 72);\n"
        #     "}\n"
        #     "QSpinBox {\n"
        #     "            border: 2px solid rgb(61, 70, 86);\n"
        #     "            border-radius: 5px;\n"
        #     "            background-color: rgb(52, 59, 72);\n"
        #     "}\n"
        #     "QDoubleSpinBox {\n"
        #     "            border: 2px solid rgb(61, 70, 86);\n"
        #     "            border-radius: 5px;\n"
        #     "            background-color: rgb(52, 59, 72);\n"
        #     "}\n"
        #     "QScrollArea {\n"
        #     "            border: 2px solid rgb(61, 70, 86);\n"
        #     "            border-radius: 5px;\n"
        #     "}\n"
        #     "QScrollBar {\n"
        #     # "            border: 2px solid rgb(85, 170, 255);\n"
        #     "            border-radius: 5px;\n"
        #     "            background: rgb(61, 70, 86);\n"
        #     "}\n"
        #     "QScrollBar:add-page {\n"
        #     "            background: rgb(52, 59, 72);\n"
        #     "}\n"
        #     "QScrollBar:sub-page {\n"
        #     "            background: rgb(52, 59, 72);\n"
        #     "}\n"
        # )
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 6)
        self.gridLayout.setObjectName("gridLayout")

        # This here shall be the logo of the program
        # self.gatherlab_picture = QtWidgets.QWidget(self.centralwidget)
        # self.gatherlab_picture.setObjectName("gatherlab_picture")
        self.gatherlab_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("icons/logo_cropped2.png")
        self.gatherlab_label.setPixmap(pixmap)
        self.gatherlab_label.setScaledContents(True)
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.gatherlab_picture.setLayout(self.horizontalLayout_2)
        self.gatherlab_label.setMinimumSize(50, 50)
        self.gridLayout.addWidget(self.gatherlab_label, 0, 0, 1, 1)

        # Tab widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet(
            "QTabBar {\n"
            "        font-weight: bold;\n"
            "}\n"
            "QTabBar:tab {\n"
            "            background: rgb(52, 59, 72);\n"
            "}\n"
            "QTabBar:tab:selected {\n"
            "            background: rgb(61, 70, 86);\n"
            "            color: rgb(85, 170, 255);\n"
            "}\n"
            "QTabBar:tab:hover {\n"
            "            color: rgb(85, 170, 255);\n"
            "}\n"
            "QTabWidget:pane {\n"
            "            border: 2px solid rgb(52, 59, 72);\n"
            "}\n"
            "QTabBar:tab:disabled {\n"
            "            width: 80px;\n"
            "            color: rgb(44, 49, 60);\n"
            "            background: rgb(44, 49, 60);\n"
            "}\n"
        )

        # -------------------------------------------------------------------- #
        # --------------------------- Setup widget --------------------------- #
        # -------------------------------------------------------------------- #
        self.setup_widget = QtWidgets.QWidget()
        self.setup_widget.setObjectName("setup_widget")
        # self.gridLayout_5 = QtWidgets.QGridLayout(self.setup_widget)
        # self.gridLayout_5.setObjectName("gridLayout_5")
        # self.setup_sub_widget = QtWidgets.QWidget(self.setup_widget)
        # self.setup_sub_widget.setObjectName("setup_sub_widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.setup_widget)
        self.gridLayout_7.setObjectName("gridLayout_7")

        # Setup widget header 1
        self.sw_header1_label = QtWidgets.QLabel(self.setup_widget)
        self.sw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.sw_header1_label.setObjectName("sw_header1_label")
        self.gridLayout_7.addWidget(self.sw_header1_label, 0, 0, 1, 1)

        # Setup widget header
        # self.sw_header2_label = QtWidgets.QLabel(self.setup_widget)
        # self.sw_header2_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        # self.sw_header2_label.setObjectName("sw_header2_label")
        # self.gridLayout_7.addWidget(self.sw_header2_label, 5, 0, 1, 1)

        # Setup widget base folder path
        self.sw_folder_path_horizontalLayout = QtWidgets.QHBoxLayout()
        self.sw_folder_path_horizontalLayout.setObjectName(
            "sw_folder_path_horizontalLayout"
        )
        self.sw_folder_path_lineEdit = QtWidgets.QLineEdit(self.setup_widget)
        self.sw_folder_path_lineEdit.setReadOnly(False)
        self.sw_folder_path_lineEdit.setObjectName("sw_folder_path_lineEdit")
        self.sw_folder_path_horizontalLayout.addWidget(self.sw_folder_path_lineEdit)
        self.sw_browse_pushButton = QtWidgets.QPushButton(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_browse_pushButton.sizePolicy().hasHeightForWidth()
        )
        self.sw_browse_pushButton.setSizePolicy(sizePolicy)
        self.sw_browse_pushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.sw_browse_pushButton.setObjectName("sw_browse_pushButton")
        self.sw_folder_path_horizontalLayout.addWidget(self.sw_browse_pushButton)
        self.gridLayout_7.addLayout(self.sw_folder_path_horizontalLayout, 1, 1, 1, 1)
        self.sw_folder_path_label = QtWidgets.QLabel(self.setup_widget)
        self.sw_folder_path_label.setObjectName("sw_folder_path_label")
        self.gridLayout_7.addWidget(self.sw_folder_path_label, 1, 0, 1, 1)

        # Setup widget batch name
        self.sw_batch_name_label = QtWidgets.QLabel(self.setup_widget)
        self.sw_batch_name_label.setObjectName("sw_batch_name_label")
        self.gridLayout_7.addWidget(self.sw_batch_name_label, 2, 0, 1, 1)
        self.sw_batch_name_lineEdit = QtWidgets.QLineEdit(self.setup_widget)
        self.sw_batch_name_lineEdit.setObjectName("sw_batch_name_lineEdit")
        self.gridLayout_7.addWidget(self.sw_batch_name_lineEdit, 2, 1, 1, 1)

        # Setup widget device number
        self.sw_device_number_label = QtWidgets.QLabel(self.setup_widget)
        self.sw_device_number_label.setObjectName("sw_device_number_label")
        self.gridLayout_7.addWidget(self.sw_device_number_label, 3, 0, 1, 1)
        self.sw_device_number_spinBox = QtWidgets.QSpinBox(self.setup_widget)
        self.sw_device_number_spinBox.setObjectName("sw_device_number_spinBox")
        self.gridLayout_7.addWidget(self.sw_device_number_spinBox, 3, 1, 1, 1)

        # Setup widget device size
        self.sw_device_size_label = QtWidgets.QLabel(self.setup_widget)
        self.sw_device_size_label.setObjectName("sw_device_size_label")
        self.gridLayout_7.addWidget(self.sw_device_size_label, 4, 0, 1, 1)
        self.sw_device_size_lineEdit = QtWidgets.QLineEdit(self.setup_widget)
        self.sw_device_size_lineEdit.setObjectName("sw_device_size_lineEdit")
        self.gridLayout_7.addWidget(self.sw_device_size_lineEdit, 4, 1, 1, 1)

        # Setup widget documentation
        # self.sw_documentation_textEdit = QtWidgets.QTextEdit(self.setup_widget)
        # self.sw_documentation_textEdit.setObjectName("sw_documentation_textEdit")
        # self.gridLayout_7.addWidget(self.sw_documentation_textEdit, 12, 1, 1, 1)
        # self.sw_documentation_label = QtWidgets.QLabel(self.setup_widget)
        # self.sw_documentation_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        # self.sw_documentation_label.setObjectName("sw_documentation_label")
        # self.gridLayout_7.addWidget(self.sw_documentation_label, 12, 0, 1, 1)

        # Header 2
        self.sw_header2_label = QtWidgets.QLabel(self.setup_widget)
        self.sw_header2_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.sw_header2_label.setObjectName("sw_header2_label")
        self.gridLayout_7.addWidget(self.sw_header2_label, 5, 0, 1, 1)

        # Current LCD number widget
        self.sw_source_vc_horizonalLayout = QtWidgets.QHBoxLayout()
        self.sw_current_field_verticalLayout = QtWidgets.QVBoxLayout()

        self.sw_current_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_current_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_current_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_current_lcdNumber.setDigitCount(10)
        self.sw_current_lcdNumber.setAutoFillBackground(False)
        self.sw_current_lcdNumber.setSmallDecimalPoint(False)
        self.sw_current_lcdNumber.setObjectName("sw_current_lcdNumber")

        self.sw_current_field_verticalLayout.addWidget(self.sw_current_lcdNumber)

        # AC Magnetic Field
        self.sw_hf_field_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_hf_field_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_hf_field_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_hf_field_lcdNumber.setDigitCount(10)
        self.sw_hf_field_lcdNumber.setAutoFillBackground(False)
        self.sw_hf_field_lcdNumber.setSmallDecimalPoint(False)
        self.sw_hf_field_lcdNumber.setObjectName("sw_hf_field_lcdNumber")
        self.sw_current_field_verticalLayout.addWidget(self.sw_hf_field_lcdNumber)

        # Voltage LCD number widget
        self.sw_voltage_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_voltage_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_voltage_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_voltage_lcdNumber.setDigitCount(3)
        self.sw_voltage_lcdNumber.setAutoFillBackground(False)
        self.sw_voltage_lcdNumber.setSmallDecimalPoint(False)
        self.sw_voltage_lcdNumber.setObjectName("sw_voltage_lcdNumber")
        # self.sw_voltage_lcdNumber.display("10 U")

        # Frequency LCD number widget
        self.sw_frequency_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_frequency_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_frequency_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_frequency_lcdNumber.setDigitCount(10)
        self.sw_frequency_lcdNumber.setAutoFillBackground(False)
        self.sw_frequency_lcdNumber.setSmallDecimalPoint(False)
        self.sw_frequency_lcdNumber.setObjectName("sw_frequency_lcdNumber")

        # capacitance LCD number widget
        self.sw_capacitance_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_capacitance_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_capacitance_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_capacitance_lcdNumber.setDigitCount(10)
        self.sw_capacitance_lcdNumber.setAutoFillBackground(False)
        self.sw_capacitance_lcdNumber.setSmallDecimalPoint(False)
        self.sw_capacitance_lcdNumber.setObjectName("sw_capacitance_lcdNumber")

        # DC Source Current
        self.sw_dc_current_field_verticalLayout = QtWidgets.QVBoxLayout()

        self.sw_dc_current_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_dc_current_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_dc_current_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_dc_current_lcdNumber.setDigitCount(10)
        self.sw_dc_current_lcdNumber.setAutoFillBackground(False)
        self.sw_dc_current_lcdNumber.setSmallDecimalPoint(False)
        self.sw_dc_current_lcdNumber.setObjectName("sw_dc_current_lcdNumber")

        self.sw_dc_current_field_verticalLayout.addWidget(self.sw_dc_current_lcdNumber)

        # DC Magnetic Field
        self.sw_dc_field_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_dc_field_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_dc_field_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_dc_field_lcdNumber.setDigitCount(10)
        self.sw_dc_field_lcdNumber.setAutoFillBackground(False)
        self.sw_dc_field_lcdNumber.setSmallDecimalPoint(False)
        self.sw_dc_field_lcdNumber.setObjectName("sw_dc_field_lcdNumber")
        self.sw_dc_current_field_verticalLayout.addWidget(self.sw_dc_field_lcdNumber)

        """
        # resistance LCD number widget
        self.sw_resistance_lcdNumber = QtWidgets.QLCDNumber(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sw_resistance_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.sw_resistance_lcdNumber.setSizePolicy(sizePolicy)
        self.sw_resistance_lcdNumber.setDigitCount(10)
        self.sw_resistance_lcdNumber.setAutoFillBackground(False)
        self.sw_resistance_lcdNumber.setSmallDecimalPoint(False)
        self.sw_resistance_lcdNumber.setObjectName("sw_resistance_lcdNumber")
        """

        self.sw_source_vc_horizonalLayout.addWidget(self.sw_voltage_lcdNumber)
        self.sw_source_vc_horizonalLayout.addLayout(
            self.sw_current_field_verticalLayout
        )
        self.sw_source_vc_horizonalLayout.addWidget(self.sw_frequency_lcdNumber)
        self.sw_source_vc_horizonalLayout.addWidget(self.sw_capacitance_lcdNumber)
        self.sw_source_vc_horizonalLayout.addLayout(
            self.sw_dc_current_field_verticalLayout
        )
        # self.sw_source_vc_horizonalLayout.addWidget(self.sw_resistance_lcdNumber)

        self.gridLayout_7.addLayout(self.sw_source_vc_horizonalLayout, 6, 0, 1, 2)

        # Setup widget current tester voltage
        # self.sw_change_voltage_label = QtWidgets.QLabel(self.setup_widget)
        # self.sw_change_voltage_label.setObjectName("sw_change_voltage_label")
        # self.gridLayout_7.addWidget(self.sw_change_voltage_label, 6, 0, 1, 1)

        self.sw_set_vc_horizontalLayout = QtWidgets.QHBoxLayout()

        self.sw_voltage_spinBox = QtWidgets.QDoubleSpinBox(self.setup_widget)
        self.sw_voltage_spinBox.setObjectName("sw_voltage_spinBox")
        self.sw_set_vc_horizontalLayout.addWidget(self.sw_voltage_spinBox)

        self.sw_current_spinBox = QtWidgets.QDoubleSpinBox(self.setup_widget)
        self.sw_current_spinBox.setObjectName("sw_current_spinBox")
        self.sw_set_vc_horizontalLayout.addWidget(self.sw_current_spinBox)

        self.sw_frequency_spinBox = QtWidgets.QDoubleSpinBox(self.setup_widget)
        self.sw_frequency_spinBox.setObjectName("sw_frequency_spinBox")
        self.sw_set_vc_horizontalLayout.addWidget(self.sw_frequency_spinBox)

        self.sw_capacitance_spinBox = QtWidgets.QDoubleSpinBox(self.setup_widget)
        self.sw_capacitance_spinBox.setObjectName("sw_capacitance_spinBox")
        self.sw_set_vc_horizontalLayout.addWidget(self.sw_capacitance_spinBox)

        self.sw_dc_current_spinBox = QtWidgets.QDoubleSpinBox(self.setup_widget)
        self.sw_dc_current_spinBox.setObjectName("sw_dc_current_spinBox")
        self.sw_set_vc_horizontalLayout.addWidget(self.sw_dc_current_spinBox)

        # self.sw_resistance_spinBox = QtWidgets.QDoubleSpinBox(self.setup_widget)
        # self.sw_resistance_spinBox.setObjectName("sw_resistance_spinBox")
        # self.sw_set_vc_horizontalLayout.addWidget(self.sw_resistance_spinBox)

        self.gridLayout_7.addLayout(self.sw_set_vc_horizontalLayout, 7, 0, 1, 2)

        # self.sw_set_buttons_gridLayout = QtWidgets.QGridLayout()

        self.sw_autoset_capacitance_HLayout = QtWidgets.QHBoxLayout()
        self.sw_autoset_capacitance_toggleSwitch = ToggleSwitch()
        self.sw_autoset_capacitance_label = QtWidgets.QLabel("Autoset Capacitance")
        self.sw_autoset_capacitance_HLayout.addWidget(
            self.sw_autoset_capacitance_toggleSwitch
        )
        self.sw_autoset_capacitance_HLayout.addWidget(self.sw_autoset_capacitance_label)
        self.gridLayout_7.addLayout(self.sw_autoset_capacitance_HLayout, 8, 0, 1, 1)

        self.sw_source_output_pushButton = QtWidgets.QPushButton(self.setup_widget)
        self.sw_source_output_pushButton.setObjectName("sw_source_output_pushButton")
        self.gridLayout_7.addWidget(self.sw_source_output_pushButton, 8, 1, 1, 1)

        self.tabWidget.addTab(self.setup_widget, "")

        # -------------------------------------------------------------------- #
        # ----------------------- Define Osci Widget-------------------------- #
        # -------------------------------------------------------------------- #
        self.osci_widget = QtWidgets.QWidget()
        self.osci_widget.setObjectName("osci_widget")
        self.osci_widget_gridLayout = QtWidgets.QGridLayout(self.osci_widget)
        self.osci_widget_gridLayout.setObjectName("osci_widget_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.ow_graph_widget = QtWidgets.QWidget(self.osci_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ow_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.ow_graph_widget.setSizePolicy(sizePolicy)
        self.ow_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.ow_graph_widget.setObjectName("ow_graph_widget")
        self.ow_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.ow_graph_widget)
        self.ow_mpl_graph_gridLayout.setObjectName("ow_mpl_graph_gridLayout")
        self.osci_widget_gridLayout.addWidget(self.ow_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.ow_fig = FigureCanvas(Figure(figsize=figureSize))
        self.ow_mpl_graph_gridLayout.addWidget(self.ow_fig)

        self.ow_ax = self.ow_fig.figure.subplots()
        # self.ow_ax.set_facecolor("#E0E0E0")
        self.ow_ax.grid(True)
        self.ow_ax.set_xlabel("Time ($\mu$s)", fontsize=14)
        self.ow_ax.set_ylabel("Voltage (V)", fontsize=14)
        self.ow_ax.set_xlim([50, 600])

        self.ow_ax.axhline(linewidth=1, color="black")
        self.ow_ax.axvline(linewidth=1, color="black")

        # self.ow_fig.figure.set_facecolor("#E0E0E0")
        self.ow_mplToolbar = NavigationToolbar(self.ow_fig, self.ow_graph_widget)
        self.ow_mplToolbar.setStyleSheet("background-color:white; color: black;")
        self.ow_mpl_graph_gridLayout.addWidget(self.ow_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.ow_scrollArea = QtWidgets.QScrollArea(self.osci_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ow_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.ow_scrollArea.setSizePolicy(sizePolicy)
        self.ow_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.ow_scrollArea.setWidgetResizable(True)
        self.ow_scrollArea.setObjectName("ow_scrollArea")
        self.ow_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.ow_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ow_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.ow_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.ow_scrollAreaWidgetContents.setObjectName("ow_scrollAreaWidgetContents")
        self.ow_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.ow_scrollAreaWidgetContents
        )
        self.ow_scrollArea_gridLayout.setObjectName("ow_scrollArea_gridLayout")

        self.ow_header1_label = QtWidgets.QLabel(self.ow_scrollAreaWidgetContents)
        self.ow_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ow_header1_label.setObjectName("ow_header1_label")
        self.ow_scrollArea_gridLayout.addWidget(self.ow_header1_label, 0, 0, 1, 1)
        self.ow_scrollArea.setWidget(self.ow_scrollAreaWidgetContents)
        self.osci_widget_gridLayout.addWidget(self.ow_scrollArea, 0, 3, 1, 1)

        # Auto Scale
        self.ow_auto_scale_pushButton = QtWidgets.QPushButton(
            self.ow_scrollAreaWidgetContents
        )
        self.ow_auto_scale_pushButton.setObjectName("ow_auto_scale_pushButton")
        self.ow_scrollArea_gridLayout.addWidget(
            self.ow_auto_scale_pushButton, 0, 0, 1, 1
        )

        # Stop
        self.ow_stop_pushButton = QtWidgets.QPushButton(
            self.ow_scrollAreaWidgetContents
        )
        self.ow_stop_pushButton.setObjectName("ow_stop_pushButton")
        self.ow_stop_pushButton.setCheckable(True)
        self.ow_scrollArea_gridLayout.addWidget(self.ow_stop_pushButton, 1, 0, 1, 1)

        # Save osci button
        self.ow_start_measurement_pushButton = QtWidgets.QPushButton(
            self.ow_scrollAreaWidgetContents
        )
        self.ow_start_measurement_pushButton.setObjectName(
            "ow_start_measurement_pushButton"
        )
        self.ow_scrollArea_gridLayout.addWidget(
            self.ow_start_measurement_pushButton, 2, 0, 1, 1
        )

        # Show Vmax for CHAN1
        self.ow_vmax_chan1_lcdNumber = QtWidgets.QLCDNumber(
            self.ow_scrollAreaWidgetContents
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ow_vmax_chan1_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.ow_vmax_chan1_lcdNumber.setSizePolicy(sizePolicy)
        self.ow_vmax_chan1_lcdNumber.setDigitCount(10)
        self.ow_vmax_chan1_lcdNumber.setAutoFillBackground(False)
        self.ow_vmax_chan1_lcdNumber.setSmallDecimalPoint(False)
        self.ow_vmax_chan1_lcdNumber.setObjectName("ow_vmax_chan1_lcdNumber")
        self.ow_scrollArea_gridLayout.addWidget(
            self.ow_vmax_chan1_lcdNumber, 3, 0, 1, 1
        )

        # Show Vmax for CHAN2
        self.ow_vmax_chan2_lcdNumber = QtWidgets.QLCDNumber(
            self.ow_scrollAreaWidgetContents
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ow_vmax_chan2_lcdNumber.sizePolicy().hasHeightForWidth()
        )
        self.ow_vmax_chan2_lcdNumber.setSizePolicy(sizePolicy)
        self.ow_vmax_chan2_lcdNumber.setDigitCount(10)
        self.ow_vmax_chan2_lcdNumber.setAutoFillBackground(False)
        self.ow_vmax_chan2_lcdNumber.setSmallDecimalPoint(False)
        self.ow_vmax_chan2_lcdNumber.setObjectName("ow_vmax_chan2_lcdNumber")
        self.ow_scrollArea_gridLayout.addWidget(
            self.ow_vmax_chan2_lcdNumber, 4, 0, 1, 1
        )

        self.tabWidget.addTab(self.osci_widget, "")

        # -------------------------------------------------------------------- #
        # ---------------------- Define Pulsing Widget ----------------------- #
        # -------------------------------------------------------------------- #
        self.pulsing_widget = QtWidgets.QWidget()
        self.pulsing_widget.setObjectName("pulsing_widget")
        self.pulsing_widget_gridLayout = QtWidgets.QGridLayout(self.pulsing_widget)
        self.pulsing_widget_gridLayout.setObjectName("pulsing_widget_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.pulsew_graph_widget = QtWidgets.QWidget(self.pulsing_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pulsew_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.pulsew_graph_widget.setSizePolicy(sizePolicy)
        self.pulsew_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.pulsew_graph_widget.setObjectName("pulsew_graph_widget")
        self.pulsew_mpl_graph_gridLayout = QtWidgets.QGridLayout(
            self.pulsew_graph_widget
        )
        self.pulsew_mpl_graph_gridLayout.setObjectName("pulsew_mpl_graph_gridLayout")
        self.pulsing_widget_gridLayout.addWidget(self.pulsew_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.pulsew_fig = FigureCanvas(Figure(figsize=figureSize))
        self.pulsew_mpl_graph_gridLayout.addWidget(self.pulsew_fig)

        self.pulsew_ax = self.pulsew_fig.figure.subplots()
        # self.pulsew_ax.set_facecolor("#E0E0E0")
        self.pulsew_ax.grid(True)
        self.pulsew_ax.set_xlabel("Time (s)", fontsize=14)
        self.pulsew_ax.set_ylabel("AC Magnetic Field (V)", fontsize=14)
        self.pulsew_ax.set_xlim([0, 300])
        self.pulsew_ax.set_xlim([0, 10])

        self.pulsew_ax.axhline(linewidth=1, color="black")
        self.pulsew_ax.axvline(linewidth=1, color="black")

        # self.pulsew_fig.figure.set_facecolor("#E0E0E0")
        self.pulsew_mplToolbar = NavigationToolbar(
            self.pulsew_fig, self.pulsew_graph_widget
        )
        self.pulsew_mplToolbar.setStyleSheet("background-color:white; color: black;")
        self.pulsew_mpl_graph_gridLayout.addWidget(self.pulsew_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.pulsew_scrollArea = QtWidgets.QScrollArea(self.pulsing_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pulsew_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.pulsew_scrollArea.setSizePolicy(sizePolicy)
        self.pulsew_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.pulsew_scrollArea.setWidgetResizable(True)
        self.pulsew_scrollArea.setObjectName("pulsew_scrollArea")
        self.pulsew_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.pulsew_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pulsew_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.pulsew_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.pulsew_scrollAreaWidgetContents.setObjectName(
            "pulsew_scrollAreaWidgetContents"
        )
        self.pulsew_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.pulsew_scrollAreaWidgetContents
        )
        self.pulsew_scrollArea_gridLayout.setObjectName("pulsew_scrollArea_gridLayout")

        self.pulsew_header1_label = QtWidgets.QLabel(
            self.pulsew_scrollAreaWidgetContents
        )
        self.pulsew_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.pulsew_header1_label.setObjectName("pulsew_header1_label")
        self.pulsew_scrollArea_gridLayout.addWidget(
            self.pulsew_header1_label, 0, 0, 1, 1
        )
        self.pulsew_scrollArea.setWidget(self.pulsew_scrollAreaWidgetContents)
        self.pulsing_widget_gridLayout.addWidget(self.pulsew_scrollArea, 0, 3, 1, 1)

        # Browse pulsing files
        self.pulsew_folder_path_label = QtWidgets.QLabel(self.setup_widget)
        self.pulsew_folder_path_label.setObjectName("pulsew_folder_path_label")
        self.pulsew_folder_path_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.pulsew_scrollArea_gridLayout.addWidget(
            self.pulsew_folder_path_label, 2, 0, 1, 1
        )

        self.pulsew_folder_path_horizontalLayout = QtWidgets.QHBoxLayout()
        self.pulsew_folder_path_horizontalLayout.setObjectName(
            "pulsew_folder_path_horizontalLayout"
        )
        self.pulsew_folder_path_lineEdit = QtWidgets.QLineEdit(self.setup_widget)
        self.pulsew_folder_path_lineEdit.setReadOnly(False)
        self.pulsew_folder_path_lineEdit.setObjectName("pulsew_folder_path_lineEdit")
        self.pulsew_folder_path_horizontalLayout.addWidget(
            self.pulsew_folder_path_lineEdit
        )
        self.pulsew_browse_pushButton = QtWidgets.QPushButton(self.setup_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pulsew_browse_pushButton.sizePolicy().hasHeightForWidth()
        )
        self.pulsew_browse_pushButton.setSizePolicy(sizePolicy)
        self.pulsew_browse_pushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.pulsew_browse_pushButton.setObjectName("pulsew_browse_pushButton")
        self.pulsew_folder_path_horizontalLayout.addWidget(
            self.pulsew_browse_pushButton
        )
        self.pulsew_scrollArea_gridLayout.addLayout(
            self.pulsew_folder_path_horizontalLayout, 3, 0, 1, 1
        )

        # Quick pulsing with predefined values
        self.pulsew_constant_parameter_mode_HLayout = QtWidgets.QHBoxLayout()
        self.pulsew_constant_parameter_mode_toggleSwitch = ToggleSwitch()
        self.pulsew_constant_parameter_mode_label = QtWidgets.QLabel("Constant Mode")
        self.pulsew_constant_parameter_mode_HLayout.addWidget(
            self.pulsew_constant_parameter_mode_toggleSwitch
        )
        self.pulsew_constant_parameter_mode_HLayout.addWidget(
            self.pulsew_constant_parameter_mode_label
        )
        self.pulsew_scrollArea_gridLayout.addLayout(
            self.pulsew_constant_parameter_mode_HLayout, 4, 0, 1, 1
        )

        # Start measurement push button
        self.pulsew_start_measurement_pushButton = QtWidgets.QPushButton(
            self.pulsew_scrollAreaWidgetContents
        )
        self.pulsew_start_measurement_pushButton.setObjectName(
            "pulsew_start_measurement_pushButton"
        )
        self.pulsew_scrollArea_gridLayout.addWidget(
            self.pulsew_start_measurement_pushButton, 5, 0, 1, 1
        )

        self.tabWidget.addTab(self.pulsing_widget, "")

        # -------------------------------------------------------------------- #
        # --------------------------- Spacer Tab ----------------------------- #
        # -------------------------------------------------------------------- #
        self.spacer = QtWidgets.QWidget()
        self.tabWidget.addTab(self.spacer, "")
        self.tabWidget.setTabEnabled(self.tabWidget.indexOf(self.spacer), False)

        # -------------------------------------------------------------------- #
        # ---------------------- Define Spectrum Widget ---------------------- #
        # -------------------------------------------------------------------- #
        self.spectrum_widget = QtWidgets.QWidget()
        self.spectrum_widget.setObjectName("spectrum_widget")
        self.spectrum_widget_gridLayout = QtWidgets.QGridLayout(self.spectrum_widget)
        self.spectrum_widget_gridLayout.setObjectName("spectrum_widget_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.specw_graph_widget = QtWidgets.QWidget(self.spectrum_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.specw_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.specw_graph_widget.setSizePolicy(sizePolicy)
        self.specw_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.specw_graph_widget.setObjectName("specw_graph_widget")
        self.specw_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.specw_graph_widget)
        self.specw_mpl_graph_gridLayout.setObjectName("specw_mpl_graph_gridLayout")
        self.spectrum_widget_gridLayout.addWidget(self.specw_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.specw_fig = FigureCanvas(Figure(figsize=figureSize))
        self.specw_mpl_graph_gridLayout.addWidget(self.specw_fig)

        self.specw_ax = self.specw_fig.figure.subplots()
        # self.specw_ax.set_facecolor("#E0E0E0")
        self.specw_ax.grid(True)
        self.specw_ax.set_xlabel("Frequency (kHz)", fontsize=14)
        self.specw_ax.set_ylabel("V$_{max,ME}$ (V)", fontsize=14)
        self.specw_ax.set_xlim([50, 600])

        self.specw_ax.axhline(linewidth=1, color="black")
        self.specw_ax.axvline(linewidth=1, color="black")

        self.specw_ax2 = self.specw_ax.twinx()
        self.specw_ax2.set_ylabel(
            "AC Magnetic Field/Current (mT/A)",
            fontsize=14,
            color=(85 / 255, 170 / 255, 255 / 255),
        )

        # self.specw_fig.figure.set_facecolor("#E0E0E0")
        self.specw_mplToolbar = NavigationToolbar(
            self.specw_fig, self.specw_graph_widget
        )
        self.specw_mplToolbar.setStyleSheet("background-color:white; color: black;")
        self.specw_mpl_graph_gridLayout.addWidget(self.specw_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.specw_scrollArea = QtWidgets.QScrollArea(self.spectrum_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.specw_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.specw_scrollArea.setSizePolicy(sizePolicy)
        self.specw_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.specw_scrollArea.setWidgetResizable(True)
        self.specw_scrollArea.setObjectName("specw_scrollArea")
        self.specw_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.specw_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.specw_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.specw_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.specw_scrollAreaWidgetContents.setObjectName(
            "specw_scrollAreaWidgetContents"
        )
        self.specw_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_scrollArea_gridLayout.setObjectName("specw_scrollArea_gridLayout")

        self.specw_header1_label = QtWidgets.QLabel(self.specw_scrollAreaWidgetContents)
        self.specw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.specw_header1_label.setObjectName("specw_header1_label")
        self.specw_scrollArea_gridLayout.addWidget(self.specw_header1_label, 0, 0, 1, 1)
        self.specw_scrollArea.setWidget(self.specw_scrollAreaWidgetContents)
        self.spectrum_widget_gridLayout.addWidget(self.specw_scrollArea, 0, 3, 1, 1)

        # Set voltage
        self.specw_voltage_label = QtWidgets.QLabel(self.specw_scrollAreaWidgetContents)
        self.specw_voltage_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.specw_voltage_label.setObjectName("specw_voltage_label")
        self.specw_scrollArea_gridLayout.addWidget(self.specw_voltage_label, 1, 0, 1, 1)
        self.specw_voltage_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_voltage_spinBox.setObjectName("specw_voltage_spinBox")
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_voltage_spinBox, 2, 0, 1, 1
        )

        # Constant magnetic field mode?
        self.specw_constant_magnetic_field_mode_HLayout = QtWidgets.QHBoxLayout()
        self.specw_constant_magnetic_field_mode_toggleSwitch = ToggleSwitch()
        self.specw_constant_magnetic_field_mode_label = QtWidgets.QLabel(
            "Magnetic Field Mode"
        )
        self.specw_constant_magnetic_field_mode_HLayout.addWidget(
            self.specw_constant_magnetic_field_mode_toggleSwitch
        )
        self.specw_constant_magnetic_field_mode_HLayout.addWidget(
            self.specw_constant_magnetic_field_mode_label
        )
        self.specw_scrollArea_gridLayout.addLayout(
            self.specw_constant_magnetic_field_mode_HLayout, 3, 0, 1, 1
        )

        # Set current/magnetic field limit
        self.specw_current_label = QtWidgets.QLabel(self.specw_scrollAreaWidgetContents)
        self.specw_current_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.specw_current_label.setObjectName("specw_current_label")
        self.specw_scrollArea_gridLayout.addWidget(self.specw_current_label, 4, 0, 1, 1)
        self.specw_current_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_current_spinBox.setObjectName("specw_current_spinBox")
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_current_spinBox, 5, 0, 1, 1
        )

        # Set dc magnetic field
        self.specw_dc_magnetic_field_label = QtWidgets.QLabel(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_dc_magnetic_field_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.specw_dc_magnetic_field_label.setObjectName(
            "specw_dc_magnetic_field_label"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_dc_magnetic_field_label, 6, 0, 1, 1
        )
        self.specw_dc_magnetic_field_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_dc_magnetic_field_spinBox.setObjectName(
            "specw_dc_magnetic_field_spinBox"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_dc_magnetic_field_spinBox, 7, 0, 1, 1
        )

        # Set minimum scan frequency
        self.specw_minimum_frequency_label = QtWidgets.QLabel(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_minimum_frequency_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.specw_minimum_frequency_label.setObjectName(
            "specw_minimum_frequency_label"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_minimum_frequency_label, 8, 0, 1, 1
        )
        self.specw_minimum_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_minimum_frequency_spinBox.setObjectName(
            "specw_minimum_frequency_spinBox"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_minimum_frequency_spinBox, 9, 0, 1, 1
        )

        # Set maximum scan frequency
        self.specw_maximum_frequency_label = QtWidgets.QLabel(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_maximum_frequency_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.specw_maximum_frequency_label.setObjectName(
            "specw_maximum_frequency_label"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_maximum_frequency_label, 10, 0, 1, 1
        )
        self.specw_maximum_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_maximum_frequency_spinBox.setObjectName(
            "specw_maximum_frequency_spinBox"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_maximum_frequency_spinBox, 11, 0, 1, 1
        )

        # Auto set step size?
        self.specw_autoset_frequency_step_HLayout = QtWidgets.QHBoxLayout()
        self.specw_autoset_frequency_step_toggleSwitch = ToggleSwitch()
        self.specw_autoset_frequency_step_label = QtWidgets.QLabel(
            "Auto Frequency Step"
        )
        self.specw_autoset_frequency_step_HLayout.addWidget(
            self.specw_autoset_frequency_step_toggleSwitch
        )
        self.specw_autoset_frequency_step_HLayout.addWidget(
            self.specw_autoset_frequency_step_label
        )
        self.specw_scrollArea_gridLayout.addLayout(
            self.specw_autoset_frequency_step_HLayout, 12, 0, 1, 1
        )

        # Set frequency step
        self.specw_frequency_step_label = QtWidgets.QLabel(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_frequency_step_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.specw_frequency_step_label.setObjectName("specw_frequency_step_label")
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_frequency_step_label, 13, 0, 1, 1
        )
        self.specw_frequency_step_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_frequency_step_spinBox.setObjectName("specw_frequency_step_spinBox")
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_frequency_step_spinBox, 14, 0, 1, 1
        )

        # Set frequency settling time
        self.specw_frequency_settling_time_label = QtWidgets.QLabel(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_frequency_settling_time_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.specw_frequency_settling_time_label.setObjectName(
            "specw_frequency_settling_time_label"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_frequency_settling_time_label, 15, 0, 1, 1
        )
        self.specw_frequency_settling_time_spinBox = QtWidgets.QDoubleSpinBox(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_frequency_settling_time_spinBox.setObjectName(
            "specw_frequency_settling_time_spinBox"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_frequency_settling_time_spinBox, 16, 0, 1, 1
        )

        # Auto set capacitance?
        self.specw_autoset_capacitance_HLayout = QtWidgets.QHBoxLayout()
        self.specw_autoset_capacitance_toggleSwitch = ToggleSwitch()
        self.specw_autoset_capacitance_label = QtWidgets.QLabel("Autoset Capacitance")
        self.specw_autoset_capacitance_HLayout.addWidget(
            self.specw_autoset_capacitance_toggleSwitch
        )
        self.specw_autoset_capacitance_HLayout.addWidget(
            self.specw_autoset_capacitance_label
        )
        self.specw_scrollArea_gridLayout.addLayout(
            self.specw_autoset_capacitance_HLayout, 17, 0, 1, 1
        )

        # Start measurement push button
        self.specw_start_measurement_pushButton = QtWidgets.QPushButton(
            self.specw_scrollAreaWidgetContents
        )
        self.specw_start_measurement_pushButton.setObjectName(
            "specw_start_measurement_pushButton"
        )
        self.specw_scrollArea_gridLayout.addWidget(
            self.specw_start_measurement_pushButton, 18, 0, 1, 1
        )

        self.tabWidget.addTab(self.spectrum_widget, "")

        # -------------------------------------------------------------------- #
        # ------------- Define Bias Field Measurement Widget ----------------- #
        # -------------------------------------------------------------------- #

        self.bias_field_widget = QtWidgets.QWidget()
        self.bias_field_widget.setObjectName("bias_field_widget")
        self.bias_field_widget_gridLayout = QtWidgets.QGridLayout(
            self.bias_field_widget
        )
        self.bias_field_widget_gridLayout.setObjectName("bias_field_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.bw_graph_widget = QtWidgets.QWidget(self.bias_field_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bw_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.bw_graph_widget.setSizePolicy(sizePolicy)
        self.bw_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.bw_graph_widget.setObjectName("bw_graph_widget")
        self.bw_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.bw_graph_widget)
        self.bw_mpl_graph_gridLayout.setObjectName("bw_mpl_graph_gridLayout")
        self.bias_field_widget_gridLayout.addWidget(self.bw_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.bw_fig = FigureCanvas(Figure(figsize=figureSize))
        self.bw_mpl_graph_gridLayout.addWidget(self.bw_fig)

        self.bw_ax = self.bw_fig.figure.subplots()
        self.bw_ax.grid(True)
        self.bw_ax.set_xlabel("Bias Field (mT)", fontsize=14)
        self.bw_ax.set_ylabel("V$_{max,ME}$ (V)", fontsize=14)
        self.bw_ax.set_xlim([50, 600])

        self.bw_ax.axhline(linewidth=1, color="black")
        self.bw_ax.axvline(linewidth=1, color="black")

        self.bw_ax2 = self.bw_ax.twinx()
        self.bw_ax2.set_ylabel(
            "AC Magnetic Field (mT)",
            fontsize=14,
            color=(85 / 255, 170 / 255, 255 / 255),
        )

        # self.bw_fig.figure.set_facecolor("#E0E0E0")
        self.bw_mplToolbar = NavigationToolbar(self.bw_fig, self.bw_graph_widget)
        self.bw_mplToolbar.setStyleSheet("background-color:white; color: black;")
        self.bw_mpl_graph_gridLayout.addWidget(self.bw_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.bw_scrollArea = QtWidgets.QScrollArea(self.bias_field_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bw_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.bw_scrollArea.setSizePolicy(sizePolicy)
        self.bw_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.bw_scrollArea.setWidgetResizable(True)
        self.bw_scrollArea.setObjectName("bw_scrollArea")
        self.bw_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.bw_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bw_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.bw_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.bw_scrollAreaWidgetContents.setObjectName("bw_scrollAreaWidgetContents")
        self.bw_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_scrollArea_gridLayout.setObjectName("bw_scrollArea_gridLayout")

        self.bw_header1_label = QtWidgets.QLabel(self.bw_scrollAreaWidgetContents)
        self.bw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.bw_header1_label.setObjectName("bw_header1_label")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_header1_label, 0, 0, 1, 1)
        self.bw_scrollArea.setWidget(self.bw_scrollAreaWidgetContents)
        self.bias_field_widget_gridLayout.addWidget(self.bw_scrollArea, 0, 3, 1, 1)

        # Set voltage
        self.bw_voltage_label = QtWidgets.QLabel(self.bw_scrollAreaWidgetContents)
        self.bw_voltage_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.bw_voltage_label.setObjectName("bw_voltage_label")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_voltage_label, 1, 0, 1, 1)
        self.bw_voltage_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_voltage_spinBox.setObjectName("bw_voltage_spinBox")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_voltage_spinBox, 2, 0, 1, 1)

        # Constant magnetic field mode?
        self.bw_constant_magnetic_field_mode_HLayout = QtWidgets.QHBoxLayout()
        self.bw_constant_magnetic_field_mode_toggleSwitch = ToggleSwitch()
        self.bw_constant_magnetic_field_mode_label = QtWidgets.QLabel(
            "Magnetic Field Mode"
        )
        self.bw_constant_magnetic_field_mode_HLayout.addWidget(
            self.bw_constant_magnetic_field_mode_toggleSwitch
        )
        self.bw_constant_magnetic_field_mode_HLayout.addWidget(
            self.bw_constant_magnetic_field_mode_label
        )
        self.bw_scrollArea_gridLayout.addLayout(
            self.bw_constant_magnetic_field_mode_HLayout, 3, 0, 1, 1
        )

        # Set current limit
        self.bw_current_label = QtWidgets.QLabel(self.bw_scrollAreaWidgetContents)
        self.bw_current_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.bw_current_label.setObjectName("bw_current_label")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_current_label, 4, 0, 1, 1)
        self.bw_current_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_current_spinBox.setObjectName("bw_current_spinBox")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_current_spinBox, 5, 0, 1, 1)

        # Set frequency
        self.bw_frequency_label = QtWidgets.QLabel(self.bw_scrollAreaWidgetContents)
        self.bw_frequency_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.bw_frequency_label.setObjectName("bw_frequency_label")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_frequency_label, 8, 0, 1, 1)
        self.bw_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_frequency_spinBox.setObjectName("bw_frequency_spinBox")
        self.bw_scrollArea_gridLayout.addWidget(self.bw_frequency_spinBox, 9, 0, 1, 1)

        # Set minimum scan dc magnetic field
        self.bw_minimum_dc_magnetic_field_label = QtWidgets.QLabel(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_minimum_dc_magnetic_field_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.bw_minimum_dc_magnetic_field_label.setObjectName(
            "bw_minimum_dc_magnetic_field_label"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_minimum_dc_magnetic_field_label, 10, 0, 1, 1
        )
        self.bw_minimum_dc_magnetic_field_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_minimum_dc_magnetic_field_spinBox.setObjectName(
            "bw_minimum_dc_magnetic_field_spinBox"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_minimum_dc_magnetic_field_spinBox, 11, 0, 1, 1
        )

        # Set maximum scan frequency
        self.bw_maximum_dc_magnetic_field_label = QtWidgets.QLabel(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_maximum_dc_magnetic_field_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.bw_maximum_dc_magnetic_field_label.setObjectName(
            "bw_maximum_dc_magnetic_field_label"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_maximum_dc_magnetic_field_label, 12, 0, 1, 1
        )
        self.bw_maximum_dc_magnetic_field_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_maximum_dc_magnetic_field_spinBox.setObjectName(
            "bw_maximum_dc_magnetic_field_spinBox"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_maximum_dc_magnetic_field_spinBox, 13, 0, 1, 1
        )

        # Set frequency step
        self.bw_dc_magnetic_field_step_label = QtWidgets.QLabel(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_dc_magnetic_field_step_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.bw_dc_magnetic_field_step_label.setObjectName(
            "bw_dc_magnetic_field_step_label"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_dc_magnetic_field_step_label, 14, 0, 1, 1
        )
        self.bw_dc_magnetic_field_step_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_dc_magnetic_field_step_spinBox.setObjectName(
            "bw_dc_magnetic_field_step_spinBox"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_dc_magnetic_field_step_spinBox, 15, 0, 1, 1
        )

        # Set bias settling time
        self.bw_dc_magnetic_field_settling_time_label = QtWidgets.QLabel(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_dc_magnetic_field_settling_time_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.bw_dc_magnetic_field_settling_time_label.setObjectName(
            "bw_dc_magnetic_field_settling_time_label"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_dc_magnetic_field_settling_time_label, 16, 0, 1, 1
        )
        self.bw_dc_magnetic_field_settling_time_spinBox = QtWidgets.QDoubleSpinBox(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_dc_magnetic_field_settling_time_spinBox.setObjectName(
            "bw_dc_magnetic_field_settling_time_spinBox"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_dc_magnetic_field_settling_time_spinBox, 17, 0, 1, 1
        )

        # Auto set capacitance?
        self.bw_autoset_capacitance_HLayout = QtWidgets.QHBoxLayout()
        self.bw_autoset_capacitance_toggleSwitch = ToggleSwitch()
        self.bw_autoset_capacitance_label = QtWidgets.QLabel("Autoset Capacitance")
        self.bw_autoset_capacitance_HLayout.addWidget(
            self.bw_autoset_capacitance_toggleSwitch
        )
        self.bw_autoset_capacitance_HLayout.addWidget(self.bw_autoset_capacitance_label)
        self.bw_scrollArea_gridLayout.addLayout(
            self.bw_autoset_capacitance_HLayout, 18, 0, 1, 1
        )

        # Include reverse sweep?
        self.bw_reverse_sweep_HLayout = QtWidgets.QHBoxLayout()
        self.bw_reverse_sweep_toggleSwitch = ToggleSwitch()
        self.bw_reverse_sweep_label = QtWidgets.QLabel("Reverse Sweep")
        self.bw_reverse_sweep_HLayout.addWidget(self.bw_reverse_sweep_toggleSwitch)
        self.bw_reverse_sweep_HLayout.addWidget(self.bw_reverse_sweep_label)
        self.bw_scrollArea_gridLayout.addLayout(
            self.bw_reverse_sweep_HLayout, 19, 0, 1, 1
        )

        # Save Power button
        self.bw_start_measurement_pushButton = QtWidgets.QPushButton(
            self.bw_scrollAreaWidgetContents
        )
        self.bw_start_measurement_pushButton.setObjectName(
            "bw_start_measurement_pushButton"
        )
        self.bw_scrollArea_gridLayout.addWidget(
            self.bw_start_measurement_pushButton, 20, 0, 1, 1
        )

        self.tabWidget.addTab(self.bias_field_widget, "")

        # -------------------------------------------------------------------- #
        # ----------------- Define AC Field Scan Widget ---------------------- #
        # -------------------------------------------------------------------- #
        self.hf_field_widget = QtWidgets.QWidget()
        self.hf_field_widget.setObjectName("hf_field_widget")
        self.hf_field_widget_gridLayout = QtWidgets.QGridLayout(self.hf_field_widget)
        self.hf_field_widget_gridLayout.setObjectName("hf_field_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.hfw_graph_widget = QtWidgets.QWidget(self.hf_field_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hfw_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.hfw_graph_widget.setSizePolicy(sizePolicy)
        self.hfw_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.hfw_graph_widget.setObjectName("hfw_graph_widget")
        self.hfw_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.hfw_graph_widget)
        self.hfw_mpl_graph_gridLayout.setObjectName("hfw_mpl_graph_gridLayout")
        self.hf_field_widget_gridLayout.addWidget(self.hfw_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.hfw_fig = FigureCanvas(Figure(figsize=figureSize))
        self.hfw_mpl_graph_gridLayout.addWidget(self.hfw_fig)

        self.hfw_ax = self.hfw_fig.figure.subplots()
        # self.hfw_ax.set_facecolor("#E0E0E0")
        self.hfw_ax.grid(True)
        self.hfw_ax.set_xlabel("AC Field Voltage (V)", fontsize=14)
        self.hfw_ax.set_ylabel("Max ME Response (V)", fontsize=14)
        self.hfw_ax.set_xlim([50, 600])

        self.hfw_ax.axhline(linewidth=1, color="black")
        self.hfw_ax.axvline(linewidth=1, color="black")

        # self.hfw_ax2 = self.hfw_ax.twinx()
        # self.hfw_ax2.set_ylabel(
        #     "HF Magnetic Field (mT)",
        #     color=(85 / 255, 170 / 255, 255 / 255),
        #     fontsize=14,
        # )
        # self.hfw_ax2.yaxis.label.set_color((43 / 255, 50 / 255, 61 / 255))

        # self.hfw_fig.figure.set_facecolor("#E0E0E0")
        self.hfw_mplToolbar = NavigationToolbar(self.hfw_fig, self.hfw_graph_widget)
        self.hfw_mplToolbar.setStyleSheet("background-color:white; color: black;")
        self.hfw_mpl_graph_gridLayout.addWidget(self.hfw_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.hfw_scrollArea = QtWidgets.QScrollArea(self.hf_field_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hfw_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.hfw_scrollArea.setSizePolicy(sizePolicy)
        self.hfw_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.hfw_scrollArea.setWidgetResizable(True)
        self.hfw_scrollArea.setObjectName("hfw_scrollArea")
        self.hfw_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.hfw_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hfw_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.hfw_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.hfw_scrollAreaWidgetContents.setObjectName("hfw_scrollAreaWidgetContents")
        self.hfw_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_scrollArea_gridLayout.setObjectName("hfw_scrollArea_gridLayout")

        self.hfw_header1_label = QtWidgets.QLabel(self.hfw_scrollAreaWidgetContents)
        self.hfw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.hfw_header1_label.setObjectName("hfw_header1_label")
        self.hfw_scrollArea_gridLayout.addWidget(self.hfw_header1_label, 0, 0, 1, 1)
        self.hfw_scrollArea.setWidget(self.hfw_scrollAreaWidgetContents)
        self.hf_field_widget_gridLayout.addWidget(self.hfw_scrollArea, 0, 3, 1, 1)

        self.hfw_voltage_compliance_label = QtWidgets.QLabel(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_voltage_compliance_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.hfw_voltage_compliance_label.setObjectName("hfw_voltage_compliance_label")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_voltage_compliance_label, 1, 0, 1, 1
        )
        self.hfw_voltage_compliance_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_voltage_compliance_spinBox.setObjectName(
            "hfw_voltage_compliance_spinBox"
        )
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_voltage_compliance_spinBox, 2, 0, 1, 1
        )

        # Constant magnetic field mode?
        self.hfw_constant_magnetic_field_mode_HLayout = QtWidgets.QHBoxLayout()
        self.hfw_constant_magnetic_field_mode_toggleSwitch = ToggleSwitch()
        self.hfw_constant_magnetic_field_mode_label = QtWidgets.QLabel(
            "Magnetic Field Mode"
        )
        self.hfw_constant_magnetic_field_mode_HLayout.addWidget(
            self.hfw_constant_magnetic_field_mode_toggleSwitch
        )
        self.hfw_constant_magnetic_field_mode_HLayout.addWidget(
            self.hfw_constant_magnetic_field_mode_label
        )
        self.hfw_scrollArea_gridLayout.addLayout(
            self.hfw_constant_magnetic_field_mode_HLayout, 3, 0, 1, 1
        )

        # Set DC magnetic field
        self.hfw_dc_magnetic_field_label = QtWidgets.QLabel(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_dc_magnetic_field_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.hfw_dc_magnetic_field_label.setObjectName("hfw_dc_magnetic_field_label")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_dc_magnetic_field_label, 6, 0, 1, 1
        )
        self.hfw_dc_magnetic_field_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_dc_magnetic_field_spinBox.setObjectName(
            "hfw_dc_magnetic_field_spinBox"
        )
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_dc_magnetic_field_spinBox, 7, 0, 1, 1
        )

        # Set frequency
        self.hfw_frequency_label = QtWidgets.QLabel(self.hfw_scrollAreaWidgetContents)
        self.hfw_frequency_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.hfw_frequency_label.setObjectName("hfw_frequency_label")
        self.hfw_scrollArea_gridLayout.addWidget(self.hfw_frequency_label, 8, 0, 1, 1)
        self.hfw_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_frequency_spinBox.setObjectName("hfw_frequency_spinBox")
        self.hfw_scrollArea_gridLayout.addWidget(self.hfw_frequency_spinBox, 9, 0, 1, 1)

        # Set minimum scan voltage 
        self.hfw_minimum_voltage_label = QtWidgets.QLabel(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_minimum_voltage_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.hfw_minimum_voltage_label.setObjectName("hfw_minimum_voltage_label")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_minimum_voltage_label, 10, 0, 1, 1
        )
        self.hfw_minimum_voltage_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_minimum_voltage_spinBox.setObjectName("hfw_minimum_voltage_spinBox")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_minimum_voltage_spinBox, 11, 0, 1, 1
        )

        # Set maximum scan frequency
        self.hfw_maximum_voltage_label = QtWidgets.QLabel(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_maximum_voltage_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.hfw_maximum_voltage_label.setObjectName("hfw_maximum_voltage_label")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_maximum_voltage_label, 12, 0, 1, 1
        )
        self.hfw_maximum_voltage_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_maximum_voltage_spinBox.setObjectName("hfw_maximum_voltage_spinBox")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_maximum_voltage_spinBox, 13, 0, 1, 1
        )

        # Set frequency step
        self.hfw_voltage_step_label = QtWidgets.QLabel(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_voltage_step_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.hfw_voltage_step_label.setObjectName("hfw_voltage_step_label")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_voltage_step_label, 14, 0, 1, 1
        )
        self.hfw_voltage_step_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_voltage_step_spinBox.setObjectName("hfw_voltage_step_spinBox")
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_voltage_step_spinBox, 15, 0, 1, 1
        )

        # Set current settling time
        self.hfw_voltage_settling_time_label = QtWidgets.QLabel(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_voltage_settling_time_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.hfw_voltage_settling_time_label.setObjectName(
            "hfw_voltage_settling_time_label"
        )
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_voltage_settling_time_label, 16, 0, 1, 1
        )
        self.hfw_voltage_settling_time_spinBox = QtWidgets.QDoubleSpinBox(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_voltage_settling_time_spinBox.setObjectName(
            "hfw_voltage_settling_time_spinBox"
        )
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_voltage_settling_time_spinBox, 17, 0, 1, 1
        )

        # Auto set capacitance?
        self.hfw_autoset_capacitance_HLayout = QtWidgets.QHBoxLayout()
        self.hfw_autoset_capacitance_toggleSwitch = ToggleSwitch()
        self.hfw_autoset_capacitance_label = QtWidgets.QLabel("Autoset Capacitance")
        self.hfw_autoset_capacitance_HLayout.addWidget(
            self.hfw_autoset_capacitance_toggleSwitch
        )
        self.hfw_autoset_capacitance_HLayout.addWidget(
            self.hfw_autoset_capacitance_label
        )
        self.hfw_scrollArea_gridLayout.addLayout(
            self.hfw_autoset_capacitance_HLayout, 18, 0, 1, 1
        )

        # Save Power button
        self.hfw_start_measurement_pushButton = QtWidgets.QPushButton(
            self.hfw_scrollAreaWidgetContents
        )
        self.hfw_start_measurement_pushButton.setObjectName(
            "hfw_start_measurement_pushButton"
        )
        self.hfw_scrollArea_gridLayout.addWidget(
            self.hfw_start_measurement_pushButton, 19, 0, 1, 1
        )

        self.tabWidget.addTab(self.hf_field_widget, "")

        # -------------------------------------------------------------------- #
        # ----------------- Define Lifetime Field Scan Widget ---------------------- #
        # -------------------------------------------------------------------- #
        self.ltw_widget = QtWidgets.QWidget()
        self.ltw_widget.setObjectName("ltw_widget")
        self.ltw_field_widget_gridLayout = QtWidgets.QGridLayout(self.ltw_widget)
        self.ltw_field_widget_gridLayout.setObjectName("ltw_field_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.ltw_graph_widget = QtWidgets.QWidget(self.ltw_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ltw_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.ltw_graph_widget.setSizePolicy(sizePolicy)
        self.ltw_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.ltw_graph_widget.setObjectName("ltw_graph_widget")
        self.ltw_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.ltw_graph_widget)
        self.ltw_mpl_graph_gridLayout.setObjectName("ltw_mpl_graph_gridLayout")
        self.ltw_field_widget_gridLayout.addWidget(self.ltw_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.ltw_fig = FigureCanvas(Figure(figsize=figureSize))
        self.ltw_mpl_graph_gridLayout.addWidget(self.ltw_fig)

        self.ltw_ax = self.ltw_fig.figure.subplots()
        # self.ltw_ax.set_facecolor("#E0E0E0")
        self.ltw_ax.grid(True)
        self.ltw_ax.set_xlabel("Time (s)", fontsize=14)
        self.ltw_ax.set_ylabel("Max. ME Voltage (V)", fontsize=14)
        self.ltw_ax.set_xlim([50, 600])

        self.ltw_ax.axhline(linewidth=1, color="black")
        self.ltw_ax.axvline(linewidth=1, color="black")

        self.ltw_ax2 = self.ltw_ax.twinx()
        self.ltw_ax2.set_ylabel(
            "Magnetic Field (mT)",
            fontsize=14,
            color=(85 / 255, 170 / 255, 255 / 255),
        )
        # self.ltw_ax2.yaxis.label.set_color((85 / 255, 170 / 255, 255 / 255))

        # self.ltw_ax2 = self.ltw_ax.twinx()
        # self.ltw_ax2.set_ylabel(
        #     "HF Magnetic Field (mT)",
        #     color=(85 / 255, 170 / 255, 255 / 255),
        #     fontsize=14,
        # )
        # self.ltw_ax2.yaxis.label.set_color((43 / 255, 50 / 255, 61 / 255))

        # self.ltw_fig.figure.set_facecolor("#E0E0E0")
        self.ltw_mplToolbar = NavigationToolbar(self.ltw_fig, self.ltw_graph_widget)
        self.ltw_mplToolbar.setStyleSheet("background-color:white; color: black;")
        self.ltw_mpl_graph_gridLayout.addWidget(self.ltw_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.ltw_scrollArea = QtWidgets.QScrollArea(self.ltw_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ltw_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.ltw_scrollArea.setSizePolicy(sizePolicy)
        self.ltw_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.ltw_scrollArea.setWidgetResizable(True)
        self.ltw_scrollArea.setObjectName("ltw_scrollArea")
        self.ltw_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.ltw_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ltw_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.ltw_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.ltw_scrollAreaWidgetContents.setObjectName("ltw_scrollAreaWidgetContents")
        self.ltw_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_scrollArea_gridLayout.setObjectName("ltw_scrollArea_gridLayout")

        self.ltw_header1_label = QtWidgets.QLabel(self.ltw_scrollAreaWidgetContents)
        self.ltw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ltw_header1_label.setObjectName("ltw_header1_label")
        self.ltw_scrollArea_gridLayout.addWidget(self.ltw_header1_label, 0, 0, 1, 1)
        self.ltw_scrollArea.setWidget(self.ltw_scrollAreaWidgetContents)
        self.ltw_field_widget_gridLayout.addWidget(self.ltw_scrollArea, 0, 3, 1, 1)

        self.ltw_voltage_compliance_label = QtWidgets.QLabel(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_voltage_compliance_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.ltw_voltage_compliance_label.setObjectName("ltw_voltage_compliance_label")
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_voltage_compliance_label, 1, 0, 1, 1
        )
        self.ltw_voltage_compliance_spinBox = QtWidgets.QDoubleSpinBox(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_voltage_compliance_spinBox.setObjectName(
            "ltw_voltage_compliance_spinBox"
        )
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_voltage_compliance_spinBox, 2, 0, 1, 1
        )

        # Constant magnetic field mode?
        self.ltw_constant_magnetic_field_mode_HLayout = QtWidgets.QHBoxLayout()
        self.ltw_constant_magnetic_field_mode_toggleSwitch = ToggleSwitch()
        self.ltw_constant_magnetic_field_mode_label = QtWidgets.QLabel(
            "Magnetic Field Mode"
        )
        self.ltw_constant_magnetic_field_mode_HLayout.addWidget(
            self.ltw_constant_magnetic_field_mode_toggleSwitch
        )
        self.ltw_constant_magnetic_field_mode_HLayout.addWidget(
            self.ltw_constant_magnetic_field_mode_label
        )
        self.ltw_scrollArea_gridLayout.addLayout(
            self.ltw_constant_magnetic_field_mode_HLayout, 3, 0, 1, 1
        )

        # Set DC magnetic field
        self.ltw_dc_magnetic_field_label = QtWidgets.QLabel(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_dc_magnetic_field_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ltw_dc_magnetic_field_label.setObjectName("ltw_dc_magnetic_field_label")
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_dc_magnetic_field_label, 6, 0, 1, 1
        )
        self.ltw_dc_magnetic_field_spinBox = QtWidgets.QDoubleSpinBox(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_dc_magnetic_field_spinBox.setObjectName(
            "ltw_dc_magnetic_field_spinBox"
        )
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_dc_magnetic_field_spinBox, 7, 0, 1, 1
        )

        # Set frequency
        self.ltw_frequency_label = QtWidgets.QLabel(self.ltw_scrollAreaWidgetContents)
        self.ltw_frequency_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ltw_frequency_label.setObjectName("ltw_frequency_label")
        self.ltw_scrollArea_gridLayout.addWidget(self.ltw_frequency_label, 8, 0, 1, 1)
        self.ltw_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_frequency_spinBox.setObjectName("ltw_frequency_spinBox")
        self.ltw_scrollArea_gridLayout.addWidget(self.ltw_frequency_spinBox, 9, 0, 1, 1)

        # Set HF Field
        self.ltw_hf_magnetic_field_label = QtWidgets.QLabel(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_hf_magnetic_field_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ltw_hf_magnetic_field_label.setObjectName("ltw_hf_magnetic_field_label")
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_hf_magnetic_field_label, 10, 0, 1, 1
        )
        self.ltw_hf_magnetic_field_spinBox = QtWidgets.QDoubleSpinBox(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_hf_magnetic_field_spinBox.setObjectName(
            "ltw_hf_magnetic_field_spinBox"
        )
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_hf_magnetic_field_spinBox, 11, 0, 1, 1
        )

        # Set measurement time
        self.ltw_total_time_label = QtWidgets.QLabel(self.ltw_scrollAreaWidgetContents)
        self.ltw_total_time_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ltw_total_time_label.setObjectName("ltw_maximum_voltage_label")
        self.ltw_scrollArea_gridLayout.addWidget(self.ltw_total_time_label, 12, 0, 1, 1)
        self.ltw_total_time_spinBox = QtWidgets.QDoubleSpinBox(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_total_time_spinBox.setObjectName("ltw_total_time_spinBox")
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_total_time_spinBox, 13, 0, 1, 1
        )

        # Set measurement time step
        self.ltw_time_step_label = QtWidgets.QLabel(self.ltw_scrollAreaWidgetContents)
        self.ltw_time_step_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.ltw_time_step_label.setObjectName("ltw_time_step_label")
        self.ltw_scrollArea_gridLayout.addWidget(self.ltw_time_step_label, 14, 0, 1, 1)
        self.ltw_time_step_spinBox = QtWidgets.QDoubleSpinBox(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_time_step_spinBox.setObjectName("ltw_time_step_spinBox")
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_time_step_spinBox, 15, 0, 1, 1
        )

        # Auto set capacitance?
        self.ltw_autoset_capacitance_HLayout = QtWidgets.QHBoxLayout()
        self.ltw_autoset_capacitance_toggleSwitch = ToggleSwitch()
        self.ltw_autoset_capacitance_label = QtWidgets.QLabel("Autoset Capacitance")
        self.ltw_autoset_capacitance_HLayout.addWidget(
            self.ltw_autoset_capacitance_toggleSwitch
        )
        self.ltw_autoset_capacitance_HLayout.addWidget(
            self.ltw_autoset_capacitance_label
        )
        self.ltw_scrollArea_gridLayout.addLayout(
            self.ltw_autoset_capacitance_HLayout, 18, 0, 1, 1
        )

        # Save Power button
        self.ltw_start_measurement_pushButton = QtWidgets.QPushButton(
            self.ltw_scrollAreaWidgetContents
        )
        self.ltw_start_measurement_pushButton.setObjectName(
            "ltw_start_measurement_pushButton"
        )
        self.ltw_scrollArea_gridLayout.addWidget(
            self.ltw_start_measurement_pushButton, 19, 0, 1, 1
        )

        self.tabWidget.addTab(self.ltw_widget, "")

        # -------------------------------------------------------------------- #
        # --------------------------- Spacer Tab ----------------------------- #
        # -------------------------------------------------------------------- #
        self.spacer2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.spacer2, "")
        self.tabWidget.setTabEnabled(self.tabWidget.indexOf(self.spacer2), False)

        # -------------------------------------------------------------------- #
        # ----------------- Define capacitance Tester Widget ----------------- #
        # -------------------------------------------------------------------- #
        self.capacitance_tester_widget = QtWidgets.QWidget()
        self.capacitance_tester_widget.setObjectName("capacitance_tester_widget")
        self.capacitance_tester_gridLayout = QtWidgets.QGridLayout(
            self.capacitance_tester_widget
        )
        self.capacitance_tester_gridLayout.setObjectName(
            "capacitance_tester_gridLayout"
        )

        # --------------- Central Widget with matplotlib graph --------------- #
        self.capw_graph_widget = QtWidgets.QWidget(self.capacitance_tester_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.capw_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.capw_graph_widget.setSizePolicy(sizePolicy)
        self.capw_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.capw_graph_widget.setObjectName("capw_graph_widget")
        self.capw_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.capw_graph_widget)
        self.capw_mpl_graph_gridLayout.setObjectName("capw_mpl_graph_gridLayout")
        self.capacitance_tester_gridLayout.addWidget(self.capw_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.capw_fig = FigureCanvas(Figure(figsize=figureSize))
        self.capw_mpl_graph_gridLayout.addWidget(self.capw_fig)

        self.capw_ax = self.capw_fig.figure.subplots()
        # self.capw_ax.set_facecolor("#E0E0E0")
        self.capw_ax.grid(True)
        self.capw_ax.set_xlabel("Frequency (kHz)", fontsize=14)
        self.capw_ax.set_ylabel("Current (A)", fontsize=14)
        self.capw_ax.set_xlim([50, 600])

        self.capw_ax.axhline(linewidth=1, color="black")
        self.capw_ax.axvline(linewidth=1, color="black")

        # self.capw_fig.figure.set_facecolor("#E0E0E0")
        self.capw_mplToolbar = NavigationToolbar(self.capw_fig, self.capw_graph_widget)
        self.capw_mplToolbar.setStyleSheet("background-color:white; color:black; ")
        self.capw_mpl_graph_gridLayout.addWidget(self.capw_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.capw_scrollArea = QtWidgets.QScrollArea(self.capacitance_tester_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.capw_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.capw_scrollArea.setSizePolicy(sizePolicy)
        self.capw_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.capw_scrollArea.setWidgetResizable(True)
        self.capw_scrollArea.setObjectName("capw_scrollArea")
        self.capw_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.capw_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.capw_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.capw_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.capw_scrollAreaWidgetContents.setObjectName(
            "capw_scrollAreaWidgetContents"
        )
        self.capw_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_scrollArea_gridLayout.setObjectName("capw_scrollArea_gridLayout")

        self.capw_header1_label = QtWidgets.QLabel(self.capw_scrollAreaWidgetContents)
        self.capw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.capw_header1_label.setObjectName("capw_header1_label")
        self.capw_scrollArea_gridLayout.addWidget(self.capw_header1_label, 0, 0, 1, 1)
        self.capw_scrollArea.setWidget(self.capw_scrollAreaWidgetContents)
        self.capacitance_tester_gridLayout.addWidget(self.capw_scrollArea, 0, 3, 1, 1)

        # Set voltage
        self.capw_voltage_label = QtWidgets.QLabel(self.capw_scrollAreaWidgetContents)
        self.capw_voltage_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.capw_voltage_label.setObjectName("capw_voltage_label")
        self.capw_scrollArea_gridLayout.addWidget(self.capw_voltage_label, 1, 0, 1, 1)
        self.capw_voltage_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_voltage_spinBox.setObjectName("capw_voltage_spinBox")
        self.capw_scrollArea_gridLayout.addWidget(self.capw_voltage_spinBox, 2, 0, 1, 1)

        # Set current limit
        self.capw_current_label = QtWidgets.QLabel(self.capw_scrollAreaWidgetContents)
        self.capw_current_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.capw_current_label.setObjectName("capw_current_label")
        self.capw_scrollArea_gridLayout.addWidget(self.capw_current_label, 3, 0, 1, 1)
        self.capw_current_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_current_spinBox.setObjectName("capw_current_spinBox")
        self.capw_scrollArea_gridLayout.addWidget(self.capw_current_spinBox, 4, 0, 1, 1)

        # Set minimum scan frequency
        self.capw_minimum_frequency_label = QtWidgets.QLabel(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_minimum_frequency_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.capw_minimum_frequency_label.setObjectName("capw_minimum_frequency_label")
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_minimum_frequency_label, 5, 0, 1, 1
        )
        self.capw_minimum_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_minimum_frequency_spinBox.setObjectName(
            "capw_minimum_frequency_spinBox"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_minimum_frequency_spinBox, 6, 0, 1, 1
        )

        # Set maximum scan frequency
        self.capw_maximum_frequency_label = QtWidgets.QLabel(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_maximum_frequency_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.capw_maximum_frequency_label.setObjectName("capw_maximum_frequency_label")
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_maximum_frequency_label, 7, 0, 1, 1
        )
        self.capw_maximum_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_maximum_frequency_spinBox.setObjectName(
            "capw_maximum_frequency_spinBox"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_maximum_frequency_spinBox, 8, 0, 1, 1
        )

        # Set frequency step
        self.capw_frequency_step_label = QtWidgets.QLabel(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_frequency_step_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.capw_frequency_step_label.setObjectName("capw_frequency_step_label")
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_frequency_step_label, 9, 0, 1, 1
        )
        self.capw_frequency_step_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_frequency_step_spinBox.setObjectName("capw_frequency_step_spinBox")
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_frequency_step_spinBox, 10, 0, 1, 1
        )

        # Set minimum capacitance
        self.capw_resonance_frequency_step_label = QtWidgets.QLabel(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_resonance_frequency_step_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.capw_resonance_frequency_step_label.setObjectName(
            "capw_resonance_frequency_step_label"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_resonance_frequency_step_label, 11, 0, 1, 1
        )
        self.capw_resonance_frequency_step_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_resonance_frequency_step_spinBox.setObjectName(
            "capw_resonance_frequency_step_spinBox"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_resonance_frequency_step_spinBox, 12, 0, 1, 1
        )

        # # Set maximum scan capacitance
        # self.capw_maximum_capacitance_label = QtWidgets.QLabel(
        #     self.capw_scrollAreaWidgetContents
        # )
        # self.capw_maximum_capacitance_label.setStyleSheet(
        #     'font: 63 bold 10pt "Segoe UI";'
        # )
        # self.capw_maximum_capacitance_label.setObjectName(
        #     "capw_maximum_capacitance_label"
        # )
        # self.capw_scrollArea_gridLayout.addWidget(
        #     self.capw_maximum_capacitance_label, 13, 0, 1, 1
        # )
        # self.capw_maximum_capacitance_spinBox = QtWidgets.QDoubleSpinBox(
        #     self.capw_scrollAreaWidgetContents
        # )
        # self.capw_maximum_capacitance_spinBox.setObjectName(
        #     "capw_maximum_capacitance_spinBox"
        # )
        # self.capw_scrollArea_gridLayout.addWidget(
        #     self.capw_maximum_capacitance_spinBox, 14, 0, 1, 1
        # )

        # Set Frequency Margin around the resonance frequency
        self.capw_frequency_margin_label = QtWidgets.QLabel(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_frequency_margin_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.capw_frequency_margin_label.setObjectName("capw_frequency_margin_label")
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_frequency_margin_label, 13, 0, 1, 1
        )
        self.capw_frequency_margin_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_frequency_margin_spinBox.setObjectName(
            "capw_frequency_margin_spinBox"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_frequency_margin_spinBox, 14, 0, 1, 1
        )

        # Set frequency settling time (time to wait until we measure)
        self.capw_frequency_settling_time_label = QtWidgets.QLabel(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_frequency_settling_time_label.setStyleSheet(
            'font: 63 bold 10pt "Segoe UI";'
        )
        self.capw_frequency_settling_time_label.setObjectName(
            "capw_frequency_settling_time_label"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_frequency_settling_time_label, 15, 0, 1, 1
        )
        self.capw_frequency_settling_time_spinBox = QtWidgets.QDoubleSpinBox(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_frequency_settling_time_spinBox.setObjectName(
            "capw_frequency_settling_time_spinBox"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_frequency_settling_time_spinBox, 16, 0, 1, 1
        )

        # Save Power button
        self.capw_start_measurement_pushButton = QtWidgets.QPushButton(
            self.capw_scrollAreaWidgetContents
        )
        self.capw_start_measurement_pushButton.setObjectName(
            "capw_start_measurement_pushButton"
        )
        self.capw_scrollArea_gridLayout.addWidget(
            self.capw_start_measurement_pushButton, 17, 0, 1, 1
        )

        self.tabWidget.addTab(self.capacitance_tester_widget, "")

        # -------------------------------------------------------------------- #
        # -------------------- Define pid tuning Widget ---------------------- #
        # -------------------------------------------------------------------- #
        self.pid_widget = QtWidgets.QWidget()
        self.pid_widget.setObjectName("pid_widget")
        self.pid_widget_gridLayout = QtWidgets.QGridLayout(self.pid_widget)
        self.pid_widget_gridLayout.setObjectName("pid_widget_gridLayout")

        # --------------- Central Widget with matplotlib graph --------------- #
        self.pidw_graph_widget = QtWidgets.QWidget(self.pid_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pidw_graph_widget.sizePolicy().hasHeightForWidth()
        )
        self.pidw_graph_widget.setSizePolicy(sizePolicy)
        self.pidw_graph_widget.setMinimumSize(QtCore.QSize(0, 442))
        self.pidw_graph_widget.setObjectName("pidw_graph_widget")
        self.pidw_mpl_graph_gridLayout = QtWidgets.QGridLayout(self.pidw_graph_widget)
        self.pidw_mpl_graph_gridLayout.setObjectName("pidw_mpl_graph_gridLayout")
        self.pid_widget_gridLayout.addWidget(self.pidw_graph_widget, 0, 1, 1, 1)

        # Define figure
        figureSize = (11, 10)
        self.pidw_fig = FigureCanvas(Figure(figsize=figureSize))
        self.pidw_mpl_graph_gridLayout.addWidget(self.pidw_fig)

        self.pidw_ax = self.pidw_fig.figure.subplots()
        # self.pidw_ax.set_facecolor("#E0E0E0")
        self.pidw_ax.grid(True)
        self.pidw_ax.set_xlabel("Time (s)", fontsize=14)
        self.pidw_ax.set_ylabel("AC Magnetic Field (mT)", fontsize=14)
        self.pidw_ax.set_xlim([50, 600])

        self.pidw_ax.axhline(linewidth=1, color="black")
        self.pidw_ax.axvline(linewidth=1, color="black")

        # self.pidw_ax2 = self.pidw_ax.twinx()
        # self.pidw_ax2.set_ylabel(
        #     "Vmax (V)",
        #     fontsize=14,
        # )

        # self.pidw_fig.figure.set_facecolor("#E0E0E0")
        self.pidw_mplToolbar = NavigationToolbar(self.pidw_fig, self.pidw_graph_widget)
        self.pidw_mplToolbar.setStyleSheet("background-color:white; color:black;")
        self.pidw_mpl_graph_gridLayout.addWidget(self.pidw_mplToolbar)

        # ----------------------- Define scroll area ---------------------------
        self.pidw_scrollArea = QtWidgets.QScrollArea(self.pid_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pidw_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.pidw_scrollArea.setSizePolicy(sizePolicy)
        self.pidw_scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.pidw_scrollArea.setWidgetResizable(True)
        self.pidw_scrollArea.setObjectName("pidw_scrollArea")
        self.pidw_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.pidw_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 655))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pidw_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.pidw_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.pidw_scrollAreaWidgetContents.setObjectName(
            "pidw_scrollAreaWidgetContents"
        )
        self.pidw_scrollArea_gridLayout = QtWidgets.QGridLayout(
            self.pidw_scrollAreaWidgetContents
        )
        self.pidw_scrollArea_gridLayout.setObjectName("pidw_scrollArea_gridLayout")

        self.pidw_header1_label = QtWidgets.QLabel(self.pidw_scrollAreaWidgetContents)
        self.pidw_header1_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.pidw_header1_label.setObjectName("pidw_header1_label")
        self.pidw_scrollArea_gridLayout.addWidget(self.pidw_header1_label, 0, 0, 1, 1)
        self.pidw_scrollArea.setWidget(self.pidw_scrollAreaWidgetContents)
        self.pid_widget_gridLayout.addWidget(self.pidw_scrollArea, 0, 3, 1, 1)

        # Set voltage
        self.pidw_voltage_label = QtWidgets.QLabel(self.pidw_scrollAreaWidgetContents)
        self.pidw_voltage_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.pidw_voltage_label.setObjectName("pidw_voltage_label")
        self.pidw_scrollArea_gridLayout.addWidget(self.pidw_voltage_label, 1, 0, 1, 1)
        self.pidw_voltage_spinBox = QtWidgets.QDoubleSpinBox(
            self.pidw_scrollAreaWidgetContents
        )
        self.pidw_voltage_spinBox.setObjectName("pidw_voltage_spinBox")
        self.pidw_scrollArea_gridLayout.addWidget(self.pidw_voltage_spinBox, 2, 0, 1, 1)

        # Set current limit
        self.pidw_current_label = QtWidgets.QLabel(self.pidw_scrollAreaWidgetContents)
        self.pidw_current_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.pidw_current_label.setObjectName("pidw_current_label")
        self.pidw_scrollArea_gridLayout.addWidget(self.pidw_current_label, 3, 0, 1, 1)
        self.pidw_current_spinBox = QtWidgets.QDoubleSpinBox(
            self.pidw_scrollAreaWidgetContents
        )
        self.pidw_current_spinBox.setObjectName("pidw_current_spinBox")
        self.pidw_scrollArea_gridLayout.addWidget(self.pidw_current_spinBox, 4, 0, 1, 1)

        # Set minimum scan frequency
        self.pidw_frequency_label = QtWidgets.QLabel(self.pidw_scrollAreaWidgetContents)
        self.pidw_frequency_label.setStyleSheet('font: 63 bold 10pt "Segoe UI";')
        self.pidw_frequency_label.setObjectName("pidw_frequency_label")
        self.pidw_scrollArea_gridLayout.addWidget(self.pidw_frequency_label, 5, 0, 1, 1)
        self.pidw_frequency_spinBox = QtWidgets.QDoubleSpinBox(
            self.pidw_scrollAreaWidgetContents
        )
        self.pidw_frequency_spinBox.setObjectName("pidw_frequency_spinBox")
        self.pidw_scrollArea_gridLayout.addWidget(
            self.pidw_frequency_spinBox, 6, 0, 1, 1
        )

        # Auto set capacitance?
        self.pidw_autoset_capacitance_HLayout = QtWidgets.QHBoxLayout()
        self.pidw_autoset_capacitance_toggleSwitch = ToggleSwitch()
        self.pidw_autoset_capacitance_label = QtWidgets.QLabel("Autoset Capacitance")
        self.pidw_autoset_capacitance_HLayout.addWidget(
            self.pidw_autoset_capacitance_toggleSwitch
        )
        self.pidw_autoset_capacitance_HLayout.addWidget(
            self.pidw_autoset_capacitance_label
        )
        self.pidw_scrollArea_gridLayout.addLayout(
            self.pidw_autoset_capacitance_HLayout, 7, 0, 1, 1
        )

        # Save button
        self.pidw_start_measurement_pushButton = QtWidgets.QPushButton(
            self.pidw_scrollAreaWidgetContents
        )
        self.pidw_start_measurement_pushButton.setObjectName(
            "pidw_start_measurement_pushButton"
        )
        self.pidw_scrollArea_gridLayout.addWidget(
            self.pidw_start_measurement_pushButton, 8, 0, 1, 1
        )

        self.tabWidget.addTab(self.pid_widget, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # -------------------------------------------------------------------- #
        # ------------------------- Define Menubar --------------------------- #
        # -------------------------------------------------------------------- #

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 31))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)

        # Define actions for menubar
        self.actionOpen_Logs = QtGui.QAction(MainWindow)
        self.actionOpen_Logs.setObjectName("actionOpen_Logs")
        # self.actionOpen_Logfile_on_Machine = QtWidgets.QAction(MainWindow)
        # self.actionOpen_Logfile_on_Machine.setObjectName(
        # "actionOpen_Logfile_on_Machine"
        # )

        self.actionChange_Path = QtGui.QAction(MainWindow)
        self.actionChange_Path.setObjectName("actionChange_Path")

        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")

        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")

        self.actionOpen_Log = QtGui.QAction(MainWindow)
        self.actionOpen_Log.setObjectName("actionOpen_Log")
        self.menuSettings.addAction(self.actionOptions)
        self.menuSettings.addAction(self.actionDocumentation)
        self.menuSettings.addAction(self.actionOpen_Log)
        self.menubar.addAction(self.menuSettings.menuAction())

        # -------------------------------------------------------------------- #
        # ----------------------- Define Statusbar --------------------------- #
        # -------------------------------------------------------------------- #

        # Define progress bar in the status bar
        self.progressBar = QtWidgets.QProgressBar()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(150, 15))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(
            "QProgressBar"
            "{"
            "border-radius: 5px;"
            "background-color: #E0E0E0;"
            "text-align: center;"
            "color: black;"
            'font: 63 bold 10pt "Segoe UI";'
            "}"
            "QProgressBar::chunk "
            "{"
            "background-color: rgb(85, 170, 255);"
            "border-radius: 5px;"
            "}"
        )

        # Define the statusbar itself
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setAccessibleName("")
        self.statusbar.setObjectName("statusbar")
        self.statusbar.addPermanentWidget(self.progressBar)
        self.statusbar.showMessage("Ready", 10000000)

        MainWindow.setStatusBar(self.statusbar)

        # -------------------------------------------------------------------- #
        # --------------------- Some General things -------------------------- #
        # -------------------------------------------------------------------- #
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        This function basicall contains all the text that is visible in the window.
        I think it is good practice to keep this seperate just in case the program
        would be translated to other languages.
        """

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ME Device Benchmarker"))
        # self.gatherlab_label.setText(
        # _translate("MainWindow", "Gatherlab JVL Measurement")
        # )
        # self.sw_header2_label.setText(
        # _translate("MainWindow", "Source Voltage & Current")
        # )
        self.sw_browse_pushButton.setText(_translate("MainWindow", "Browse"))
        self.sw_voltage_spinBox.setSuffix(_translate("MainWindow", " V"))
        self.sw_current_spinBox.setSuffix(_translate("MainWindow", " A"))
        self.sw_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.sw_capacitance_spinBox.setSuffix(_translate("MainWindow", " pF"))
        self.sw_dc_current_spinBox.setSuffix(_translate("MainWindow", " A"))
        # self.sw_resistance_spinBox.setSuffix(_translate("MainWindow", " Ohm"))
        self.sw_source_output_pushButton.setText(
            _translate("MainWindow", "Output On/Off")
        )
        self.sw_batch_name_label.setText(_translate("MainWindow", "Batch Name"))
        self.sw_device_number_label.setText(_translate("MainWindow", "Device Number"))
        self.sw_device_size_label.setText(
            _translate("MainWindow", "Device Size (length, width) in mm")
        )
        self.sw_header1_label.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>The file name the data is saved in in the end"
                " will be in the format"
                " yyyy-mm-dd_&lt;batch-name&gt;_d&lt;device-number&gt;_p&lt;pixel-number&gt;.csv.</p></body></html>",
            )
        )
        self.sw_header1_label.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Dashboard that shows the current values of the important parameters.</p></body></html>",
            )
        )
        self.sw_header1_label.setText(
            _translate("MainWindow", "Batch Name and File Path")
        )
        self.sw_header2_label.setText(_translate("MainWindow", "Current Parameters"))
        # self.sw_change_voltage_label.setText(
        # _translate("MainWindow", "Change Voltage (V)")
        # )
        # self.sw_documentation_label.setToolTip(
        # _translate(
        # "MainWindow",
        # "<html><head/><body><p>Please write here any comments to the"
        # " measurement of your batch. The comments will be saved as .md file"
        # " within your selected file path. If there are any issues with the"
        # " measurement setup or the software document it in a seperate line"
        # " starting with [!] to ensure easy debugging.</p></body></html>",
        # )
        # )
        # self.sw_documentation_label.setText(_translate("MainWindow", "Documentation"))
        self.sw_folder_path_label.setText(_translate("MainWindow", "Folder Path"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.setup_widget), _translate("MainWindow", "Setup")
        )

        self.pulsew_header1_label.setText(
            _translate("MainWindow", "Measurement Parameters")
        )
        self.pulsew_folder_path_label.setText(
            _translate("MainWindow", "Pulsing Instructions")
        )
        self.pulsew_browse_pushButton.setText(_translate("MainWindow", "Browse"))
        self.pulsew_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )

        # self.pidw_max_voltage_label.setText(
        # _translate("MainWindow", "Max Voltage (V)")
        # )
        self.specw_voltage_label.setText(_translate("MainWindow", "Voltage (V)"))
        self.specw_current_label.setText(
            _translate("MainWindow", "AC Magnetic Field (mT)")
        )
        self.specw_dc_magnetic_field_label.setText(
            _translate("MainWindow", "DC Magnetic Field (mT)")
        )
        self.specw_minimum_frequency_label.setText(
            _translate("MainWindow", "Min Frequency (kHz)")
        )
        self.specw_maximum_frequency_label.setText(
            _translate("MainWindow", "Max Frequency (kHz)")
        )
        self.specw_frequency_step_label.setText(
            _translate("MainWindow", "Frequency Step (kHz)")
        )
        self.specw_frequency_settling_time_label.setText(
            _translate("MainWindow", "Settling Time (s)")
        )
        self.specw_autoset_capacitance_toggleSwitch.setText(
            _translate("MainWindow", "Autoset Capacitance")
        )
        self.specw_autoset_frequency_step_toggleSwitch.setText(
            _translate("MainWindow", "Autoset Frequency Step")
        )

        self.specw_constant_magnetic_field_mode_toggleSwitch.setText(
            _translate("MainWindow", "Constant Magnetic Field Mode")
        )

        self.specw_voltage_spinBox.setSuffix(_translate("MainWindow", " V"))
        self.specw_current_spinBox.setSuffix(_translate("MainWindow", " mT"))
        self.specw_dc_magnetic_field_spinBox.setSuffix(_translate("MainWindow", " mT"))
        self.specw_minimum_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.specw_maximum_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.specw_frequency_step_spinBox.setSuffix(_translate("MainWindow", " kHz"))

        self.specw_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )
        self.specw_header1_label.setText(
            _translate("MainWindow", "Measurement Parameters")
        )

        self.bw_voltage_label.setText(_translate("MainWindow", "Voltage (V)"))
        self.bw_current_label.setText(
            _translate("MainWindow", "AC Magnetic Field (mT)")
        )
        self.bw_frequency_label.setText(_translate("MainWindow", "Frequency (kHz)"))
        self.bw_minimum_dc_magnetic_field_label.setText(
            _translate("MainWindow", "Min DC Field (mT)")
        )
        self.bw_maximum_dc_magnetic_field_label.setText(
            _translate("MainWindow", "Max DC Field (mT)")
        )
        self.bw_dc_magnetic_field_step_label.setText(
            _translate("MainWindow", "DC Field Step (mT)")
        )
        self.bw_dc_magnetic_field_settling_time_label.setText(
            _translate("MainWindow", "Settling Time (s)")
        )
        self.bw_autoset_capacitance_toggleSwitch.setText(
            _translate("MainWindow", "Autoset Capacitance")
        )
        self.bw_reverse_sweep_toggleSwitch.setText(
            _translate("MainWindow", "Reverse Sweep")
        )

        self.bw_constant_magnetic_field_mode_toggleSwitch.setText(
            _translate("MainWindow", "Constant Magnetic Field Mode")
        )

        self.bw_voltage_spinBox.setSuffix(_translate("MainWindow", " V"))
        self.bw_current_spinBox.setSuffix(_translate("MainWindow", " mT"))
        self.bw_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.bw_minimum_dc_magnetic_field_spinBox.setSuffix(
            _translate("MainWindow", " mT")
        )
        self.bw_maximum_dc_magnetic_field_spinBox.setSuffix(
            _translate("MainWindow", " mT")
        )
        self.bw_dc_magnetic_field_step_spinBox.setSuffix(
            _translate("MainWindow", " mT")
        )

        self.bw_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )
        self.bw_header1_label.setText(
            _translate("MainWindow", "Measurement Parameters")
        )

        self.hfw_voltage_compliance_label.setText(
            _translate("MainWindow", "Voltage Compliance (V)")
        )
        self.hfw_dc_magnetic_field_label.setText(
            _translate("MainWindow", "DC Magnetic Field (mT)")
        )
        self.hfw_frequency_label.setText(_translate("MainWindow", "Frequency (kHz)"))
        self.hfw_minimum_voltage_label.setText(
            _translate("MainWindow", "Min Voltage (V)")
        )
        self.hfw_maximum_voltage_label.setText(
            _translate("MainWindow", "Max Voltage (V)")
        )
        self.hfw_voltage_step_label.setText(
            _translate("MainWindow", "Voltage Step (V)")
        )
        self.hfw_voltage_settling_time_label.setText(
            _translate("MainWindow", "Settling Time (s)")
        )
        self.hfw_autoset_capacitance_toggleSwitch.setText(
            _translate("MainWindow", "Autoset Capacitance")
        )

        self.hfw_constant_magnetic_field_mode_toggleSwitch.setText(
            _translate("MainWindow", "Magnetic Field Mode")
        )

        self.hfw_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )

        self.ltw_voltage_compliance_label.setText(
            _translate("MainWindow", "Voltage Compliance (V)")
        )
        self.ltw_dc_magnetic_field_label.setText(
            _translate("MainWindow", "DC Magnetic Field (mT)")
        )
        self.ltw_frequency_label.setText(_translate("MainWindow", "Frequency (kHz)"))
        self.ltw_total_time_label.setText(
            _translate("MainWindow", "Total Measurement Time (s)")
        )
        self.ltw_time_step_label.setText(
            _translate("MainWindow", "Measurement Interval (s)")
        )
        self.ltw_hf_magnetic_field_label.setText(
            _translate("MainWindow", "Magnetic Field (V)")
        )
        self.ltw_autoset_capacitance_toggleSwitch.setText(
            _translate("MainWindow", "Autoset Capacitance")
        )

        self.ltw_constant_magnetic_field_mode_toggleSwitch.setText(
            _translate("MainWindow", "Magnetic Field Mode")
        )

        # self.ltw_current_spinBox.setSuffix(_translate("MainWindow", " mT"))
        self.ltw_dc_magnetic_field_spinBox.setSuffix(_translate("MainWindow", " mT"))
        self.ltw_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.ltw_hf_magnetic_field_spinBox.setSuffix(_translate("MainWindow", " V"))
        self.ltw_total_time_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.ltw_time_step_spinBox.setSuffix(_translate("MainWindow", " s"))

        self.ltw_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )
        self.ltw_header1_label.setText(
            _translate("MainWindow", "Measurement Parameters")
        )

        self.capw_voltage_label.setText(_translate("MainWindow", "Voltage (V)"))
        self.capw_current_label.setText(_translate("MainWindow", "Maximum Current (A)"))
        self.capw_minimum_frequency_label.setText(
            _translate("MainWindow", "Min Frequency (kHz)")
        )
        self.capw_maximum_frequency_label.setText(
            _translate("MainWindow", "Max Frequency (kHz)")
        )
        self.capw_frequency_step_label.setText(
            _translate("MainWindow", "Frequency Step (kHz)")
        )
        self.capw_voltage_spinBox.setSuffix(_translate("MainWindow", " V"))
        self.capw_current_spinBox.setSuffix(_translate("MainWindow", " A"))
        self.capw_minimum_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.capw_maximum_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.capw_frequency_step_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.capw_resonance_frequency_step_spinBox.setSuffix(
            _translate("MainWindow", " kHz")
        )
        self.capw_frequency_margin_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        self.capw_frequency_settling_time_spinBox.setSuffix(
            _translate("MainWindow", " s")
        )
        self.capw_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )
        self.capw_header1_label.setText(
            _translate("MainWindow", "Measurement Parameters")
        )
        self.capw_resonance_frequency_step_label.setText(
            _translate("MainWindow", "Resonance Freq Step (kHz)")
        )
        self.capw_frequency_margin_label.setText(
            _translate("MainWindow", "Frequency Margin (kHz)")
        )
        self.capw_frequency_settling_time_label.setText(
            _translate("MainWindow", "Settling Time (s)")
        )

        # self.ow_voltage_label.setText(_translate("MainWindow", "Voltage (V)"))
        # self.ow_current_label.setText(_translate("MainWindow", "Maximum Current (A)"))
        # self.ow_minimum_frequency_label.setText(
        # _translate("MainWindow", "Min Frequency (kHz)")
        # )
        # self.ow_maximum_frequency_label.setText(
        # _translate("MainWindow", "Max Frequency (kHz)")
        # )
        # self.ow_frequency_step_label.setText(
        #     _translate("MainWindow", "Frequency Step (kHz)")
        # )
        # self.ow_voltage_spinBox.setSuffix(_translate("MainWindow", " V"))
        # self.ow_current_spinBox.setSuffix(_translate("MainWindow", " A"))
        # self.ow_minimum_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        # self.ow_maximum_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))
        # self.ow_frequency_step_spinBox.setSuffix(_translate("MainWindow", " kHz"))

        self.pidw_voltage_label.setText(_translate("MainWindow", "Voltage (V)"))
        self.pidw_current_label.setText(
            _translate("MainWindow", "AC Magnetic Field (mT)")
        )
        self.pidw_frequency_label.setText(_translate("MainWindow", "Frequency (kHz)"))
        self.pidw_autoset_capacitance_toggleSwitch.setText(
            _translate("MainWindow", "Autoset Capacitance")
        )

        self.pidw_voltage_spinBox.setSuffix(_translate("MainWindow", " V"))
        self.pidw_current_spinBox.setSuffix(_translate("MainWindow", " mT"))
        self.pidw_frequency_spinBox.setSuffix(_translate("MainWindow", " kHz"))

        self.pidw_start_measurement_pushButton.setText(
            _translate("MainWindow", "Start Measurement")
        )
        self.pidw_header1_label.setText(
            _translate("MainWindow", "Measurement Parameters")
        )

        # self.specw_changeover_voltage_label.setText(
        # _translate("MainWindow", "Changeover Voltage (V)")
        # )
        # self.specw_low_voltage_step_label.setText(
        # _translate("MainWindow", "Low Voltage Step (V)")
        # )
        # self.specw_scan_compliance_label.setText(
        # _translate("MainWindow", "Scan Compliance (A)")
        # )
        # self.specw_pd_saturation_checkBox.setText(
        # _translate("MainWindow", "Check for PD Saturation")
        # )
        # self.specw_select_pixel_label.setText(_translate("MainWindow", "Select Pixels"))
        # self.specw_bad_contact_checkBox.setText(
        # _translate("MainWindow", "Check fo Bad Contacts")
        # )

        self.ow_stop_pushButton.setText(_translate("MainWindow", "Run/Stop"))
        self.ow_auto_scale_pushButton.setText(_translate("MainWindow", "Auto Scale"))
        self.ow_start_measurement_pushButton.setText(
            _translate("MainWindow", "Save Data")
        )
        self.ow_header1_label.setText(_translate("MainWindow", "Osci Parameters"))

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.spectrum_widget),
            _translate("MainWindow", "Resonance Frequency"),
        )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.bias_field_widget),
            _translate("MainWindow", "Bias Field"),
        )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.hf_field_widget),
            _translate("MainWindow", "AC Field"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.ltw_widget),
            _translate("MainWindow", "Lifetime"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.capacitance_tester_widget),
            _translate("MainWindow", "Capacitance Calibration"),
        )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.pulsing_widget),
            _translate("MainWindow", "Pulsing"),
        )

        # self.tabWidget.setTabText(
        #     self.tabWidget.indexOf(self.spacer),
        #     _translate("MainWindow", "               "),
        # )

        # self.tabWidget.setTabText(
        #     self.tabWidget.indexOf(self.spacer2),
        #     _translate("MainWindow", "               "),
        # )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.osci_widget),
            _translate("MainWindow", "Oscilloscope"),
        )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.pid_widget),
            _translate("MainWindow", "PID Tuning"),
        )

        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))

        # self.actionOpen_Logs.setText(_translate("MainWindow", "Open Logs"))
        # self.actionOpen_Logfile_on_Machine.setText(
        # _translate("MainWindow", "Open Logfile on Machine")
        # )
        self.actionChange_Path.setText(_translate("MainWindow", "Change Saving Path"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionDocumentation.setText(_translate("MainWindow", "Help"))

        self.actionOpen_Log.setText(_translate("MainWindow", "Open Log"))

    # ------------------------------------------------------------------------ #
    # ----------------- User Defined UI related Functions -------------------- #
    # ------------------------------------------------------------------------ #
    def center(self):
        # position and size of main window

        # self.showFullScreen()
        qc = self.frameGeometry()
        # desktopWidget = QtWidgets.QApplication.desktop()
        # PCGeometry = desktopWidget.screenGeometry()
        # self.resize(PCGeometry.height(), PCGeometry.height())
        screen = QtWidgets.QApplication.primaryScreen()
        cp = screen.availableGeometry().center()
        qc.moveCenter(cp)
        self.move(qc.topLeft())
