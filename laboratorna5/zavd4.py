password = input("Введіть пароль: ")
minLength = 8
unmetConditions = ""
def checkLength(password):
    if len(password) < minLength:
        return False
    else:
        return True
def checkNumbers(password):
    global unmetConditions
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in password:
        if i in numbers:
            return True
    unmetConditions += "цифру,"
    return False

def checkLetters(password):
    global unmetConditions
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in password:
        if i in letters:
            return True
    unmetConditions += "малу літеру,"
    return False
def checkCapitalLetters(password):
    global unmetConditions
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in password:
        if i in letters:
            return True
    unmetConditions += "велику літеру,"
    return False
def checkSymbols(password):
    global unmetConditions
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "/", "<", ">", "?", "~"]
    for i in password:
        if i in symbols:
            return True
    unmetConditions += "спеціальний символ,"
    return False
def finalCheck(password):
    if checkLength(password) == True and checkNumbers(password) == True and checkLetters(password) == True and checkCapitalLetters(password) == True and checkSymbols(password) == True:
        print("Пароль надійний")
    else:
        print("Пароль не надійний")
        print(f"Пароль має містити: {unmetConditions[:-1]}")
finalCheck(password)