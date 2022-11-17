from PyQt5 import QtWidgets, QtCore
from qtwidgets import PasswordEdit
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        password = PasswordEdit()
        password.setGeometry(QtCore.QRect(210, 250, 461, 51))
        self.setCentralWidget(password)


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()