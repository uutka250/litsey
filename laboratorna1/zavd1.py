number = input("Введіть число: ")
number = int(number)
if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
age = input("Введіть вік: ")
age = int(age)
if age >= 18:
    print("Ви повнолітні!")
else:
    print("Ви неповнолітній!")
radius = input("Введіть радіус кола: ")
radius = int(radius)
area = 3.14 * radius ** 2
length = 2 * 3.14 * radius
print(f"Площа кола: {area}")
print(f"Довжина кола: {length}")
firstn = input("Введіть перше число: ")
secondn = input("Введіть друге число: ")
firstn = int(firstn)
secondn = int(secondn)
if firstn > secondn:
    print("Перше число більше")
elif firstn == secondn:
    print("Числа рівні")
else:
    print("Друге число більше")
