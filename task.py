# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя
# print('1 - вывести все контакты \n ')
# print('2 - поиск контакта\n ')
# print('3 - добавить контакт\n ')
# print('4 - изменить данные контакта\n ')
# print('5 - удалить контакт\n ')
# print('6 - выход\n ')
def print_menu():
    print("""  
    ------------------------------\n
    1 - вывести все контакты \n 
    2 - поиск контакта\n  
    3 - добавить контакт\n 
    4 - изменить данные контакта\n 
    5 - удалить контакт\n 
    6 - выход\n 
    ------------------------------\n
     """)

def addition ():
    with open(file_path, 'a', encoding='utf8') as open_book:
        add_n1 = (input('Введите фамилию: ' ).title())
        add_n2 = (input('Введите Имя: ' ).title())
        add_n3 = input('Введите телефон: ' )
        new_line = add_n1 +' '+add_n2 +' '+ add_n3 
        open_book.writelines(f'\n{new_line}')
        print(new_line)

def search():
    with open(file_path, 'r', encoding='utf8') as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if seach_param in line:
                print(line)

def delete(l):
    delet_param = (input('Введите контакт удаления: ' ).title())
    with open (file_path, 'w', encoding='utf8') as open_book:
        for line in l:
            if delet_param not in line:
               open_book.writelines(line)

def edit(l):
    seach_param = (input('Введите параметр для поиска: ' ).title())
    with open (file_path, 'w', encoding='utf8') as open_book:
        for line in l:
            print(line)
            if seach_param in line:
                line = line.replace(seach_param, (input('Новые данные контакта: ').title()))
            open_book.writelines(line)

def read_all():
    with open(file_path, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  

def read():
    return open(file_path, 'r', encoding='utf8').readlines()

def tasks(task):
   if task > 6: print('Вы ошиблись')
   if task == 6: print('До свидания!')
   else:
    match task:
        case 1: #  вывести все контакты
            read_all()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))  
        case 2: # поиск контактов
            search()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 3: # добавить контакт
            addition ()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 4: # изменить контакт
            edit(read())
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 5: # удалить контакт
            delete(read())
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))            
        case _:
            print('введите значение из меню: ')
            tasks(int(input('Введите номер задачи от 1 до 6: '))) 
file_path = 'phone_book.txt'             
print_menu()
tasks(int(input('Введите номер задачи от 1 до 6: ')))

