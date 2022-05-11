from my_tools.tools import timer


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

# В этой задаче (как и в прошлой) явно необходимо использовать графы и искать в них клики.

# Разделить каждый список на 2 части с началом и концом числа.
# Проверять с последнего списка каждое его число - есть ли в списке №5 число, которое заканчивается
# так же, как начинается число из списка №6. При этом есть ли число в списке №1, которое начинается так же,
# как заканчивается число из списка №6


@timer
def problem_61():
    triangle_nums = [int(n*(n+1)/2) for n in range(200) if len(str(int(n*(n+1)/2))) == 4]
    square_nums = [int(n**2) for n in range(100) if len(str(int(n**2))) == 4]
    pentagonal_nums = [int(n*(3*n+1)/2) for n in range(150) if len(str(int(n*(3*n+1)/2))) == 4]
    hexagonal_nums = [int(n*(2*n+1)) for n in range(150) if len(str(int(n*(2*n+1)))) == 4]
    heptagonal_nums = [int(n*(5*n+1)/2) for n in range(150) if len(str(int(n*(5*n+1)/2))) == 4]
    octagonal_nums = [int(n*(3*n+1)) for n in range(150) if len(str(int(n*(3*n+1)))) == 4]

    triangle_nums = [n for n in triangle_nums if str(n)[:2] in
                     [str(k)[2:] for k in octagonal_nums] and str(n)[2:] in
                     [str(x)[:2] for x in square_nums]]
    square_nums = [n for n in square_nums if str(n)[:2] in
                   [str(k)[2:] for k in triangle_nums] and str(n)[2:] in
                   [str(j)[:2] for j in pentagonal_nums]]

    pentagonal_nums = [n for n in pentagonal_nums if str(n)[:2] in
                       [str(k)[2:] for k in square_nums] and str(n)[2:] in
                       [str(j)[:2] for j in hexagonal_nums]]

    hexagonal_nums = [n for n in hexagonal_nums if str(n)[:2] in
                      [str(k)[2:] for k in pentagonal_nums] and str(n)[2:] in
                      [str(j)[:2] for j in heptagonal_nums]]

    heptagonal_nums = [n for n in heptagonal_nums if str(n)[:2] in
                      [str(k)[2:] for k in hexagonal_nums] and str(n)[2:] in
                      [str(j)[:2] for j in octagonal_nums]]

    octagonal_nums = [n for n in octagonal_nums if str(n)[:2] in
                      [str(k)[2:] for k in heptagonal_nums] and str(n)[2:] in
                      [str(j)[:2] for j in triangle_nums]]

    return (triangle_nums, square_nums, pentagonal_nums, hexagonal_nums, heptagonal_nums, octagonal_nums)
    # Не работает!?

if __name__ == "__main__":
    print(problem_61())
