N = input("Введіть число: ")
N = int(N)
if N <= 0:
    print("Введені дані не є коректними!")
    exit()
digitCount = 0
digits = []
digitSum = 0
while N != 0:
    if digits == []:
        digits.append(N % 10)
    else:
        N = N//10
        print(N)
        digits.append(N % 10)
        digitCount = digitCount + 1
digits.pop()
digits.reverse()
biggestNum = max(digits)
smallestNum = min(digits)
for i in digits:
    digitSum = digitSum + i
print(f"Кількість цифр: {digitCount}")
print(f"Послідовність цифр: {digits}")
print(f"Сума цифр: {digitSum}")
print(f"Наибільша цифра: {biggestNum}")
print(f"Найменша цифра: {smallestNum}")