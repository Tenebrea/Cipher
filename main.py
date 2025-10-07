from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QActionGroup
from PyQt6.QtWidgets import QApplication, QFileDialog, QStackedLayout, QVBoxLayout, QButtonGroup, QRadioButton, QGridLayout, QLabel, QMainWindow, QMenu, QToolBar, QPushButton, QLineEdit, QWidget
from functions import base64_encoder, verman_cipher, vigenere_cipher, caesars_cipher, eng_caesars_cipher, eng_vigenere_cipher


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.encrypt_state = True
        self.getting_from_file = True
        self.eng = True
        self.cipher = "vigenere"
        self.text = ""
        self.key = ""

        self.setWindowTitle("Encrypter")
        self.setFixedSize(600, 300)

        self.container = QWidget(self)
        main_layout = QVBoxLayout(self.container)
        self.stack_layout = QStackedLayout()

        main_layout.addLayout(self.stack_layout)

        self.label_text = QLabel(self.container)
        self.label_text.move(140, 10)
        self.label_text.setText("")
        self.label_text.setFixedWidth(1600)

        self.label_key = QLabel(self.container)
        self.label_key.move(140, 50)
        self.label_key.setText("")
        self.label_key.setFixedWidth(1600)

        self.vigenere_layout()
        self.caesar_layout()
        self.base64_layout()
        self.verman_layout()

        self.create_toolbar()
        self.create_encryption()

        self.stack_layout.setCurrentIndex(0)

        self.setCentralWidget(self.container)

    def vigenere_layout(self):
        self.vigenere_widget = QWidget(self)

        self.text_vigenere = QLabel(self.vigenere_widget)
        self.text_vigenere.setText("Текст:")
        self.text_vigenere.move(10, 10)

        self.input_text_vigenere = QPushButton(self.vigenere_widget)
        self.input_text_vigenere.setFixedWidth(80)
        self.input_text_vigenere.setText("Выбрать")
        self.input_text_vigenere.move(50, 10)
        self.input_text_vigenere.clicked.connect(self.get_text)

        self.key_vigenere = QLabel(self.vigenere_widget)
        self.key_vigenere.setText("Ключ:")
        self.key_vigenere.move(10, 50)

        self.input_key_vigenere = QPushButton(self.vigenere_widget)
        self.input_key_vigenere.setFixedWidth(80)
        self.input_key_vigenere.setText("Выбрать")
        self.input_key_vigenere.move(50, 50)
        self.input_key_vigenere.clicked.connect(self.get_key)

        self.stack_layout.addWidget(self.vigenere_widget)

    def caesar_layout(self):
        self.caesar_widget = QWidget(self)

        self.text_caesar = QLabel(self.caesar_widget)
        self.text_caesar.setText("Текст:")
        self.text_caesar.move(10, 10)

        self.input_text_caesar = QPushButton(self.caesar_widget)
        self.input_text_caesar.setFixedWidth(80)
        self.input_text_caesar.setText("Выбрать")
        self.input_text_caesar.move(50, 10)
        self.input_text_caesar.clicked.connect(self.get_text)

        self.key_caesar = QLabel(self.caesar_widget)
        self.key_caesar.setText("Ключ:")
        self.key_caesar.move(10, 50)

        self.input_key_caesar = QLineEdit(self.caesar_widget)
        self.input_key_caesar.setFixedWidth(80)
        self.input_key_caesar.move(50, 50)

        self.stack_layout.addWidget(self.caesar_widget)

    def base64_layout(self):
        self.base64_widget = QWidget(self)

        self.text_base64 = QLabel(self.base64_widget)
        self.text_base64.setText("Текст:")
        self.text_base64.move(10, 10)

        self.input_text_base64 = QPushButton(self.base64_widget)
        self.input_text_base64.setFixedWidth(80)
        self.input_text_base64.setText("Выбрать")
        self.input_text_base64.move(50, 10)
        self.input_text_base64.clicked.connect(self.get_text)

        self.stack_layout.addWidget(self.base64_widget)

    def create_toolbar(self):
        self.tool_bar = QToolBar("Main panel")
        self.addToolBar(self.tool_bar)
        self.tool_bar.setMovable(False)

        menu = self.menuBar()

        self.action_group = QActionGroup(self)
        self.action_group.setExclusive(True)

        self.getting_of_file = QActionGroup(self)
        self.getting_of_file.setExclusive(True)

        get_from_file = QAction("Из файла")
        get_from_file.setStatusTip("Вводить текст и ключ из файла")
        get_from_file.setCheckable(True)
        get_from_file.setChecked(True)
        get_from_file.triggered.connect(self.change_getting)

        get_from_entries = QAction("Вводить")
        get_from_entries.setStatusTip("Вводить текст в строку")
        get_from_entries.setCheckable(True)
        get_from_entries.triggered.connect(self.change_getting)

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

        self.getting_of_file.addAction(get_from_entries)
        self.getting_of_file.addAction(get_from_file)

        self.action_group.addAction(action1)
        self.action_group.addAction(action2)
        self.action_group.addAction(action4)
        self.action_group.addAction(action3)

        self.tool_bar.addAction(action1)
        self.tool_bar.addAction(action2)
        self.tool_bar.addAction(action4)
        self.tool_bar.addAction(action3)

        file_menu = menu.addMenu("File")
        file_menu.addAction(get_from_entries)
        file_menu.addAction(get_from_file)

    def create_encryption(self):
        self.encrypt = QRadioButton("Зашифровать", self)
        self.encrypt.move(10, 150)
        self.encrypt.setChecked(True)
        self.encrypt.clicked.connect(self.change_encrypt)

        self.decrypt = QRadioButton("Расшифровать", self)
        self.decrypt.move(120, 150)
        self.decrypt.clicked.connect(self.change_encrypt)

        self.encrypt_radio_button = QButtonGroup(self)

        self.encrypt_radio_button.addButton(self.encrypt)
        self.encrypt_radio_button.addButton(self.decrypt)

        self.get_result = QPushButton(self)
        self.get_result.setText("Получить")
        self.get_result.move(10, 180)
        self.get_result.clicked.connect(self.encrypt_text)

    def create_language_changer(self):
        self.russian = QRadioButton("Зашифровать", self)
        self.russian.move(10, 150)
        self.russian.setChecked(True)
        self.russian.clicked.connect(self.change_encrypt)

        self.english = QRadioButton("Расшифровать", self)
        self.english.move(120, 150)
        self.english.clicked.connect(self.change_encrypt)

        self.encrypt_radio_button = QButtonGroup(self)

        self.encrypt_radio_button.addButton(self.encrypt)
        self.encrypt_radio_button.addButton(self.decrypt)

        self.get_result = QPushButton(self)
        self.get_result.setText("Получить")
        self.get_result.move(10, 180)
        self.get_result.clicked.connect(self.encrypt_text)

    def change_encrypt(self):
        selected_button = self.encrypt_radio_button.checkedButton()
        if selected_button.text() == "Зашифровать":
            self.encrypt_state = True
        else:
            self.encrypt_state = False

    def change_language(self):
        selected_button = self.encrypt_radio_button.checkedButton()
        if selected_button.text() == "Зашифровать":
            self.encrypt_state = True
        else:
            self.encrypt_state = False

    def change_getting(self):
        selected_action = self.getting_of_file.checkedAction()
        if selected_action.text() == "Из файла":
            self.getting_from_file = True
        else:
            self.getting_from_file = False

    def change_layout(self):
        self.vigenere_widget.hide()
        self.caesar_widget.hide()
        self.base64_widget.hide()
        self.verman_widget.hide()

        selected_cipher = self.action_group.checkedAction().text()
        match selected_cipher:
            case "Vigenere":
                self.cipher = "vigenere"
                self.stack_layout.setCurrentIndex(0)
            case "Caesar":
                self.cipher = "caesar"
                self.stack_layout.setCurrentIndex(1)
            case "BASE64":
                self.cipher = "base64"
                self.stack_layout.setCurrentIndex(2)
            case "Verman":
                self.cipher = "verman"
                self.stack_layout.setCurrentIndex(3)

    def get_text(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        try:
            with open(file, 'r', encoding='utf-8') as source:
                self.text = source.read()
            if file:
                self.label_text.setText(f"Selected file: {file}")
            else:
                self.label_text.setText("No file selected")
        except:
            self.label_text.setText("Error")

    def get_key(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        try:
            with open(file, 'r', encoding='utf-8') as source:
                self.key = source.readline()
            if file:
                self.label_key.setText(f"Selected file: {file}")
            else:
                self.label_key.setText("No file selected")
        except:
            self.label_key.setText("Error")

    def encrypt_text(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Text File",
            "document.txt",
            "Text Files (*.txt);;All Files (*)"
        )
        match self.cipher:
            case "vigenere":
                self.text = eng_vigenere_cipher(
                    self.text, self.key, self.encrypt_state)
            case "caesar":
                try:
                    self.key = int(self.input_key_caesar.text())
                    self.text = eng_caesars_cipher(
                        self.text, self.key, self.encrypt_state)
                except:
                    return
            case "base64":
                self.text = base64_encoder(self.text, self.encrypt_state)
            case "verman":
                self.text = verman_cipher(self.text, self.key)

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text)
            except:
                return


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
