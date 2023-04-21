# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь 
# в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X . Если таких значений больше одного, 
# вывести первый найденный.

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

count_of_number = int(input('Введите длинну массива: '))
find_number = int(input("С каим числом будеи сравнивать. Число должно быть больше 10: "))

count = find_number
list = []
number = 0

for i in range(count_of_number):
    list.append(random.randint(1,10))
    if (find_number - list[i]) < count:
        count = find_number - list[i]
        number = list[i]

print(list)
print(number) 