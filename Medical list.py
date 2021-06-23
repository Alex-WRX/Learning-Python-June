name = input('Введите имя и фамилию ')
print('Имя Фамилия', name)
age = int(input('Введите возраст '))
print('Возраст', age)
weight = int(input('Введите вес '))
print('Вес', weight)
if age < 30 and 50 < weight < 120:
    print('Пациент в хорошем состоянии')
if 30 < age < 40 and (50 < weight or 120 > weight):
    print('Пациенту следует заняться собой')
if age > 40 and (50 < weight or 120 > weight):
    print('Пациенту требуется врачебный осмотр')
