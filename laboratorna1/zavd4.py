fares = input("Введіть кількість поїздок: ")
packFareCount = input("Введіть кількість білетів у пачці квитків: ")
singleFareCost = input("Введіть вартість одного квитка: ")
packFareCost = input("Введіть вартість пачки квитків: ")
totalCost = 0
fares = int(fares)
packFareCount = int(packFareCount)
singleFareCost = int(singleFareCost)
packFareCost = int(packFareCost)
if fares > 10000 or packFareCount > 10000 or singleFareCost > 10000 or packFareCost > 10000:
    print("Введені дані не є коректними!")
    exit()
while fares - packFareCount >= 0:
    totalCost += packFareCost
    fares -= packFareCount
if fares * singleFareCost > packFareCost:
    totalCost += packFareCost
else:
    totalCost += fares * singleFareCost
print(f"Загальна вартість: {totalCost}")