n = input("Введіть ПІБ: ")
n = n.lower()
n = n.title()
n = n.split()
final = n[0] + " " + n[1][0] + "." + n[2][0] + "."
print(final)