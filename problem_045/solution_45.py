from my_tools.tools import timer
"""
Задача 45
Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:
Треугольные	 	    Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Пятиугольные	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
Можно убедиться в том, что T285 = P165 = H143 = 40755.
Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.
"""


@timer
def problem_45():
    res = []
    triangle_nums = set([n * (n + 1) / 2 for n in range(2, 100000)])
    fivangle_nums = set([n * (3 * n - 1) / 2 for n in range(2, 100000)])
    sixangle_nums = set([n * (2 * n - 1) for n in range(2, 100000)])
    for i in sixangle_nums:
        if i in fivangle_nums and i in triangle_nums:
            res.append(i)
    return sorted(res)[1]


if __name__ == "__main__":
    print(problem_45())
