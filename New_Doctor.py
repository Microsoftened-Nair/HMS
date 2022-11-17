from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from New_Doctor_ui import Ui_NewDoctor
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='hms'
)

c = db.cursor()

class NewDoctor(QtWidgets.QWidget, Ui_NewDoctor):

    closed = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def Submit(self):
        c.execute("select * from dms;")
        res = c.fetchall()
        l = res[-1]

        docID = int(l[0]) + 1
        name = self.lineEdit.text()
        dept = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        sex = self.lineEdit_5.text()

        cmd = f'insert into dms values({docID}, "{name}", "{dept}", "{email}", "{sex}");'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.closed.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWidget = NewDoctor()
    myWidget.show()
    sys.exit(app.exec_())