import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class popupwindow(QWidget):
    def __init__(self):
        super(popupwindow).__init__()
        self.initui()
        self.setWindowTitle('Popup')
        self.setGeometry(0, 0, 250, 250)

    def initui(self):
        self.label = QLabel('Test', self)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet('border:2px solid black')
        self.label.setGeometry(200, 200, 100, 50)
        self.button.setStyleSheet('border:2px solid red')


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
        self.label.setText('wha--______------------___---_--_-----__-_-_-_-_-_--_------')
        self.label.adjustSize()


def window(args):
    app = QApplication(sys.argv)
    win = testwindow()
    win.show()
    sys.exit(app.exec_())


window()
