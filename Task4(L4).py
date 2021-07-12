from random import randint

my_list = [randint(-20, 20) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) ==1]
print(my_list)
print(uniq_list)
