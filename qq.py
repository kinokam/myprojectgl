import random
import sys
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QTimer


class SKRAMBL (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('skrb.ui', self)
        self.timer1 = QTimer()

        try:
            file = open('Рекорд.txt')
        except IOError:
            pass
        else:
            with open('Рекорд.txt', 'r') as f:
                f.seek(0)
                first_char = f.read(1)
                if first_char:
                    f.seek(0)
                    self.set(float(f.read()))

        self.btn.clicked.connect(self.tablo1)

        self.code = ['F', 'F\'', 'F2',
                        'B', 'B\'', 'B2',
                        'U', 'U\'', 'U2',
                        'D', 'D\'', 'D2',
                        'R', 'R\'', 'R2',
                        'L', 'L\'', 'L2']

        n = random.randint(13, 25)
        a = []
        for i in range(n):
            k = random.randint(0, len(self.code) - 1)
            a.append(self.code[k])
        self.sk = (' '.join(a))

        self.fl = True

        self.timer1.timeout.connect(self.tablo)

    def set(self, record):
        self.best.setText('{0:.3f}'.format(record))

    def tablo(self):
        self.timer.setText('{0:.3f}'.format(time.time() - self.time1))

    def tablo1(self):
        n = random.randint(13, 25)
        a = []
        for i in range(n):
            k = random.randint(0, len(self.code) - 1)
            a.append(self.code[k])
        self.sk = (' '.join(a))

        self.fl = True
        self.skrambl.setText(self.sk)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            if self.fl:
                self.timer1.start(10)
                self.time1 = time.time()
            else:
                tm = time.time() - self.time1
                try:
                    file = open('Рекорд.txt')
                except IOError:
                    with open('Рекорд.txt', 'w') as f:
                        f.write('{0:.3f}'.format(tm))
                        self.set(tm)
                else:
                    with open('Рекорд.txt', 'r') as f:
                        f.seek(0)
                        first_char = f.read(1)
                    if not first_char:
                        with open('Рекорд.txt', 'w') as f:
                            f.write('{0:.3f}'.format(tm))
                            self.set(tm)
                    else:
                        with open('Рекорд.txt', 'r') as f:
                            best = float(f.read())
                        if best > tm:
                            with open('Рекорд.txt', 'w') as f:
                                f.seek(0)
                                f.write('{0:.3f}'.format(tm))
                                self.set(tm)
                self.timer1.stop()
            self.fl = not self.fl




app = QApplication(sys.argv)
ex = SKRAMBL()
ex.show()
sys.exit(app.exec_())
