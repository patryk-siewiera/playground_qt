from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
import sys


# for conversion .ui file -> python
# in terminal:
# pyuic5 -x input_file.ui -o output_file.py
# -o -> write generated code to FILE instead of stdout
# -x, -- execute ->  generate extra code to test and display the class


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech with Tim")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(20, 30)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
