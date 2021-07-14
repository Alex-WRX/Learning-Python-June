rus_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open ('task_4.txt', 'w', encoding='utf-8') as new_file:
    with open ('task_4.txt', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_trans.get(line.split()[0])) for line in my_file])