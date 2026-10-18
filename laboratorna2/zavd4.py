width = input("Введіть ширину: ")
height = input("Введіть висоту: ")
outsideSymbol = input("Введіть символ: ")
insideSymbol = input("Введіть символ всередині: ")
width = int(width)
height = int(height)
for i in range(width):
    if i == 0 or i == width - 1:
        print(outsideSymbol * width)
    else:
        print(outsideSymbol + insideSymbol * (width - 2) + outsideSymbol)