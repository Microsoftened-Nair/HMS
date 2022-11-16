from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from New_Record_ui import Ui_NewRecord
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='hms'
)

c = db.cursor()

class NewRecord(QtWidgets.QWidget, Ui_NewRecord):

    closed = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def Submit(self):
        c.execute("select * from pms;")
        res = c.fetchall()
        l = res[-1]

        pid = int(l[0]) + 1
        name = self.lineEdit.text()
        ill = self.lineEdit_3.text()
        phone = int(self.lineEdit_4.text())
        sex = self.lineEdit_5.text()

        cmd = f'insert into pms values({pid}, "{name}", "{ill}", {phone}, "{sex}");'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.closed.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWidget = NewRecord()
    myWidget.show()
    sys.exit(app.exec_())