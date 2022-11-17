from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Delete_Doctor_UI import Ui_DeleteDoctor
import mysql.connector


class DeleteDocWin(QtWidgets.QWidget, Ui_DeleteDoctor):
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

        DocID = self.lineEdit.text()
        c = db.cursor()
        cmd = f'delete from dms where DocID={DocID}'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.delclose.emit()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = DeleteDocWin()
    win.show()
    sys.exit(app.exec_())

