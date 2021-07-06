my_list = [2, 4, 8, 6, 12, 12, 4, 65]
new_number = int(input("Введите новое число: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)