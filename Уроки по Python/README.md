Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.    

**Задача 25**
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам
с помощью постфикса формата _n.

**Задача 26:  (рекурсия)**
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 

**Задача 27**
Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите, сколько различных
слов содержится в этом тексте.

**Задача 28: (рекусрия)**
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
return sum(a, b) + 1 - такое использовать нельзя

*Пример:
2 2
    4

**Задача 30:**  
Заполните массив элементами арифметической прогрессии. 
Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Input:
1 - a1
2 - d
5 - n
Output:
1, 3, 5, 7, 9

**Задача 31. (рекурсия)**
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

**Задача 32:** 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

Input:
1, 3, 7, 10, 5, 8 - рассматриваемый список
4 - начало диапазона
8 - конец
Output:
2(7), 4(5), 5(8)

**Задача 33. (рекурсия)**
Хакер Василий получил доступ к классному журналу
и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия,
но наоборот: все максимальные – на минимальные.
[1, 2, 3, 1, 1, 3, 4, 5, 5, 5] -> [1, 2, 3, 1, 1, 3, 4, 1, 1, 1]

**Задача 34 (7 домашка):**
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова. 
Если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
     **Вывод:** Парам пам-пам 

**Задача 35. (рекурсия)**
Напишите функцию, которая принимает
одно число и проверяет, является ли оно простым

*Напоминание: Простое число - это число,
которое имеет 2 делителя: 1  и n(само число)*
5 -> Yes (имеет делители: 5, 1)
4 -> No (имеет делители: 2, 1, 4)
9 -> No (имеет делители: 1, 3, 9)

**Задача 36 (7 домашка)**
На вход программы поступает строка в формате:
ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.

Sample Input:
house=дом car=машина men=человек tree=дерево
Sample Output:
(('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))

**Задача 36 (7 домашка) Дополнительное** 
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, 
у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*
Ввод: `print_operation_table(lambda x, y: x * y) ` 
Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36

**Задача 37. (рекурсия) -->**
Дано натуральное число *N* и последовательность
из *N* элементов. Требуется вывести эту последовательность
в обратном порядке.

В программе запрещается объявлять
массивы и использовать циклы (даже для ввода и вывода).
5 | 1 2 3 4 5 -> 5 4 3 2 1

**Задача 39.** 
Даны два массива чисел. Требуется вывести те уникальные элементы первого массива 
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
Элементы обоих массивов вводятся в две строки через пробел.
Пример:
1 2 3 4 5 6
4 5 6 7 8 -> 1 2 3

**Задача 41.**
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
определит количество элементов, у которых два соседних и, при этом, оба соседних 
элемента меньше данного. Массив чисел вводится в одну строку через пробел.
Массив состоит из целых чисел.
Пример:
5 1 3 7 9 6 -> 1
3 4 3 6 5 8 7 -> 3

**Задача 43**
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что
любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на одной строке через пробел.
1 2 1 3 4 5 3 4 -> 3
1 2 1 3 4 3 1 -> 2

**Задача 45**
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

**Задача 47 (7 семинар)**
У вас есть код, который вы не можете менять
(так часто бывает, когда код в глубине программы используется 
множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом
- посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак
преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation,
чтобы transformed_values получился копией values.

**Задача 49 (7 семинар).** 
Планеты вращаются вокруг звезд по эллиптическим
орбитам. Назовем самой далекой планетой ту, орбита
которой имеет самую большую площадь.
Напишите функцию find_farthest_orbit(list_of_orbits),
которая среди списка орбит планет найдет ту, по которой
вращается самая далекая планета. Круговые орбиты не учитывайте:
вы знаете, что у вашей звезды таких планет нет, зато
искусственные спутники были были запущены на круговые орбиты.
Результатом функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита представляет из
себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется
по формуле S = piab, где a и b - длины полуосей эллипса.
 При решении задачи используйте списочные
выражения. Подсказка: проще всего будет найти эллипс в два шага:
сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
Гарантируется, что самая далекая планета ровно одна
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Вывод:
2.5 10

**Задача 51 (7 семинар)**
Напишите функцию same_by(characteristic, objects),
которая проверяет, все ли объекты имеют одинаковое
значение некоторой характеристики, и возвращают True,
если это так. Если значение характеристики для разных
объектов отличается - то False. Для пустого набора объектов,
функция должна возвращать True. Аргумент characteristic
- это функция, которая принимает объект и вычисляет его характеристику.
В качестве примера характеристики можно взять проверку
четности из лекции, а можно придумать свою.

# Задача №55 (8 семинар/дз).  
Создать телефонный справочник с возможностью импорта
и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные,
которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для
поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной