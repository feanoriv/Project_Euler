from my_tools.tools import timer, multiply

"""
Задача 9
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""


@timer
def problem_9(s=1000):
    for a in range(3, s):
        for b in range(4, s):
            if (a + b) * 2 < s:
                continue
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == s:
                return multiply([a, b, c])


if __name__ == "__main__":
    print(problem_9())
