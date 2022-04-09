# Декоратор - таймер
from functools import wraps
from time import time


def timer(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Функция {func.__name__} с аргументом/и {args}, - завершилась за: {end_ if end_ > 0 else 0} ms")
    return _time_it

"""
Задача 1
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""
@timer
def sum_3_5_multiples_numbers(n):
    return sum([a for a in range(n) if a % 3 == 0 or a % 5 == 0])
# print(sum_3_5_multiples_numbers(1000))

"""
Задача 2
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
@timer
def sum_fib_even(n):
    i1 = 1
    i2 = 2
    res = 0
    while i2 < n:
        i3 = i1 + i2
        if i2 % 2 == 0:
            res += i2
        i1, i2 = i2, i3
    return res
# print(sum_fib_even(4000000))

"""
Задача 3
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""
@timer
def biggest_simple_divisor(n):
    square_root = int(n**0.5)
    for i in range(square_root, 0, -1):
        if n % i == 0:
            if i > 3:
                flag = True
                for k in range(2, i):
                    if i % k == 0:
                        flag = False
                        continue
                if flag:
                    return i
# print(biggest_simple_divisor(600851475143))

"""
Задача 4
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""
@timer
def biggest_palindrome(n:int):  # n - разрядность чисел
    list_palindrome = []
    n1, n2 = int(n * "9"), int(n * "9")
    for i in range(n1, 0, -1):
        for k in range(n2, 0, -1):
            if str(i*k) == str(i*k)[::-1]:
                list_palindrome.append(i*k)
    return max(list_palindrome)
# print(biggest_palindrome(3))

"""
Задача 5
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

def sieve_of_Eratosthenes(n:int) -> list:
    lst = list(range(2, n + 1))
    i, k = 0, 0
    sqrt_n = int(n**0.5) + 1
    while sqrt_n >= k:
        k = lst[i]
        lst = [x for x in lst if x % k != 0]
        lst.insert(i, k)
        i += 1
    return lst


def is_prime(n):
    if n in (1, 2, 3):
        return True
    if n % 2 == 0:
        return False
    for k in range(3, int(n**0.5)+1, 2):
        if n % k == 0:
            return False
    else:
        return True
def multiply(lst):
    res = 1
    for elem in lst:
        res *= elem
    return res

@timer
def smallest_multiple_number(n):
    list_simple_numbers = [x for x in range(1, n+1) if is_prime(x)]
    step = multiply(list_simple_numbers)
    res = 0
    while res <= multiply(list(range(1, n+1))):
        res += step
        if all([res % x == 0 for x in list(range(1, n+1))]):
            return res

# Удивительная разница во времени расчётах между числом 120 и 130 для этой функции
# print(smallest_multiple_number(20))

"""
Задача 6
Сумма квадратов первых десяти натуральных чисел равна
1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен
(1 + 2 + ... + 10)^2 = 552 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти 
натуральных чисел составляет 3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
"""
@timer
def difference_of_squares(n):
    return sum(list(range(n + 1)))**2 - sum([x**2 for x in range(n + 1)])
# print(difference_of_squares(100))

"""
Задача 7
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?
"""
@timer
def primary_10001(n):
    number = 2
    number_primary = 0
    while True:
        if is_prime(number):
            number_primary += 1
            if number_primary == n:
                return number
        number += 1
# print(primary_10001(10001))

"""
Задача 8
Наибольшее произведение четырех последовательных цифр в нижеприведенном 
1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
"""
str_number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""
"""
Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
"""
@timer
def biggest_mul(n):  # Число символов
    res = []
    number = str_number.replace("\n", "")
    for i in range(len(number) - n - 1):
        str_sequence = number[i:i+n]
        lst_int = []
        for elem in str_sequence:
            lst_int.append(int(elem))
        res.append(multiply(lst_int))
    return max(res)
# print(biggest_mul(13))

"""
Задача 9
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""
@timer
def pythagorean_triple(s=1000):
    for a in range(3, s):
        for b in range(4, s):
            c = (a**2 + b**2)**0.5
            if a + b + c == s:
                return multiply([a, b, c])
# print(pythagorean_triple(1000))

"""
Задача 10
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""

@timer
def sum_prime_numbers(n):  # n - до скольки считать
    return sum(sieve_of_Eratosthenes(n))
# print(sum_prime_numbers(2000000))

"""
Задача 11
В таблице 20×20 (внизу) четыре числа на одной диагонали выделены красным.
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

Произведение этих чисел 26 × 63 × 78 × 14 = 1788696.
Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, 
расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?
"""
def table_conversion_in_list_of_list(file:str):
    with open(file) as file:
        tbl = file.read()
    lst_row = tbl.split("\n")
    for i, row in enumerate(lst_row):
        lst_row[i] = row.split()
        for ind, elem in enumerate(lst_row[i]):
            lst_row[i][ind] = int(elem)
    return lst_row
@timer
def max_multiply(n=4):
    lst_of_lst = table_conversion_in_list_of_list("greed.txt")
    res_lst = []
    for i in range(len(lst_of_lst)):
        for j in range(0, len(lst_of_lst[i]) - 3):
            res_lst.append(lst_of_lst[i][j] * lst_of_lst[i][j+1] *
                           lst_of_lst[i][j+2] * lst_of_lst[i][j+3])
    for i in range(len(lst_of_lst) - 3):
        for j in range(0, len(lst_of_lst[i])):
            res_lst.append(lst_of_lst[i][j] * lst_of_lst[i+1][j] *
                           lst_of_lst[i+2][j] * lst_of_lst[i+3][j])
    for i in range(len(lst_of_lst) - 3):
        for j in range(0, len(lst_of_lst[i]) - 3):
            res_lst.append(lst_of_lst[i][j] * lst_of_lst[i+1][j+1] *
                           lst_of_lst[i+2][j+2] * lst_of_lst[i+3][j+3])
    for i in range(len(lst_of_lst) - 3):
        for j in range(0, len(lst_of_lst[i]) - 3):
            res_lst.append(lst_of_lst[i][j+3] * lst_of_lst[i+1][j+2] *
                           lst_of_lst[i+2][j+1] * lst_of_lst[i+3][j])
    return max(res_lst)
# print(max_multiply(4))

"""
Задача 12
Последовательность треугольных чисел образуется путем сложения натуральных чисел. 
К примеру, 7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
Первые десять треугольных чисел:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Перечислим делители первых семи треугольных чисел:
 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
Каково первое треугольное число, у которого более пятисот делителей?
"""
def how_divisors_have(n):
    res = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res += 2
    if n / n**0.5 % 1 == 0:
        res -= 1
    return res + 1
@timer
def triangular_numbers(n=500):
    i = 1
    while True:
        number = sum(range(i))
        divis = how_divisors_have(number)
        i += 1
        if divis >= n:
            return i, number, divis
""" Тут 1 секунда - вычисление sum(range(i)), остальные 6 секунд - подсчёт 
кол-ва делителей числа функцией how_divisors_have(). Есть в сети алгоритмы."""
# print(triangular_numbers())

"""
Задача 13
Найдите первые десять цифр суммы следующих ста 50-значных чисел. Имя файла "50numbers.txt"
"""
def parse_numbers(file:str):
    with open(file) as file:
        text = file.read()
    text = text.split('\n')
    for i, elem in enumerate(text):
        text[i] = int(elem)
    return text
@timer
def sum_all_numbers():
    lst = parse_numbers("50numbers.txt")
    return str(sum(lst))[:10]
# print(sum_all_numbers())

"""
Задача 14
Следующая повторяющаяся последовательность определена для множества натуральных чисел:
n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)
Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.
Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
"""
@timer
def problem_Collatz(n=1000000):
    res = [1, 1]
    dict_results = {}
    for ind in range(1, 1000000):
        i = ind
        k = 1
        while i != 1:
            if i % 2 == 0:
                i = i / 2
                k += 1
            else:
                i = 3 * i + 1
                k += 1
            if i in dict_results.keys():  # Если ключ уже есть, то нет необходимости ещё раз считать
                k += dict_results[i]
                i = 1
            if i == 1:
                dict_results[ind] = k  # В словарь добавляются {число:путь}
                if res[1] < k:
                    res = [ind, k]
    return res
""" Добавление словаря пройденных путей позволило уменьшить скорость работы 
алгоритма с 45 до 3 секунд, я рад =)"""

# print(problem_Collatz())

"""
Задача 15
Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только 
вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке 20×20?
"""
"""
Мой комментарий
Долго вникал в то как просчитать все ячейки этой сетки, нашёл некоторые закономерности, 
но их было мало для расчёта полной сетки при n > 7-8.
После этого нашлось элегантное решение позволяющее найти 
весь верхний ряд значений для n+1 при известном n. Где решением для n будет f(n) = lst[0]
Доволен=)
"""

@timer
def path_in_grid(n:int) -> int:  # Принимает разрядность сетки
    n += 1    # Количество узлов в сетке на 1 больше чем разрядность
    lst = [1]
    res = [1]
    for i in range(1, n + 1):
        for k in range(len(lst)):
            res[k] = sum(lst[k:])
        res.insert(0, 2 * res[0])
        res = lst
    return res[0]
# print(path_in_grid(20))

"""
Задача 16
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 2^1000?
"""
@timer
def sum_degree_of_2(n:int) -> int:  # Сумма цифр в числе 2^n
    str_number = str(2**n)
    res = 0
    for num in str_number:
        res += int(num)
    return res
print(sum_degree_of_2(1000))
