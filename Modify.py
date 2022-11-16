from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Modify_ui import Ui_ModifyWindow
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='hms'
)
c = db.cursor()

class ModifyWin(QtWidgets.QWidget, Ui_ModifyWindow):
    modclose = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def showRec(self):
        pid = self.lineEdit_6.text()

        cmd = f'select * from pms where pid={pid}'
        c.execute(cmd)
        res = c.fetchall()
        cell = res[0]
        self.lineEdit.setText(str(cell[1]))
        self.lineEdit_2.setText(str(cell[2]))
        self.lineEdit_3.setText(str(cell[3]))
        self.lineEdit_4.setText(str(cell[4]))

    def Mod(self):
        pid = self.lineEdit_6.text()
        name = self.lineEdit.text()
        ill = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        sex = self.lineEdit_4.text()
        cmd = f'update pms set Patient_name="{name}", Illness="{ill}", PhoneNo="{phone}",Gender="{sex}" where PID={pid};'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.modclose.emit()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = ModifyWin()
    win.show()
    sys.exit(app.exec_())

