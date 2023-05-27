path = '8_Seminar\\book.txt'

def show_data() -> None:
    """Выводит информацию из справочника"""
    with open(path, 'r', encoding='utf-8') as book:
        print (book.read())
    


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите Ф.И.О.: ')
    adress = input('Введите адрес: ')
    with open(path, 'a', encoding='utf-8') as book:
        book.write(f'{fio} | {adress}\n')
    


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    find_data = input('Что вы хотите найти: ')
    result = search (data, find_data)
    print (result)


def replace_data() -> None:
    """Заменяет информацию в  справочнике."""
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()

    print (numerate (data))
    replace_data = int(input('Введите номер значения, которое вы хотите заменить/удалить: '))
    action = int(input('Что будем делать? (удалить - 1; заменить - 2): '))
    if action == 1:
        data.remove(data[replace_data])
    else:
        data[replace_data] = new_values()
    
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(data)


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return [contact for contact in book if info.lower() in contact.lower()]

#нумерация значений
def numerate (book: list) -> list:
    """Находит в списке записи по определенному критерию поиска"""
    return  list(enumerate(book))

# метод получения новых значений
def new_values ():                                                      
    fio = input('Введите Ф.И.О.: ')
    adress = input('Введите адрес: ')
    return f'{fio} | {adress}\n'

