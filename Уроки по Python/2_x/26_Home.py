# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 



def stepen(number1, number2):
    if number2 == 1:
        return number1
    return number1 * stepen(number1, number2-1)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print (stepen(number1, number2))

