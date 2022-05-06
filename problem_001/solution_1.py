from my_tools.tools import timer

"""
Задача 1
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""


@timer
def problem_1(n=1000):
    return sum([a for a in range(n) if a % 3 == 0 or a % 5 == 0])


if __name__ == "__main__":
    print(problem_1())
