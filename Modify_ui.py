from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifyWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 649)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 151, 61))
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 26pt \"Bahnschrift\";\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 411, 41))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 570, 201, 51))
        self.pushButton.setStyleSheet("QPushButton    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Mod)
        self.pushButton.clicked.connect(MainWindow.close)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 131, 41))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 131, 41))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 320, 131, 41))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 131, 41))
        self.label_5.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 250, 411, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 320, 411, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 390, 411, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 141, 41))
        self.label_7.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 110, 191, 41))
        self.pushButton_2.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.showRec)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 110, 211, 41))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Modify"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "Illness"))
        self.label_4.setText(_translate("MainWindow", "PhoneNo"))
        self.label_5.setText(_translate("MainWindow", "Gender"))
        self.label_7.setText(_translate("MainWindow", "Insert Pid:"))
        self.pushButton_2.setText(_translate("MainWindow", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ModifyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
