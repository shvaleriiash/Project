from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 700)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 900, 80))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, -1, 31, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.left_color = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.left_color.setText("")
        self.left_color.setObjectName("left_color")
        self.gridLayout.addWidget(self.left_color, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(110, 0, 131, 83))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.black_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.black_c.setText("")
        self.black_c.setObjectName("black_c")
        self.gridLayout_3.addWidget(self.black_c, 0, 0, 1, 1)
        self.grey_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.grey_c.setText("")
        self.grey_c.setObjectName("grey_c")
        self.gridLayout_3.addWidget(self.grey_c, 0, 3, 1, 1)
        self.brown_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.brown_c.setText("")
        self.brown_c.setObjectName("brown_c")
        self.gridLayout_3.addWidget(self.brown_c, 1, 3, 1, 1)
        self.red_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.red_c.setText("")
        self.red_c.setObjectName("red_c")
        self.gridLayout_3.addWidget(self.red_c, 1, 1, 1, 1)
        self.blue_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.blue_c.setText("")
        self.blue_c.setObjectName("blue_c")
        self.gridLayout_3.addWidget(self.blue_c, 1, 2, 1, 1)
        self.yellow_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.yellow_c.setText("")
        self.yellow_c.setObjectName("yellow_c")
        self.gridLayout_3.addWidget(self.yellow_c, 0, 1, 1, 1)
        self.green_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.green_c.setText("")
        self.green_c.setObjectName("green_c")
        self.gridLayout_3.addWidget(self.green_c, 0, 2, 1, 1)
        self.white_c = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.white_c.setText("")
        self.white_c.setObjectName("white_c")
        self.gridLayout_3.addWidget(self.white_c, 1, 0, 1, 1)
        self.collor_settings = QtWidgets.QPushButton(self.groupBox)
        self.collor_settings.setGeometry(QtCore.QRect(280, 20, 101, 41))
        self.collor_settings.setObjectName("collor_settings")
        self.clean = QtWidgets.QPushButton(self.groupBox)
        self.clean.setGeometry(QtCore.QRect(480, 20, 100, 41))
        self.clean.setObjectName("clean_button")
        self.grab_btn = QtWidgets.QPushButton(self.groupBox)
        self.grab_btn.setGeometry(QtCore.QRect(600, 20, 100, 41))
        self.grab_btn.setObjectName("screen_button")
        self.line = QtWidgets.QLabel(self.groupBox)
        self.line.setObjectName("screen_button")
        self.line.setGeometry(QtCore.QRect(740, 20, 100, 41))
        self.brash = QtWidgets.QComboBox(self.groupBox)
        self.brash.setGeometry(QtCore.QRect(780, 20, 40, 41))
        self.brash.setObjectName("brash_button")
        self.brash.addItems(["3", "6", "8", "10", "12", "14", "16", "18", "20", "22", "25"])
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 80, 900, 700))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NOTEPAD"))
        self.groupBox.setTitle(_translate("MainWindow", "??????????"))
        self.collor_settings.setText(_translate("MainWindow", "?????????????????? ????????"))
        self.clean.setText(_translate("MainWindow", "????????????????"))
        self.grab_btn.setText(_translate("MainWindow", "??????????????????"))
        self.line.setText(_translate("MainWindow", "??????????"))