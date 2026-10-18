a = input("Введіть першу сторону:")
b = input("Введіть другу сторону:")
c = input("Введіть третю сторону:")
if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False:
    print("Введені дані не є коректними числами!")
    exit()
a = int(a)
b = int(b)
c = int(c)
valid = False
if a + b > c and b + c > a and c + a > b and a > 0 and b > 0 and c > 0:
    print("Трикутник існує")
    valid = True
else:
    print("Цей трикутник неможливий, перевірте введені дані!")
    exit()
if valid:
    if a == b == c:
        print("Рівносторонній")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Прямокутний")
    elif a == b or b == c or c == a:
        print("Рівнобедрений")
    else:
        print("Різносторонній")