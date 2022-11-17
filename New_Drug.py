from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from New_Drug_ui import Ui_NewDrug
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='hms'
)

c = db.cursor()

class New_Drug(QtWidgets.QWidget, Ui_NewDrug):

    closed = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def Submit(self):
        c.execute("select * from drugms;")
        res = c.fetchall()
        l = res[-1]

        drugID = int(l[0]) + 1
        name = self.lineEdit.text()
        dept = self.lineEdit_3.text()
        comp = self.lineEdit_4.text()
        exp = self.lineEdit_5.text()

        cmd = f'insert into drugms values({drugID}, "{name}", "{dept}", "{comp}", "{exp}");'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.closed.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWidget = New_Drug()
    myWidget.show()
    sys.exit(app.exec_())