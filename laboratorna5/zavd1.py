def mainFunction():
    def figureAsk():
        figureName = input("Введіть назву фігури: ")
        figureName = figureName.lower()
        return figureName
    figureName = figureAsk()
    def triangle(a,b,c):
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
    def circle(r):
        s = 3.14 * r * r
        return s
    def square(a, b):
        s = a * b
        return s
    if figureName == "трикутник":
        a = input("Введіть першу сторону: ")
        b = input("Введіть другу сторону: ")
        c = input("Введіть третю сторону: ")
        if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False or int(a) <= 0 or int(b) <= 0 or int(c) <= 0:
            print("Введені дані не є коректними числами!")
            mainFunction()
        else:
            a = int(a)
            b = int(b)
            c = int(c)
            print(f"Площа трикутника: {triangle(a,b,c)}")
    elif figureName == "коло":
        r = input("Введіть радіус кола: ")
        if r.isdigit() == False or int(r) <= 0:
            print("Введені дані не є коректними числами!")
            mainFunction()
        else:
            r = int(r)
            print(f"Площа кола: {circle(r)}")
    elif figureName == "прямокутник":
        a = input("Введіть першу сторону: ")
        b = input("Введіть другу сторону: ")
        if a.isdigit() == False or b.isdigit() == False or int(a) <= 0 or int(b) <= 0:
            print("Введені дані не є коректними числами!")
            mainFunction()
        else:
            a = int(a)
            b = int(b)
            print(f"Площа прямокутника: {square(a,b)}")
    else:
        print("Ця фігура не існує!")
        mainFunction()
mainFunction()