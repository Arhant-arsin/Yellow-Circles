from random import randint
import sys

from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pb_rand.clicked.connect(self.onClick)

    def onClick(self):
        self.draw()

    def draw(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QBrush(QColor(255, 255, 0), Qt.SolidPattern))
        size = randint(10, 150)
        x, y = randint(0, 300), randint(0, 300)
        qp.drawEllipse(x, y, size, size)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())