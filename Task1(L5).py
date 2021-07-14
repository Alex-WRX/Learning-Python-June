print('ВВедите данные для создания файла \nДля окончания ввода введите пустую строку')
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while (line :=input()) != ' ':
        my_file.write(f"{line}\n")
