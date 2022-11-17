from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='hms'
)
c = db.cursor()


class Ui_NewDrug(object):

    # def Refresh(self):
    #     print('function called')
    #     from TB_Admin import Ui_MainWindow
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #
    #     table = 'pms'
    #     widnum='_1'
    #
    #     c.execute("select * from pms")
    #     data = c.fetchall()
    #     print(data)
    #
    #     for row_number, row_data in enumerate(data):
    #         eval(f'self.ui.tableWidget{widnum}.insertRow(row_number)')
    #
    #         for column_number, item in enumerate(row_data):
    #             eval(f'self.ui.tableWidget{widnum}.setItem(row_number, column_number, QTableWidgetItem(str(item)))')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 568)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 231, 61))
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 26pt \"Bahnschrift\";\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 110, 411, 41))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 430, 201, 51))
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
        self.pushButton.clicked.connect(self.Submit)
        self.pushButton.clicked.connect(MainWindow.close)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 131, 41))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 131, 41))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 131, 41))
        self.label_5.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 16pt \"Bahnschrift\";\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 320, 131, 41))
        self.label_6.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 20pt \"Bahnschrift\";\n"
"}")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 180, 411, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 250, 411, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 320, 411, 41))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20pt \"Bahnschrift\";\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "New Drug"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Dept:"))
        self.label_5.setText(_translate("MainWindow", "Composition:"))
        self.label_6.setText(_translate("MainWindow", "Expiry:"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_NewDrug()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
