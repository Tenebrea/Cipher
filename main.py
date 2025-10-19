import sys

from PyQt6.QtGui import QActionGroup
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QLabel, QMainWindow
from functions import base64_encoder, verman_cipher, ru_vigenere_cipher, ru_caesars_cipher, eng_caesars_cipher, eng_vigenere_cipher
from MainWindow import Ui_MainWindow
import pyperclip


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.eng = False
        self.cipher = "caesar"
        self.text = ""
        self.key = ""
        self.result = ""

        self.setWindowTitle("Encrypter")
        self.setFixedSize(844, 499)

        self.grouping()
        self.connects()

        self.change_theme()

    def connects(self):
        self.ciphers.triggered.connect(self.change_method)

        self.ui.rus.triggered.connect(self.change_lang_ru)
        self.ui.eng.triggered.connect(self.change_lang_eng)

        self.ui.get_text.textChanged.connect(self.update_text)
        self.ui.get_key.textChanged.connect(self.update_key)

        self.ui.choose_file.clicked.connect(self.get_text_from_file)

        self.ui.print_key.clicked.connect(self.paste_key)
        self.ui.print_text.clicked.connect(self.paste_text)
        self.ui.copy_text.clicked.connect(self.copy_result)

        self.ui.encrypt_with_key.clicked.connect(self.encrypt_text_with_key)
        self.ui.encrypt_without_key.clicked.connect(
            self.encrypt_text_with_no_key)

        self.ui.decrypt_with_key.clicked.connect(self.decrypt_text_with_key)
        self.ui.decrypt_without_key.clicked.connect(
            self.decrypt_text_with_no_key)

        self.ui.save_file.clicked.connect(self.save_into_file)

        self.theme.triggered.connect(self.change_theme)

        self.ui.info.triggered.connect(self.show_info)

    def grouping(self):
        self.ciphers = QActionGroup(self)
        self.ciphers.setExclusive(True)
        self.ciphers.addAction(self.ui.caesar)
        self.ciphers.addAction(self.ui.vigenere)
        self.ciphers.addAction(self.ui.verman)
        self.ciphers.addAction(self.ui.base64)

        self.lang = QActionGroup(self)
        self.lang.setExclusive(True)
        self.lang.addAction(self.ui.rus)
        self.lang.addAction(self.ui.eng)

        self.theme = QActionGroup(self)
        self.theme.setExclusive(True)
        self.theme.addAction(self.ui.dark)
        self.theme.addAction(self.ui.light)

    def get_text_from_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        try:
            with open(file, 'r', encoding='utf-8') as source:
                self.text = source.readline()
            if file:
                self.ui.get_text.setText(self.key)
        except:
            return

    def update_text(self):
        self.text = self.ui.get_text.toPlainText()

    def update_key(self):
        self.key = self.ui.get_key.text()

    def change_method(self, action):
        if action == self.ui.base64:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.cipher = "base64"
        elif action == self.ui.caesar:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.cipher = "caesar"
        elif action == self.ui.vigenere:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.cipher = "vigenere"
        elif action == self.ui.verman:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.cipher = "verman"

    def change_lang_ru(self):
        self.eng = False

    def change_lang_eng(self):
        self.eng = True

    def paste_text(self):
        self.ui.get_text.setText(pyperclip.paste())

    def paste_key(self):
        self.ui.get_key.setText(pyperclip.paste())

    def copy_result(self):
        pyperclip.copy(self.ui.output_text.toPlainText())

    def encrypt_text_with_key(self):
        try:
            if self.cipher == "verman":
                self.result = verman_cipher(self.text, self.key)
            elif self.eng:
                match self.cipher:
                    case "caesar":
                        self.result = eng_caesars_cipher(
                            self.text, self.key, True)
                    case "vigenere":
                        self.result = eng_vigenere_cipher(
                            self.text, self.key, True)
            else:
                match self.cipher:
                    case "caesar":
                        self.result = ru_caesars_cipher(
                            self.text, int(self.key), True)
                    case "vigenere":
                        print(self.cipher)
                        self.result = ru_vigenere_cipher(
                            self.text, self.key, True)

            self.ui.output_text.setText(self.result)
        except:
            dlg = CustomDialog("Ошибка шифрования")
            dlg.exec()

    def encrypt_text_with_no_key(self):
        try:
            if self.eng:
                self.result = base64_encoder(self.text, True)
            else:
                dlg = CustomDialog("В base64 нельзя шифровать на русском")
                dlg.exec()
                return
            self.ui.output_text.setText(self.result)
        except:
            dlg = CustomDialog("Ошибка шифрования")
            dlg.exec()

    def decrypt_text_with_key(self):
        try:
            if self.cipher == "verman":
                self.result = verman_cipher(self.text, self.key)
            elif self.eng:
                match self.cipher:
                    case "caesar":
                        self.result = eng_caesars_cipher(
                            self.text, int(self.key), False)
                    case "vigenere":
                        self.result = eng_vigenere_cipher(
                            self.text, self.key, False)
            else:
                match self.cipher:
                    case "caesar":
                        self.result = ru_caesars_cipher(
                            self.text, int(self.key), False)
                    case "vigenere":
                        self.result = ru_vigenere_cipher(
                            self.text, self.key, False)

            self.ui.output_text.setText(self.result)
        except:
            dlg = CustomDialog("Ошибка шифрования")
            dlg.exec()

    def decrypt_text_with_no_key(self):
        try:
            if self.eng:
                self.result = base64_encoder(self.text, self.key, False)
            else:
                dlg = CustomDialog("В base64 нельзя расшифровывать на русском")
                dlg.exec()
                return
            self.ui.output_text.setText(self.result)
        except:
            dlg = CustomDialog("Ошибка шифрования")
            dlg.exec()

    def save_into_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Text File",
            "document.txt",
            "Text Files (*.txt);;All Files (*)"
        )
        try:
            with open(file_path, "w", encoding="utf-8") as dest:
                dest.write(self.result)
        except:
            dlg = CustomDialog("Выберите путь для файла")
            dlg.exec()
            return

    def change_theme(self, action=0):
        if action == self.ui.light:
            self.setStyleSheet('''
            QMainWindow{
                background-color: #FFFFFF;
                color: #000000;
            }
            QLineEdit{
                background-color: #CDA3FF;
                color: #000000;
                border-radius: 10px;
            }
            QTextEdit{
                background-color: #CDA3FF;
                color: #000000;
                border-radius: 10px;
            }
            QPushButton{
                background-color: #6200EE;
                color: #E7D9D9;
            }
            QMenuBar{
                background-color: #353535;
                color: #F3F2E3
            }
        ''')
            self.ui.get_text.setStyleSheet("border: 1px solid black;")
            self.ui.get_key.setStyleSheet("border: 1px solid black;")
            self.ui.output_text.setStyleSheet("border: 1px solid black;")
        else:
            self.setStyleSheet('''
            QMainWindow{
                background-color: #121212;
                color: #353535;
            }
            QLineEdit{
                background-color: #353535;
                color: #F3F2E3;
                border-radius: 10px;
            }
            QTextEdit{
                background-color: #353535;
                color: #F3F2E3;
                border-radius: 10px;
            }
            QPushButton{
                background-color: #BB86FC;
                color: #353535;
            }
            QMenuBar{
                background-color: #353535;
                color: #F3F2E3
            }
        ''')

    def show_info(self):
        dlg = CustomDialog('''
                           Для вводы текста для зашифровки или расшифровки добавьте
                           его в левое большое поле. Если выбран метод шифрования с
                           ключом(шифр Цезаря выбран по умолчанию), то введите ключ
                           в левое малое поле. После этого нажмите кнопку
                           "Зашифровать" или "Расшифровать", после чего увидите ит-
                           оговый текст в правом поле, из которого вы можете либо 
                           его скопировать большой кнопкой "CTRL+C" или записать в
                           файл с помощью кнопки "Сохранить в файл". Вы можете 
                           выбрать другой шрифт в раскрывающемся меню слева сверху.
                           На выбор есть шифры Цезаря, Виженера, Вернама и BASE64.
                           Также можео изменить исходный язык данных(подменю "Язык")
                           и изменить цветовую тему приложения(подменю тема).
                           ''')
        dlg.exec()


class CustomDialog(QDialog):
    def __init__(self, text):
        super().__init__()

        self.setWindowTitle("ОШИБКА!")

        layout = QVBoxLayout()
        message = QLabel(text)
        layout.addWidget(message)
        self.setLayout(layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
