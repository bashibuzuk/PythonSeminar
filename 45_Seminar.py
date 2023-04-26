# Задача 45 
# Два различных натуральных числа n и m называются дружественными, если сумма делителей
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: 1220
# Вывод:
# 220     284
# 1184    1210


def find_div_sum(num: int) -> int:
    div_sum = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            div_sum += i
    return div_sum


k = int(input())
result = []
for i in range(k):
    second = find_div_sum(i)
    first = find_div_sum(second)
    if i == first and i != second:
        if (second, i) not in result:
            result.append((i, second))
print(result)