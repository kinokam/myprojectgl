import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QKeyEvent

class SKRAMBL(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('skrb.ui', self)
        self.timer = QTimer()

    def timerr(self):
        self.timer.timeout.connect(self)
        self.timer.start(10)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.timer.start(10)

app = QApplication(sys.argv)
ex = SKRAMBL()
ex.show()
sys.exit(app.exec_())
