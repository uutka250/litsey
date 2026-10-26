numberList = [12, 3, 4, 14, -12, 5, 10, 16, -4]
posNumbers = []
for i in numberList:
    if i > 0:
        posNumbers.append(i)
print(f"Додатні: {posNumbers}")
negNumbers = []
for i in numberList:
    if i < 0:
        negNumbers.append(i)
print(f"Від'ємні: {negNumbers}")
evenNumbers = []
for i in numberList:
    if i % 2 == 0:
        evenNumbers.append(i)
print(f"Парні: {evenNumbers}")
divBy3 = []
for i in numberList:
    if i % 3 == 0:
        divBy3.append(i)
print(f"Кратні 3: {divBy3}")
minNum = min(numberList)
maxNum = max(numberList)
sumArr = sum(numberList)
avgArr = sumArr / len(numberList)
print(f"Min: {minNum}, Max: {maxNum}, Sum: {sumArr}, Average: {avgArr}")