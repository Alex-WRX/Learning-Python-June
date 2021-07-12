from random import randint

first_list = [randint(0, 999) for _ in range(0, randint(3, 25))]
second_list = [num for i, num in enumerate(first_list[1:]) if num > first_list[i]]

print(first_list)
print(second_list)