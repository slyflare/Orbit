import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class testwindow(QMainWindow):
    def __init__(self):
        super(testwindow, self).__init__()
        self.initUI()
        self.setWindowTitle('Test')
        self.setGeometry(0, 0, 500, 500)

    def initUI(self):
        self.label = QLabel('Test', self)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet('border:2px solid black')
        self.label.setGeometry(200, 200, 100, 50)

        self.button = QPushButton(self)
        self.button.setText('test')
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('wha-')


def window():
    app = QApplication(sys.argv)
    win = testwindow()
    win.show()
    sys.exit(app.exec_())


window()