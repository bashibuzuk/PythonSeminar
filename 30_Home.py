# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

array_first = int(input('Введите первый элемент массива: '))
array_difference = int(input('Введите разность между элементами массива: '))
array_count = int(input('Введите количество элементов  массива: '))

array = []

for i in range(array_count):
    array.append(array_first + i * array_difference)

print(array)

