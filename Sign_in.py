from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Sign_in_ui import Ui_Sign_in
import mysql.connector

try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='HMS')
    c = db.cursor()
except:
    print("MySQL error run: ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'; in your mysql window")

class SignInWin(QtWidgets.QWidget, Ui_Sign_in):
    closeSig = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.lineEdit_2.returnPressed.connect(self.authorize)
        self.pushButton.clicked.connect(self.authorize)
        self.pushButton_2.clicked.connect(self.NewPatient)
        self.pushButton_2.clicked.connect(self.close)

    def authorize(self):
        user = self.lineEdit.text()
        key = self.lineEdit_2.text()

        cmd = f'select username from accounts where username="{user}"'
        c.execute(cmd)
        r = c.fetchall()

        if len(r) == 0:
            self.label_4.setText("[USER DOES NOT EXIST          ]")

        if len(r) != 0:
            cmd = f'select password from accounts where username="{user}"'
            c.execute(cmd)
            r = c.fetchall()
            rs = r[0]

            if key == rs[0]:
                cmd = f'select permissions from accounts where username="{user}"'
                c.execute(cmd)
                r = c.fetchall()
                keys = r[0]
                p = keys[0]

                if p == 'a':
                    self.AdminWindow()
                if p == 'd':
                    self.DoctorWindow()
                if p == 'p':
                    self.PatientWindow()

            if key != rs[0]:
                self.label_4.setText('[INCORRECT PASSWORD            ]')

    def NewPatient(self):
        from New_Patient import Ui_NewPatient
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewPatient()
        self.ui.setupUi(self.window)
        self.window.show()

    def AdminWindow(self):
        self.close()
        from TB_Admin import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def DoctorWindow(self):
        self.close()
        from TB_Doctor import Ui_DoctorWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DoctorWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def PatientWindow(self):
        self.close()
        from TB_Patient import Ui_PatientWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatientWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def closeEvent(self, event):
        self.closeSig.emit()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = SignInWin()
    win.show()
    sys.exit(app.exec_())

