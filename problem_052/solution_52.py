from my_tools.tools import timer
"""
Задача 52
Найдите такое наименьшее натуральное число x, чтобы 
2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.
"""


@timer
def problem_52():
    n = 0
    while True:
        n += 1
        if set(str(n * 2)) == set(str(n * 3)) == set(str(n * 4)) == set(str(n * 5)) == set(str(n * 6)):
            return n


if __name__ == "__main__":
    print(problem_52())
