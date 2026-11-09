grades = [10,8,12,9,11]
passingGrade = 9
def average(grades):
    sum = 0
    for i in range(len(grades)):
        sum = sum + grades[i]
    return round(sum/len(grades))
def min_grade(grades):
    min = grades[0]
    for i in range(len(grades)):
        if min > grades[i]:
            min = grades[i]
    return min
def max_grade(grades):
    max = grades[0]
    for i in range(len(grades)):
        if max < grades[i]:
            max = grades[i]
    return max
def higherThanPassing(grades):
    count = 0
    for i in range(len(grades)):
        if grades[i] > passingGrade:
            count = count + 1
    return count
print(f"Середній бал: {average(grades)}")
print(f"Мінімальна: {min_grade(grades)}")
print(f"Максимальна: {max_grade(grades)}")
print(f"Вище {passingGrade}:{higherThanPassing(grades)}")