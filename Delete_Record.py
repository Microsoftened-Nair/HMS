from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Delete_Record_UI import Ui_DeleteRecord
import mysql.connector


class DeleteWin(QtWidgets.QWidget, Ui_DeleteRecord):
    delclose = pyqtSignal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def deleteRec(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='hms'
        )

        pid = self.lineEdit.text()
        c = db.cursor()
        cmd = f'delete from pms where pid={pid}'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.delclose.emit()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = DeleteWin()
    win.show()
    sys.exit(app.exec_())

