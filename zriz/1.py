numbers = [];
for i in range(5):
    user_input = input(f"Введіть число {i + 1}:");
    if str(user_input).lstrip('-').isdigit() == True:
        numbers.append(int(user_input));
    else:
        print("Введені дані не є числом!");
        exit();
number = numbers[0];
for i in numbers:
    if i > number:
        number = i;
print(f"Найбільше число або цифра: {number}:");
for i in numbers:
    if i < number:
        number = i;
print(f"Найменше число або цифра: {number}:");