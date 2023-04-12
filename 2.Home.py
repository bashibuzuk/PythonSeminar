# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

x_number = int(input("Введите 3-х значное число: "))

f_number = x_number%10
s_number = (x_number//10)%10
th_number = x_number//100

summ = f_number + s_number + th_number

print(summ)