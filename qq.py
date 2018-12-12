import random
import sys
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QKeyEvent

class SKRAMBL(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('skrb.ui', self)
        self.timer1 = QTimer()

        self.skrambl = ['F', 'F\'', 'F2',
                   'B', 'B\'', 'B2',
                   'U', 'U\'', 'U2',
                   'D', 'D\'', 'D2',
                   'R', 'R\'', 'R2',
                   'L', 'L\'', 'L2']

        self.n = random.randint(13, 25)
        a = []
        for i in range(self.n):
            k = random.randint(0, len(self.skrambl) - 1)
            a.append(self.skrambl[k])
        sk = ('  '.join(a))

        self.fl = True

        self.timer1.timeout.connect(self.tablo)


    def tablo(self):
        self.timer.setText(str(time.time() - self.t))


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.fl:
                self.timer1.start(10)
                self.t = time.time()
            else:
                self.timer1.stop()
            self.fl = not self.fl


app = QApplication(sys.argv)
ex = SKRAMBL()
ex.show()
sys.exit(app.exec_())
