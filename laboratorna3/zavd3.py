n = input("Введіть перше слово: ")
m = input("Введіть друге слово: ")
n.lower()
m.lower()

anagram = True
for char in n:
    if char in m:
        print(char)
    else:
        if char == " ":
            continue
        else:
            anagram = False
            break
if anagram:
    print("Це анаграма")
else:
    print("Це не анаграма")