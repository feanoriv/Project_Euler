from my_tools.tools import timer
"""
Задача 48
Сумма 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


@timer
def problem_48(n=1000):
    res = 0
    for i in range(1, n + 1):
        res += i ** i
    return str(res)[-10:]


if __name__ == "__main__":
    print(problem_48())
