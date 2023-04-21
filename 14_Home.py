# Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

any_number = int(input("Введите любое число: "))

i = 0
result = 0
while result < any_number:
    result = 2 ** i
    if result < any_number:
        i += 1
        print (result)
    else:
        break