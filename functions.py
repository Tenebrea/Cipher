import base64


def caesars_cipher(line: str, step: int, encrypt=True) -> str:
    keys_numbers = {
        1: "А",  2: "Б",  3: "В",  4: "Г",  5: "Д",  6: "Е",
        7: "Ё",  8: "Ж",  9: "З", 10: "И", 11: "Й", 12: "К",
        13: "Л", 14: "М", 15: "Н", 16: "О", 17: "П", 18: "Р",
        19: "С", 20: "Т", 21: "У", 22: "Ф", 23: "Х", 24: "Ц",
        25: "Ч", 26: "Ш", 27: "Щ", 28: "Ъ", 29: "Ы", 30: "Ь",
        31: "Э", 32: "Ю", 33: "Я"
    }
    keys_letters = {
        "А": 1,  "Б": 2,  "В": 3,  "Г": 4,  "Д": 5,  "Е": 6,
        "Ё": 7,  "Ж": 8,  "З": 9,  "И": 10, "Й": 11, "К": 12,
        "Л": 13, "М": 14, "Н": 15, "О": 16, "П": 17, "Р": 18,
        "С": 19, "Т": 20, "У": 21, "Ф": 22, "Х": 23, "Ц": 24,
        "Ч": 25, "Ш": 26, "Щ": 27, "Ъ": 28, "Ы": 29, "Ь": 30,
        "Э": 31, "Ю": 32, "Я": 33
    }
    ans = ""
    step %= 33
    if encrypt == False:
        step = -step

    for i in line:
        if i.upper() in keys_numbers.values():
            if i.isupper():
                ans += keys_numbers[keys_letters[i]+step]
            else:
                ans += keys_numbers[keys_letters[i.upper()]+step].lower()
        else:
            ans += i
    return ans


def verman_cipher(line: str, key: str) -> str:
    if len(line) > len(key):
        key += "o"*(len(line)-len(key))
    return ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(line, key))


def vigenere_cipher(line: str, key: str, encrypt=True) -> str:
    key = key*(len(line)//len(key)) + key[:len(line) % len(key)]
    text = []
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


def eng_caesars_cipher(line: str, step: int, encrypt=True) -> str:
    keys_numbers = {
        1: "A",  2: "B",  3: "C",  4: "D",  5: "E",  6: "F",
        7: "G",  8: "H",  9: "I", 10: "J", 11: "K", 12: "L",
        13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
        19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X",
        25: "Y", 26: "Z"
    }
    keys_letters = {
        "A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,  "F": 6,
        "G": 7,  "H": 8,  "I": 9,  "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
        "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24,
        "Y": 25, "Z": 26
    }
    ans = ""
    step %= 26
    if encrypt == False:
        step = -step

    for i in line:
        if i.upper() in keys_numbers.values():
            if i.isupper():
                ans += keys_numbers[keys_letters[i]+step]
            else:
                ans += keys_numbers[keys_letters[i.upper()]+step].lower()
        else:
            ans += i
    return ans


def eng_vigenere_cipher(line: str, key: str, encrypt=True) -> str:
    key = key*(len(line)//len(key)) + key[:len(line) % len(key)]
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
