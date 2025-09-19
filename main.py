from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QMenu, QToolBar, QPushButton, QLineEdit, QWidget
from functions import base64_encoder, verman_cipher, vigenere_cipher, caesars_cipher


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_toolbar()

        self.setWindowTitle("Encrypter")
        self.setFixedSize(600, 300)

    def remove_everything(self):
        children = self.findChildren(QWidget)

        for child in children:
            child.deleteLater()

        self.create_toolbar()

    def vigenere_layout(self):
        self.remove_everything()

        self.input_text = QLineEdit(self)
        self.input_text.move(50, 50)

    def create_toolbar(self):
        tool_bar = QToolBar("Main panel")
        self.addToolBar(tool_bar)
        tool_bar.setMovable(False)

        action1 = QAction("Vigenere", self)
        action1.triggered.connect(self.vigenere_layout)

        action2 = QAction("Caesar", self)

        action3 = QAction("BASE64", self)

        action4 = QAction("Verman", self)

        tool_bar.addAction(action1)
        tool_bar.addAction(action2)
        tool_bar.addAction(action3)
        tool_bar.addAction(action4)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
