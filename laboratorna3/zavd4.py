n = input("Введіть фразу: ")
n = n.lower()
n = n.split()
changeWord = input("Введіть слово, яке замінити: ")
changeToWord = input("Введіть слово, на яке замінити: ")
changeWord = changeWord.lower()
changeToWord = changeToWord.lower()
largestWord = n[0]
smallestWord = n[0]
uniqueWords = []
uniqueWords.append(n[0])
finalString = ""
print(n)
for i in n:
    if len(largestWord) < len(i):
        largestWord = i
    if len(smallestWord) > len(i):
        smallestWord = i
    if i not in uniqueWords:
        uniqueWords.append(i)
    if i == changeWord:
        n[n.index(i)] = changeToWord
finalString = " ".join(n)
print(f"Найдовше слово: {largestWord}")
print(f"Найменше слово: {smallestWord}")
print(f"Унікальні слова: {uniqueWords}")
print(finalString)
