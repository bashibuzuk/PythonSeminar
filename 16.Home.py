# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


import random

count_of_number = int(input('Введите длинну массива: '))
find_number = int(input("Какое число будем искать: "))

count = 0
list = []

for i in range(count_of_number):
    list.append(random.randint(1,10))
    if list[i] == find_number:
        count +=1

print(list)
print(count)  