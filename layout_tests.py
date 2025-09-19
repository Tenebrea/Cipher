from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QActionGroup
from PyQt6.QtWidgets import QApplication, QButtonGroup, QRadioButton, QGridLayout, QLabel, QMainWindow, QMenu, QToolBar, QPushButton, QLineEdit, QWidget
from functions import base64_encoder, verman_cipher, vigenere_cipher, caesars_cipher


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.encrypt = True
        self.cipher = "vigenere"

        self.setWindowTitle("Encrypter")
        self.setFixedSize(600, 300)

        self.vigenere_layout()
        self.caesar_layout()
        self.base64_layout()
        self.verman_layout()

        self.create_toolbar()
        self.create_encryption()

    def vigenere_layout(self):
        self.vigenere_widget = QWidget(self)

        self.text_vigenere = QLabel(self.vigenere_widget)
        self.text_vigenere.setText("Текст:")
        self.text_vigenere.move(10, 10)

        self.input_text_vigenere = QPushButton(self.vigenere_widget)
        self.input_text_vigenere.setFixedWidth(80)
        self.input_text_vigenere.setText("Выбрать")
        self.input_text_vigenere.move(50, 10)

        self.key_vigenere = QLabel(self.vigenere_widget)
        self.key_vigenere.setText("Ключ:")
        self.key_vigenere.move(10, 50)

        self.input_key_vigenere = QPushButton(self.vigenere_widget)
        self.input_key_vigenere.setFixedWidth(80)
        self.input_key_vigenere.setText("Выбрать")
        self.input_key_vigenere.move(50, 50)

        # self.setCentralWidget(self.vigenere_widget)

    def caesar_layout(self):
        self.caesar_widget = QWidget(self)

        self.text_caesar = QLabel(self.caesar_widget)
        self.text_caesar.setText("Текст:")
        self.text_caesar.move(10, 10)

        self.input_text_caesar = QPushButton(self.caesar_widget)
        self.input_text_caesar.setFixedWidth(80)
        self.input_text_caesar.setText("Выбрать")
        self.input_text_caesar.move(50, 10)

        self.key_caesar = QLabel(self.caesar_widget)
        self.key_caesar.setText("Ключ:")
        self.key_caesar.move(10, 50)

        self.input_key_caesar = QLineEdit(self.caesar_widget)
        self.input_key_caesar.setFixedWidth(80)
        self.input_key_caesar.move(50, 50)

        self.caesar_widget.hide()

    def base64_layout(self):
        self.base64_widget = QWidget(self)

        self.text_base64 = QLabel(self.base64_widget)
        self.text_base64.setText("Текст:")
        self.text_base64.move(10, 10)

        self.input_text_base64 = QPushButton(self.base64_widget)
        self.input_text_base64.setFixedWidth(80)
        self.input_text_base64.setText("Выбрать")
        self.input_text_base64.move(50, 10)

        self.base64_widget.hide()

    def verman_layout(self):
        self.verman_widget = QWidget(self)

        self.text_verman = QLabel(self.verman_widget)
        self.text_verman.setText("Текст:")
        self.text_verman.move(10, 10)

        self.input_text_verman = QPushButton(self.verman_widget)
        self.input_text_verman.setFixedWidth(80)
        self.input_text_verman.setText("Выбрать")
        self.input_text_verman.move(50, 10)

        self.key_verman = QLabel(self.verman_widget)
        self.key_verman.setText("Ключ:")
        self.key_verman.move(10, 50)

        self.input_key_verman = QPushButton(self.verman_widget)
        self.input_key_verman.setFixedWidth(80)
        self.input_key_verman.setText("Выбрать")
        self.input_key_verman.move(50, 50)

        self.verman_widget.hide()

    def create_toolbar(self):
        self.tool_bar = QToolBar("Main panel")
        self.addToolBar(self.tool_bar)
        self.tool_bar.setMovable(False)

        self.action_group = QActionGroup(self)
        self.action_group.setExclusive(True)

        action1 = QAction("Vigenere", self)
        action1.setCheckable(True)
        action1.setChecked(True)
        action1.triggered.connect(self.change_layout)

        action2 = QAction("Caesar", self)
        action2.setCheckable(True)
        action2.triggered.connect(self.change_layout)

        action3 = QAction("BASE64", self)
        action3.setCheckable(True)
        action3.triggered.connect(self.change_layout)

        action4 = QAction("Verman", self)
        action4.setCheckable(True)
        action4.triggered.connect(self.change_layout)

        self.action_group.addAction(action1)
        self.action_group.addAction(action2)
        self.action_group.addAction(action3)
        self.action_group.addAction(action4)

        self.tool_bar.addAction(action1)
        self.tool_bar.addAction(action2)
        self.tool_bar.addAction(action3)
        self.tool_bar.addAction(action4)

    def create_encryption(self):
        self.encrypt = QRadioButton("Зашифровать", self)
        self.encrypt.move(10, 100)
        self.decrypt = QRadioButton("Расшифровать", self)
        self.decrypt.move(120, 100)

        self.encrypt_radio_button = QButtonGroup(self)

        self.encrypt_radio_button.addButton(self.encrypt)
        self.encrypt_radio_button.addButton(self.decrypt)

        self.get_result = QPushButton(self)
        self.get_result.setText("Получить")
        self.get_result.move(10, 140)

    def change_encrypt(self):
        selected_button = self.encrypt_radio_button.checkedButton()
        if selected_button.text() == "Зашифровать":
            self.encrypt = True
        else:
            self.encrypt = False

    def change_layout(self):
        self.vigenere_widget.hide()
        self.caesar_widget.hide()
        self.base64_widget.hide()
        self.verman_widget.hide()

        selected_cipher = self.action_group.checkedAction().text()
        match selected_cipher:
            case "Vigenere":
                self.cipher = "vigenere"
                # self.setCentralWidget(self.vigenere_widget)
                self.vigenere_widget.show()
            case "Caesar":
                self.cipher = "caesar"
                # self.setCentralWidget(self.caesar_widget)
                self.caesar_widget.show()
            case "BASE64":
                self.cipher = "base64"
                # self.setCentralWidget(self.base64_widget)
                self.base64_widget.show()
            case "Verman":
                self.cipher = "verman"
                # self.setCentralWidget(self.verman_widget)
                self.verman_widget.show()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
