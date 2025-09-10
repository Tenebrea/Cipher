import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.windowTitle("Шифратор")

    


app = QApplication([])

window = MainWindow()
window.show()

app.exec()