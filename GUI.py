import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class testwindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(testwindow, self).__init__(*args,**kwargs)

        self.setWindowTitle('Test')
        self.setGeometry(0,0,500,500)
        label = QLabel('Test', self)
        label.setAlignment(Qt.AlignHCenter)
        label.setStyleSheet('border:2px solid black')


def window():
    app = QApplication(sys.argv)
    win = testwindow()
    win.show()
    sys.exit(app.exec_())


window()