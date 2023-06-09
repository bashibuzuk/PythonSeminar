# Задача 36:

# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.

# Sample Input:
# house=дом car=машина men=человек tree=дерево

# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))

input_string = 'house=дом car=машина men=человек tree=дерево'
modern_list = input_string.split()

def result(x):
    return tuple(x.split('='))

print(tuple(map(result , modern_list)))

print(tuple(map(lambda x: tuple(x.split('=')), modern_list)))
