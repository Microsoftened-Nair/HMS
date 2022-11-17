from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Modify_Doc_ui import Ui_ModifyDocWindow
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='hms'
)
c = db.cursor()

class ModifyDocWin(QtWidgets.QWidget, Ui_ModifyDocWindow):
    modclose = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def showRec(self):
        docID = self.lineEdit_6.text()

        cmd = f'select * from dms where DocID={docID}'
        c.execute(cmd)
        res = c.fetchall()
        cell = res[0]
        self.lineEdit.setText(str(cell[1]))
        self.lineEdit_2.setText(str(cell[2]))
        self.lineEdit_3.setText(str(cell[3]))
        self.lineEdit_4.setText(str(cell[4]))

    def Mod(self):
        docID = self.lineEdit_6.text()
        name = self.lineEdit.text()
        dept = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        sex = self.lineEdit_4.text()
        cmd = f'update dms set Doc_name="{name}", Department="{dept}", Email="{email}",Gender="{sex}" where DocID={docID};'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.modclose.emit()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = ModifyDocWin()
    win.show()
    sys.exit(app.exec_())

