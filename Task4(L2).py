my_str = input('Введите слова ')
my_sep = my_str.split()
number = 0
for el in my_sep:
    number += 1
    print(f'{number}: {el[:10]}')