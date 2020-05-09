import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class testwindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(testwindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("test string")
        label = QLabel('bubjabksdjkabsdjkb')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = testwindow()
window.show()

app.exec_()