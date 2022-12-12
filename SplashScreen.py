from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from SplashScreen_ui import Ui_SplashWindow
import mysql.connector
import os, time

class SplashWin(QtWidgets.QWidget, Ui_SplashWindow):
    # close = pyqtSignal()

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.setupUi(self)

    def checkfiles(self):
        self.label_2.setText('Checking files.....')
        files = open('files.txt').readlines()
        curlist = os.listdir()
        lst = ['.git', '.gitignore', '.idea', 'assets', '__pycache__']
        for i in lst:
            curlist.remove(i)

        if len(files) > len(os.listdir()):
            self.label_2.setText('Files missing, download again')
        else:
            self.label_2.setText("Good to go!")
            self.close()

# def closeEvent(self, event):
# 		self.close.emit()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = SplashWin()
    win.show()
    sys.exit(app.exec_())
