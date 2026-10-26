# Я так зрозумів що дані не мають тут поступати через input, бо дві константи перетворити зі строки в одну змінну майже неможливо
group1 = {'Anna','Ivan','Olha'}
group2 = {'Ivan','Maksym','Olha'}
print(f"Спільні: {group1 & group2}")
print(f"Тільки group1: {group1 - group2}")
print(f"Тільки group2: {group2 - group1}")
print(f"Усі: {group1 | group2}")