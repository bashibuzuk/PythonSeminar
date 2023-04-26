Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.    

Задача 25
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам
с помощью постфикса формата _n.

Задача 26:  (рекурсия)
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 

Задача 27
Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите, сколько различных
слов содержится в этом тексте.

Задача 28: (рекусрия)
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
return sum(a, b) + 1 - такое использовать нельзя

*Пример:
2 2
    4

Задача 31. (рекурсия)
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Задача 33. (рекурсия)
Хакер Василий получил доступ к классному журналу
и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия,
но наоборот: все максимальные – на минимальные.
[1, 2, 3, 1, 1, 3, 4, 5, 5, 5] -> [1, 2, 3, 1, 1, 3, 4, 1, 1, 1]

Задача 35. (рекурсия)
Напишите функцию, которая принимает
одно число и проверяет, является ли оно простым

*Напоминание: Простое число - это число,
которое имеет 2 делителя: 1  и n(само число)*
5 -> Yes (имеет делители: 5, 1)
4 -> No (имеет делители: 2, 1, 4)
9 -> No (имеет делители: 1, 3, 9)

Задача 37. (рекурсия)
Дано натуральное число *N* и последовательность
из *N* элементов. Требуется вывести эту последовательность
в обратном порядке.

В программе запрещается объявлять
массивы и использовать циклы (даже для ввода и вывода).
5 | 1 2 3 4 5 -> 5 4 3 2 1

Задача 39. 
Даны два массива чисел. Требуется вывести те уникальные элементы первого массива 
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
Элементы обоих массивов вводятся в две строки через пробел.
Пример:
1 2 3 4 5 6
4 5 6 7 8 -> 1 2 3

Задача 41.
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
определит количество элементов, у которых два соседних и, при этом, оба соседних 
элемента меньше данного. Массив чисел вводится в одну строку через пробел.
Массив состоит из целых чисел.
Пример:
5 1 3 7 9 6 -> 1
3 4 3 6 5 8 7 -> 3

Задача 43 
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что
любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на одной строке через пробел.
1 2 1 3 4 5 3 4 -> 3
1 2 1 3 4 3 1 -> 2

Задача 45 
Два различных натуральных числа n и m называются дружественными, если сумма делителей
числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
Программа получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести
все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод: 1220
Вывод:
220     284
1184    1210