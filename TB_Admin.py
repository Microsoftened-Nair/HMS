from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector


class Ui_MainWindow(object):

    def CreateTable(self, table, widnum):

        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='HMS'
        )

        c = db.cursor()

        c.execute(f"select * from {table}")
        data = c.fetchall()


        eval(f'self.tableWidget{widnum}.setRowCount(0)')
        for row_number, row_data in enumerate(data):
            eval(f'self.tableWidget{widnum}.insertRow(row_number)')

            for column_number, item in enumerate(row_data):
                eval(f'self.tableWidget{widnum}.setItem(row_number, column_number, QTableWidgetItem(str(item)))')

    def Sign_out(self):
        from Sign_in import SignInWin
        self.ui = SignInWin()
        self.ui.show()


    def Delete_record(self):
        from Delete_Record import DeleteWin
        self.ui = DeleteWin()
        self.ui.show()
        self.ui.delclose.connect(lambda: self.CreateTable('pms', '_1'))
    def Modify_record(self):
        from Modify import ModifyWin
        self.ui = ModifyWin()
        self.ui.show()
        self.ui.modclose.connect(lambda: self.CreateTable('pms', '_1'))
    def New_record(self):
        from New_Record import NewRecord
        self.ui = NewRecord()
        self.ui.show()
        self.ui.closed.connect(lambda: self.CreateTable('pms', '_1'))

    def New_doctor(self):
        from New_Doctor import NewDoctor
        self.ui = NewDoctor()
        self.ui.show()
        self.ui.closed.connect(lambda: self.CreateTable('dms', '_2'))

    def Delete_doctor(self):
        from Delete_Doctor import DeleteDocWin
        self.ui = DeleteDocWin()
        self.ui.show()
        self.ui.delclose.connect(lambda: self.CreateTable('dms', '_2'))

    def Modify_doctor(self):
        from Modify_Doc import ModifyDocWin
        self.ui = ModifyDocWin()
        self.ui.show()
        self.ui.modclose.connect(lambda: self.CreateTable('dms', '_2'))

    def New_drug(self):
        from New_Drug import New_Drug
        self.ui = New_Drug()
        self.ui.show()
        self.ui.closed.connect(lambda: self.CreateTable('Drugms', '_3'))

    def Delete_drug(self):
        from Delete_Drug import DeleteDrugWin
        self.ui = DeleteDrugWin()
        self.ui.show()
        self.ui.delclose.connect(lambda: self.CreateTable('Drugms', '_3'))

    def Modify_drug(self):
        from Modify_Drug import ModifyDrugWin
        self.ui = ModifyDrugWin()
        self.ui.show()
        self.ui.modclose.connect(lambda: self.CreateTable('Drugms', '_3'))

    def Enter_command(self):
        from Enter_command import EnterWin
        self.ui = EnterWin()
        self.ui.show()
        self.ui.enterclose.connect(lambda: self.CreateTable('pms', '_1'))
        self.ui.enterclose.connect(lambda: self.CreateTable('dms', '_2'))
        self.ui.enterclose.connect(lambda: self.CreateTable('Drugms', '_3'))

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
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(490, 20, 221, 41))
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
        self.pushButton.clicked.connect(self.Modify_record)
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_1.setGeometry(QtCore.QRect(20, 80, 1101, 641))
        self.tableWidget_1.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.tableWidget_1.setStyleSheet("QTableView {\n"
"    font: 13pt \"Bahnschrift\";\n"
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
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 20, 221, 41))
        self.pushButton_2.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Delete_record)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.pushButton_6.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.New_record)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(900, 20, 221, 41))
        self.pushButton_13.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.Enter_command)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 80, 1101, 641))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.tableWidget_2.setStyleSheet("QTableView {\n"
"    font: 13pt \"Bahnschrift\";\n"
"    color: rgb(255, 255, 255);\n"
"}")

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(215)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 20, 221, 41))
        self.pushButton_8.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.Modify_doctor)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.pushButton_9.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.New_doctor)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setGeometry(QtCore.QRect(900, 20, 221, 41))
        self.pushButton_15.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.Enter_command)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 20, 221, 41))
        self.pushButton_10.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.Delete_doctor)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 80, 1101, 641))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.tableWidget_3.setStyleSheet("QTableView {\n"
"    font: 13pt \"Bahnschrift\";\n"
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
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(215)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_11.setGeometry(QtCore.QRect(490, 20, 221, 41))
        self.pushButton_11.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.Modify_drug)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.pushButton_12.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.New_drug)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_16.setGeometry(QtCore.QRect(900, 20, 221, 41))
        self.pushButton_16.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.Enter_command)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setGeometry(QtCore.QRect(250, 20, 221, 41))
        self.pushButton_17.setStyleSheet("QPushButton    {\n"
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
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.Delete_drug)
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1230, 30, 51, 81))
        self.pushButton_5.setStyleSheet("QPushButton    {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Bahnschrift\";\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.clicked.connect(self.Sign_out)
        self.pushButton_5.clicked.connect(MainWindow.close)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/SignOut_Light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HMS - Admin"))
        MainWindow.setWindowTitle(_translate("MainWindow", "HMS - New Record"))
        MainWindow.setWindowIcon(QtGui.QIcon('assets/LOGO.png'))
        self.pushButton.setText(_translate("MainWindow", "Modify"))
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
        self.pushButton_2.setText(_translate("MainWindow", "Delete record"))
        self.pushButton_6.setText(_translate("MainWindow", "Add record"))
        self.pushButton_13.setText(_translate("MainWindow", "Enter command"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Patient"))
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
        self.pushButton_8.setText(_translate("MainWindow", "Modify"))
        self.pushButton_9.setText(_translate("MainWindow", "Add record"))
        self.pushButton_15.setText(_translate("MainWindow", "Enter command"))
        self.pushButton_10.setText(_translate("MainWindow", "Delete record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Doctor"))
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
        self.pushButton_11.setText(_translate("MainWindow", "Modify"))
        self.pushButton_12.setText(_translate("MainWindow", "Add record"))
        self.pushButton_16.setText(_translate("MainWindow", "Enter command"))
        self.pushButton_17.setText(_translate("MainWindow", "Delete record"))
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
