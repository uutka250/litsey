N = input("Введіть число: ")
N = int(N)
sumRange = 0
numCount = 0
for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:
        numCount = numCount + 1
        sumRange = sumRange + i

if(numCount == 0):
    exit()
print(f"Кількість чисел: {numCount}")
print(f"Сума чисел: {sumRange}")
print(f"Середнє арифметичне: {sumRange/numCount}")

