# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. 
# Выведите минимальное количество монет, 
# которые нужно перевернуть. С клавиатуры вводятся число монет 
# и сами монеты построчно.

# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

# from random import randint

# count_of_coin = int(input("Введите число монеток: "))
# count_of_reshka = 0

# for i in range(count_of_coin):
#     side_of_coin = randint(0,1)
#     if side_of_coin != 1:
#         count_of_reshka += 1
# print(f'Количество монеток, которые надо перевернуть: {count_of_reshka}')

n = int(input("Введите количество монеток: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("Введите 0 и 1: "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
