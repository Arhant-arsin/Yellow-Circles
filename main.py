from random import randint
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self), self.retranslateUi(self)
        self.pb_rand.clicked.connect(self.onClick)

    def onClick(self):
        self.draw()

    def draw(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        c1, c2, c3 = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QBrush(QColor(c1, c2, c3), Qt.SolidPattern))
        size = randint(10, 150)
        x, y = randint(0, 300), randint(0, 300)
        qp.drawEllipse(x, y, size, size)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())