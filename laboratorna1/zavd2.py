coords = input("Введіть координати: ").split()
x = int(coords[0])
y = int(coords[1])
if x > 0 and y > 0:
    print("Перша чверть")
elif x < 0 and y > 0:
    print("Друга чверть")
elif x < 0 and y < 0:
    print("Третя чверть")
elif x == 0 and y != 0:
    print("Точка на осі Оу")
elif y == 0 and x != 0:
    print("Точка на осі Ох")
elif x == 0 and y == 0:
    print("Точка в центрі декратової площини")
else:
    print("Четверта чверть")