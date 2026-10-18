age = input("Введіть вік: ")
age = int(age)
if age >= 120 or age <= 0 or age % 1 != 0:
    print("Введені дані не є коректними!")
    exit()
last_digit = age % 10
if age < 20 and age > 10:
    print(f"Вам {age} років")
elif last_digit == 0:
    print(f"Вам {age} років")
elif last_digit == 1:
    print(f"Вам {age} рік")
elif last_digit > 1 and last_digit < 5:
    print(f"Вам {age} роки")
else:
    print(f"Вам {age} років")