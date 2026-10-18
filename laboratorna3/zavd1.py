n = input("Введіть фразу: ")
symbols = len(n)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдееєжзиіїйклмнопрстуфхцчшщьыюяАБВГДЕЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯ"
numbers = "0123456789"
vowels = "aeiouAEIOUаеєиіїоуюяАЕЄІІЗОУЮЯ"
vowelsCount = 0
numberCount = 0
letterCount = 0
spaces = n.count(" ")
for char in n:
    if char in letters:
        letterCount = letterCount + 1
    if char in numbers:
        numberCount = numberCount + 1
    if char in vowels:
        vowelsCount = vowelsCount + 1
print(f"Кількість символів: {symbols}")
print(f"Кількість букв: {letterCount}")
print(f"Кількість цифр: {numberCount}")
print(f"Кількість пробілів: {spaces}")
print(f"Кількість голосних: {vowelsCount}")
print(f"Кількість слів: {len(n.split())}")