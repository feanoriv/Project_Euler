from my_tools.tools import timer
from itertools import permutations

"""
Задача 44
Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. 
Первые десять пятиугольных чисел:
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. 
Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.
Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность 
являются пятиугольными числами и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.
"""


@timer
def problem_44():
    res = []
    lst = set([int(n * (3 * n - 1) / 2) for n in range(1, 2400)])  # 2400 - определено перебором
    for i in lst:
        for j in lst:
            if i > j:
                if i + j in lst and i - j in lst:
                    res.append(i - j)
    return res


if __name__ == "__main__":
    print(problem_44())
