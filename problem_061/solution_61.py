from my_tools.tools import timer
from itertools import permutations


"""
Задача 61
К фигурным (многоугольным) числам относятся треугольные, квадратные, пятиугольные, шестиугольные, 
семиугольные и восьмиугольные числа, которые расчитываются по следующим формулам:

Треугольные	 	    P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Квадратные	 	    P4,n=n2	 	        1, 4, 9, 16, 25, ...
Пятиугольные	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Шестиугольные	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Семиугольные	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Восьмиугольные	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
Упорядоченное множество из трех четырехзначных чисел: 8128, 2882, 8281, обладает тремя интересными свойствами

Множество является цикличным: последние две цифры каждого числа являются первыми двумя цифрами следующего 
(включая последнее и первое числа).
Каждый тип многоугольника — треугольник (P3,127=8128), квадрат (P4,91=8281) и пятиугольник (P5,44=2882) — 
представлены различными числами данного множества.
Это — единственное множество четырехзначных чисел, обладающее указанными свойствами.
Найдите сумму элементов единственного упорядоченного множества из шести цикличных четырехзначных чисел, в 
котором каждый тип многоугольников — треугольник, квадрат, пятиугольник, шестиугольник, семиугольник и
восьмиугольник — представлены различными числами этого множества.
"""


# Упорядоченный != последовательно 3-4-5-6-7-8-угольные. Порядок произвольный.
# Этот код ужасен. Но ответ верный. Мы тут не в продакшн пушим.


@timer
def problem_61():
    triangle_nums = [int(n * (n + 1) / 2) for n in range(200) if len(str(int(n * (n + 1) / 2))) == 4]
    square_nums = [int(n ** 2) for n in range(200) if len(str(int(n ** 2))) == 4]
    pentagonal_nums = [int(n * (3 * n - 1) / 2) for n in range(200) if len(str(int(n * (3 * n - 1) / 2))) == 4]
    hexagonal_nums = [int(n * (2 * n - 1)) for n in range(200) if len(str(int(n * (2 * n - 1)))) == 4]
    heptagonal_nums = [int(n * (5 * n - 3) / 2) for n in range(200) if len(str(int(n * (5 * n - 3) / 2))) == 4]
    octagonal_nums = [int(n * (3 * n - 2)) for n in range(200) if len(str(int(n * (3 * n - 2)))) == 4]

    lst_lst = [triangle_nums, square_nums, pentagonal_nums, hexagonal_nums, heptagonal_nums, octagonal_nums]
    perm_gen = permutations(lst_lst, r=6)
    for perm_comb in perm_gen:
        i1 = [n for n in perm_comb[0] if str(n)[:2] in [str(k)[2:] for k in perm_comb[-1]]
              and str(n)[2:] in [str(k)[:2] for k in perm_comb[1]]]
        i2 = [n for n in perm_comb[1] if str(n)[:2] in [str(k)[2:] for k in perm_comb[0]]
              and str(n)[2:] in [str(k)[:2] for k in perm_comb[2]]]
        i3 = [n for n in perm_comb[2] if str(n)[:2] in [str(k)[2:] for k in perm_comb[1]]
              and str(n)[2:] in [str(k)[:2] for k in perm_comb[3]]]
        i4 = [n for n in perm_comb[3] if str(n)[:2] in [str(k)[2:] for k in perm_comb[2]]
              and str(n)[2:] in [str(k)[:2] for k in perm_comb[4]]]
        i5 = [n for n in perm_comb[4] if str(n)[:2] in [str(k)[2:] for k in perm_comb[3]]
              and str(n)[2:] in [str(k)[:2] for k in perm_comb[5]]]
        i6 = [n for n in perm_comb[5] if str(n)[:2] in [str(k)[2:] for k in perm_comb[4]]
              and str(n)[2:] in [str(k)[:2] for k in perm_comb[0]]]

        # Блок кода ниже можно повторять до достижения результата. Тут хватает 1 раза.
        i1 = [n for n in i1 if str(n)[:2] in [str(k)[2:] for k in i6] and str(n)[2:] in [str(k)[:2] for k in i2]]
        i2 = [n for n in i2 if str(n)[:2] in [str(k)[2:] for k in i1] and str(n)[2:] in [str(k)[:2] for k in i3]]
        i3 = [n for n in i3 if str(n)[:2] in [str(k)[2:] for k in i2] and str(n)[2:] in [str(k)[:2] for k in i4]]
        i4 = [n for n in i4 if str(n)[:2] in [str(k)[2:] for k in i3] and str(n)[2:] in [str(k)[:2] for k in i5]]
        i5 = [n for n in i5 if str(n)[:2] in [str(k)[2:] for k in i4] and str(n)[2:] in [str(k)[:2] for k in i6]]
        i6 = [n for n in i6 if str(n)[:2] in [str(k)[2:] for k in i5] and str(n)[2:] in [str(k)[:2] for k in i1]]

        if (len(i1) == 1) and (len(i2) == 1) and (len(i3) == 1) and (len(i4) == 1) and (len(i5) == 1) and (len(i6) == 1):
            return sum([i1[0], i2[0], i3[0], i4[0], i5[0], i6[0]])


if __name__ == "__main__":
    print(problem_61())
