def caesars_cipher(line:str, step:int, decipher = False)->str:
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
    step%=33
    if decipher==True:
        step=-step
    
    for i in line:
        if i.upper() in keys_numbers.values():
            if i.isupper():
                ans+=keys_numbers[keys_letters[i]+step]
            else:
                ans+=keys_numbers[keys_letters[i.upper()]+step].lower()
        else:
            ans+=i
    return ans

def base64_cipher(line:str)->str:
    def binaryTodecimal(n):
        decimal = 0
        power = 1
        while n>0:
            rem = n%10
            n = n//10
            decimal += rem*power
            power = power*2
            
        return decimal
    
    base64 = {
     0: "A",  1: "B",  2: "C",  3: "D",  4: "E",  5: "F",
     6: "G",  7: "H",  8: "I",  9: "J", 10: "K", 11: "L",
    12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R",
    18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
    24: "Y", 25: "Z",
    26: "a", 27: "b", 28: "c", 29: "d", 30: "e", 31: "f",
    32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l",
    38: "m", 39: "n", 40: "o", 41: "p", 42: "q", 43: "r",
    44: "s", 45: "t", 46: "u", 47: "v", 48: "w", 49: "x",
    50: "y", 51: "z",
    52: "0", 53: "1", 54: "2", 55: "3", 56: "4", 57: "5",
    58: "6", 59: "7", 60: "8", 61: "9",
    62: "+", 63: "/"
}
    ans = ""
    to_convert = ""
    for i in line:
        if i in base64.values():
           to_convert+=str(bin(ord(i))) 
        else:
            return "Нельзя конвертировать в base64"
    to_convert=to_convert.replace("b","")
    if len(to_convert)%6==0:
        for i in range(0,len(line)):
            ans+=base64[binaryTodecimal(int(to_convert[i:i+5]))]
    else:
        to_convert+=len(to_convert)%6*"0"
        for i in range(0,len(line)):
            ans+=base64[binaryTodecimal(int(to_convert[i:i+5]))]
    return ans

print(base64_cipher('Logto'))






