from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteDoctor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 109)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 201, 61))
        self.pushButton.setStyleSheet("QPushButton    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.deleteRec)
        self.pushButton.clicked.connect(MainWindow.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 20, 170, 51))
        self.label.setStyleSheet("QLabel {\n"
"    \n"
"    font: 18pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 20, 201, 61))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    \n"
"    font: 18pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.deleteRec)
        self.lineEdit.returnPressed.connect(MainWindow.close)

        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Delete record"))
        self.label.setText(_translate("MainWindow", "Insert DocID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DeleteDoctor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
