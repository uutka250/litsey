N = input("Введіть число: ")
N = int(N)
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "ні"
    return "так"
def dividers(n):
    dividers = []
    for i in range(1, n + 1):
        if n % i == 0:
            dividers.append(i)
    return dividers
def sumOfDigits(n):
    sum = 0
    while n != 0:
        sum = sum + n % 10
        n = n//10
    return sum
print(f"Просте число: {is_prime(N)}")
print(f"Дільники: {dividers(N)}")
print(f"Сума цифр: {sumOfDigits(N)}")