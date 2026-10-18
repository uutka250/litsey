# Не судіть строго, я робив цей код о 12 ночі
N = input("Введіть число: ")
N = int(N)
correctDigits = []
makeDigTogether = 0
iter = 0
multiDig = False
if N <= 0:
    print("Введені дані не є коректними!")
    exit()
for i in range(1, N + 1):
    multiDig = False
    makeDigTogether = 0
    digits = []
    while i != 0:
        if digits == []:
            digits.append(i % 10)
        else:
            i = i//10
            print(i)
            digits.append(i % 10)
    digits.pop()
    digits.reverse()
    if len(digits) > 1:
        for b in digits:
            if iter == 0:
                makeDigTogether = makeDigTogether + b
                iter = iter + 1
            else:
                print(makeDigTogether)
                print(b)
                makeDigTogether = int(str(makeDigTogether) + str(b))
                print(f"Число: {makeDigTogether}")
                multiDig = True
                iter = 0
    for c in digits:
        print(multiDig)
        if c != 0:
            if multiDig == False:
                correctDigits.append(c)
            else:
                for d in digits:
                    trueNumber = True
                    if  d == 0:
                        trueNumber = False
                    else:
                        if makeDigTogether % d != 0:
                            trueNumber = False
                if trueNumber == True:
                    print(f"Число додати: {makeDigTogether}")
                    correctDigits.append(makeDigTogether)
                    break

print(f"Послідовність цифр: {correctDigits}")