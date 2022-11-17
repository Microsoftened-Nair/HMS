from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Enter_command_ui import Ui_EnterWindow
import mysql.connector


class EnterWin(QtWidgets.QWidget, Ui_EnterWindow):
    enterclose = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def enterCommand(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='hms'
        )

        c = db.cursor()
        cmd = self.lineEdit.text()
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.enterclose.emit()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = EnterWin()
    win.show()
    sys.exit(app.exec_())

