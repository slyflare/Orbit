import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class testwindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(testwindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("wha-")
        label = QLabel('KORE GA REQUIEM DA')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


def window():
    app = QApplication(sys.argv)
    win = testwindow()
    win.setGeometry(0,0,500,500)
    win.show()
    sys.exit(app.exec_())


window()