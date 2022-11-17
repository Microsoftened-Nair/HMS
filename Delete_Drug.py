from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Delete_Drug_UI import Ui_DeleteDrug
import mysql.connector


class DeleteDrugWin(QtWidgets.QWidget, Ui_DeleteDrug):
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

        drugID = self.lineEdit.text()
        c = db.cursor()
        cmd = f'delete from drugms where DrugID={drugID}'
        c.execute(cmd)
        db.commit()

    def closeEvent(self, event):
        self.delclose.emit()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = DeleteDrugWin()
    win.show()
    sys.exit(app.exec_())

