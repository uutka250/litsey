group_info = ('10-IT', '2026/2027')
grade_dict = {
    "Anna": "10 11 12 9 10",
    "Ivan": "8 9 10 11 9",
}
addStudent = input("Введіть ім'я студента: ")
addGrades = input("Введіть оцінки студента: ")
grade_dict[addStudent] = addGrades
midDict = {}
for name in grade_dict:
    mid = 0
    for grade in grade_dict[name].split():
        if (grade_dict[name].split()).length != 5 or int(grade) < 1 or int(grade) > 12:
            print("Дані некоректні")
            exit()
        mid = mid + int(grade)
    mid = mid / 5
    midDict[name] = mid
print(midDict)
print(group_info[0] + " - " + group_info[1])
for name in midDict:
    print(name + " - " + str(midDict[name]))
print(f"Найкращий результат: {max(midDict, key=midDict.get)} - {midDict[max(midDict, key=midDict.get)]}")
