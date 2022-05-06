from my_tools.tools import timer, factorial

"""
Задача 20
n! означает n × (n − 1) × ... × 3 × 2 × 1
Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Найдите сумму цифр в числе 100!.
"""


@timer
def problem_20(n=100):
    return sum([int(x) for x in list(str(factorial(n)))])


if __name__ == "__main__":
    print(problem_20())
