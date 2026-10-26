productsDict = {
    "apple": 10,
    "banana": 5,
    "orange": 15,
    "milk": 20,
    "bread": 8
}
product = input("Введіть продукт: ")
product = product.lower()
price = input("Введіть ціну: ")
price = int(price)
productsDict[product] = price
print(productsDict)
searchProduct = input("Введіть продукт, який хочете знайти: ")
searchProduct = searchProduct.lower()
if productsDict.get(searchProduct) != None:
    print(f"Ціна {searchProduct}: {productsDict[searchProduct]}")
else:
    print("Такого продукту не існує!")
smallPrice = input("Введіть мінімальну ціну: ")
highestPrice = input("Введіть максимальну ціну: ")
priceRange = range(int(smallPrice), int(highestPrice) + 1)
for product in productsDict:
    if productsDict[product] in priceRange:
        print(f"{product} - {productsDict[product]}")

