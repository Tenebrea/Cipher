import base64


def ru_caesars_cipher(line: str, key: int, encrypt=True) -> str:
    keys_numbers = [
        "А", "Б", "В", "Г", "Д", "Е",
        "Ё", "Ж", "З", "И", "Й", "К",
        "Л", "М", "Н", "О", "П", "Р",
        "С", "Т", "У", "Ф", "Х", "Ц",
        "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь",
        "Э", "Ю", "Я"
    ]
    keys_letters = {
        "А": 1,  "Б": 2,  "В": 3,  "Г": 4,  "Д": 5,  "Е": 6,
        "Ё": 7,  "Ж": 8,  "З": 9,  "И": 10, "Й": 11, "К": 12,
        "Л": 13, "М": 14, "Н": 15, "О": 16, "П": 17, "Р": 18,
        "С": 19, "Т": 20, "У": 21, "Ф": 22, "Х": 23, "Ц": 24,
        "Ч": 25, "Ш": 26, "Щ": 27, "Ъ": 28, "Ы": 29, "Ь": 30,
        "Э": 31, "Ю": 32, "Я": 33
    }
    ans = ""

    if encrypt == False:
        key = -key

    if key < 0:
        key = -(-key % 33)
    else:
        key %= 33

    for i in line:
        if i.upper() in keys_letters.keys():
            if keys_letters[i.upper()]+key-1 > 33:
                local_key = (keys_letters[i.upper()]+key-1) % 33
            else:
                local_key = keys_letters[i.upper()]+key-1

            if i.isupper():
                ans += keys_numbers[local_key]
            else:
                ans += keys_numbers[local_key].lower()
        else:
            ans += i
    return ans


def verman_cipher(line: str, key: str) -> str:
    line_bytes = line.encode('utf-8')
    key_bytes = key.encode('utf-8')

    key_bytes = (key_bytes * (len(line_bytes) // len(key_bytes))) + key_bytes[:len(line_bytes) % len(key_bytes)]
    
    cipher_bytes = bytes([b1 ^ b2 for b1, b2 in zip(line_bytes, key_bytes)])
  
    return cipher_bytes.decode('utf-8', errors='ignore')



def ru_vigenere_cipher(line: str, key: str, encrypt=True) -> str:
    if key == "":
        return ""
    key = key*(len(line)//len(key)) + key[:len(line) % len(key)]
    text = []
    if len(key) < 2:
        raise ValueError
    if encrypt:
        for i in range(len(line)):
            char = line[i]
            if char.isupper() and char != "Ё":
                encrypted_char = chr(
                    (ord(char) + ord(key[i]) - 2 * ord('А')) % 32 + ord('А'))
            elif char.islower() and char != "ё":
                encrypted_char = chr(
                    (ord(char) + ord(key[i]) - 2 * ord('а')) % 32 + ord('а'))
            else:
                encrypted_char = char
            text.append(encrypted_char)
        return "".join(text)
    else:
        for i in range(len(line)):
            char = line[i]
            if char.isupper() and char != "Ё":
                decrypted_char = chr(
                    (ord(char) - ord(key[i]) + 32) % 32 + ord('А'))
            elif char.islower() and char != "ё":
                decrypted_char = chr(
                    (ord(char) - ord(key[i]) + 32) % 32 + ord('а'))
            else:
                decrypted_char = char
            text.append(decrypted_char)
        return "".join(text)

# Английские шифры


def eng_caesars_cipher(line: str, key: int, encrypt=True) -> str:
    keys_numbers = [
        "A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y", "Z"
    ]
    keys_letters = {
        "A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,  "F": 6,
        "G": 7,  "H": 8,  "I": 9,  "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
        "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24,
        "Y": 25, "Z": 26
    }

    ans = ""

    if encrypt == False:
        key = -key

    if key < 0:
        key = -(-key % 26)
    else:
        key %= 26

    for i in line:
        if i.upper() in keys_letters.keys():
            if keys_letters[i.upper()]+key-1 > 26:
                local_key = (keys_letters[i.upper()]+key-1) % 26
            else:
                local_key = keys_letters[i.upper()]+key-1

            if i.isupper():
                ans += keys_numbers[local_key]
            else:
                ans += keys_numbers[local_key].lower()
        else:
            ans += i
    return ans


def eng_vigenere_cipher(line: str, key: str, encrypt=True) -> str:
    if key == "":
        return ""
    key = key*(len(line)//len(key)) + key[:len(line) % len(key)]
    if len(key) < 2:
        raise ValueError
    text = []
    if encrypt:
        for i in range(len(line)):
            char = line[i]
            if char.isupper():
                encrypted_char = chr(
                    (ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
            elif char.islower():
                encrypted_char = chr(
                    (ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
            else:
                encrypted_char = char
            text.append(encrypted_char)
        return "".join(text)
    else:
        for i in range(len(line)):
            char = line[i]
            if char.isupper():
                decrypted_char = chr(
                    (ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
            elif char.islower():
                decrypted_char = chr(
                    (ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
            else:
                decrypted_char = char
            text.append(decrypted_char)
        return "".join(text)


def base64_encoder(line: str, encrypt=True) -> str:
    if encrypt:
        try:
            return base64.b64encode(line.encode("ascii")).decode("ascii")
        except:
            return "Это не Base64"
    else:
        try:
            return base64.b64decode(line.encode("ascii")).decode("ascii")
        except:
            return "Это не Base64"

