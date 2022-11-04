from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database='HMS',
)

mycursor = mydb.cursor()
mycursor.execute("describe pms")
myresult = mycursor.fetchall()

lst = []
for x in myresult:
    lst.append(x[0])

mycursor.execute("select * from pms")
myresult = mycursor.fetchall()

class Ui_PatientWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 877)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 877))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setBaseSize(QtCore.QSize(1440, 877))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(40, 30, 1151, 791))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1151, 791))
        self.tabWidget.setMaximumSize(QtCore.QSize(1151, 791))
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"    font: 20pt \"Bahnschrift\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 871, 41))
        self.lineEdit.setStyleSheet("QLineEdit    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(900, 20, 221, 41))
        self.pushButton.setStyleSheet("QPushButton    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
#         self.textEdit = QtWidgets.QTextEdit(self.tab)
#         self.textEdit.setGeometry(QtCore.QRect(20, 10, 1101, 711))
#         self.textEdit.setStyleSheet("QTextEdit {\n"
# "    font: 18pt \"Bahnschrift\";\n"
# "    color: rgb(255, 255, 255);\n"
# "}")
#         self.textEdit.setReadOnly(True)
#         self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 10, 1101, 711))
        self.textEdit_3.setStyleSheet("QTextEdit {\n"
"    font: 18pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
#         self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
#         self.pushButton_3.setGeometry(QtCore.QRect(900, 20, 221, 41))
#         self.pushButton_3.setStyleSheet("QPushButton    {\n"
# "    background-color: rgb(0, 0, 0);\n"
# "    color: rgb(255, 255, 255);\n"
# "    font: 75 14pt \"Bahnschrift\";\n"
# "    border: 2px solid rgb(255, 255, 255);\n"
# "}\n"
# "\n"
# "QPushButton:hover  {\n"
# "    background-color: rgb(255, 255, 255);\n"
# "    color: rgb(0, 0, 0);\n"
# "    font: 75 14pt \"Bahnschrift\";\n"
# "    border: 2px solid rgb(255, 255, 255);\n"
# "}")
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
#         self.lineEdit_3.setGeometry(QtCore.QRect(20, 20, 871, 41))
#         self.lineEdit_3.setStyleSheet("QLineEdit    {\n"
# "    background-color: rgb(0, 0, 0);\n"
# "    color: rgb(255, 255, 255);\n"
# "    font: 75 14pt \"Bahnschrift\";\n"
# "    border: 2px solid rgb(255, 255, 255);\n"
# "}")
#         self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 90, 1101, 631))
        self.textEdit_4.setStyleSheet("QTextEdit {\n"
"    font: 18pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(900, 20, 221, 41))
        self.pushButton_4.setStyleSheet("QPushButton    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 20, 871, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1230, 30, 51, 81))
        self.pushButton_5.setStyleSheet("QPushButton    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"}")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets\SignOut_Light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "!xobile"))
        self.pushButton.setText(_translate("MainWindow", "Enter command"))
        # self.textEdit.setText(_translate("MainWindow", f"{lst}"))
        # for x in myresult:
        #     self.textEdit.append(f"{x}")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Patient"))
        mycursor.execute("describe Dms")
        res = mycursor.fetchall()
        doc = []
        for i in res:
            doc.append(i[0])

        self.textEdit_3.setText(_translate("MainWindow", f"{doc}"))
        mycursor.execute("select * from dms")
        docdata = mycursor.fetchall()
        for t in docdata:
            self.textEdit_3.append(f"{t}")
        # self.pushButton_3.setText(_translate("MainWindow", "Enter command"))
        # self.lineEdit_3.setText(_translate("MainWindow", "!xobile"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Doctor"))
        mycursor.execute('describe drugms')
        drugcol = mycursor.fetchall()
        col = []
        for y in drugcol:
            col.append(y[0])
        self.textEdit_4.setText(_translate("MainWindow", f"{col}"))
        mycursor.execute('select * from drugms')
        drugdata = mycursor.fetchall()
        for o in drugdata:
            self.textEdit_4.append(f'{o}')
        self.pushButton_4.setText(_translate("MainWindow", "Enter command"))
        self.lineEdit_4.setText(_translate("MainWindow", "!xobile"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Drug"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PatientWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
