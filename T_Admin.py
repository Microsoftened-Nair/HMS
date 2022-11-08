from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='HMS'
)

c = db.cursor()

class Ui_MainWindow(object):

    def CreateTable(self, table, widnum):
        c.execute(f"select * from {table}")
        data = c.fetchall()

        eval(f'self.tableWidget{widnum}.setRowCount(0)')

        for row_number, row_data in enumerate(data):
            eval(f'self.tableWidget{widnum}.insertRow(row_number)')

            for column_number, item in enumerate(row_data):
                eval(f'self.tableWidget{widnum}.setItem(row_number, column_number, QTableWidgetItem(str(item)))')

        # else:
        #     self.tableWidget_1.setRowCount(0)
        #
        #     for row_number, row_data in enumerate(data):
        #         self.tableWidget_1.insertRow(row_number)
        #
        #         for column_number, item in enumerate(row_data):
        #             self.tableWidget_1.setItem(row_number, column_number, QTableWidgetItem(str(item)))


    def PMSTable(self):
        c.execute(f"select * from pms")
        data = c.fetchall()

        self.tableWidget_1.setRowCount(0)

        for row_number, row_data in enumerate(data):
            self.tableWidget_1.insertRow(row_number)

            for column_number, item in enumerate(row_data):
                self.tableWidget_1.setItem(row_number, column_number, QTableWidgetItem(str(item)))

    def DMSTable(self):
        c.execute("select * from dms")
        data = c.fetchall()

        self.tableWidget_2.setRowCount(0)

        for row_number, row_data in enumerate(data):
            self.tableWidget_2.insertRow(row_number)

            for column_number, item in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(item)))

    def DrugMSTable(self):
        c.execute("select * from pms")
        data = c.fetchall()

        self.tableWidget_3.setRowCount(0)

        for row_number, row_data in enumerate(data):
            self.tableWidget_3.insertRow(row_number)

            for column_number, item in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(item)))

    def Sign_out(self):
        from Sign_in import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


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
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_1.setGeometry(QtCore.QRect(20, 80, 1101, 641))
        self.tableWidget_1.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.tableWidget_1.setStyleSheet("QTableView {\n"
"    font: 11pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.setColumnCount(5)
        self.tableWidget_1.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(4, item)
        self.tableWidget_1.horizontalHeader().setVisible(True)
        self.tableWidget_1.horizontalHeader().setDefaultSectionSize(214)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 20, 221, 41))
        self.pushButton_3.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 20, 871, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 80, 1101, 641))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.tableWidget_2.setStyleSheet("QTableView {\n"
"    font: 11pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem("DocID")
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("DocID")
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("DocID")
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem("DocID")
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem("DocID")
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(215)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
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
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 80, 1101, 641))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.tableWidget_3.setStyleSheet("QTableView {\n"
"    font: 11pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(214)
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
        icon.addPixmap(QtGui.QPixmap("assets/SignOut_Light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Sign_out)
        self.pushButton_5.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "!xobile"))
        self.pushButton.setText(_translate("MainWindow", "Enter command"))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Illness"))
        item = self.tableWidget_1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PhoneNo"))
        item = self.tableWidget_1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Patient"))
        self.pushButton_3.setText(_translate("MainWindow", "Enter command"))
        self.lineEdit_3.setText(_translate("MainWindow", "!xobile"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DocID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DocName"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Department"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Doctor"))
        self.pushButton_4.setText(_translate("MainWindow", "Enter command"))
        self.lineEdit_4.setText(_translate("MainWindow", "!xobile"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DrugID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DrugName"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Department"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Composition"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Expiry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Drug"))
        self.CreateTable('pms', '_1')
        self.CreateTable('dms', '_2')
        self.CreateTable('drugms', '_3')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
