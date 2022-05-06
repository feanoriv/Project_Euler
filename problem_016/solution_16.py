from my_tools.tools import timer

"""
Задача 16
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 2^1000?

"""


@timer
def problem_16(n=1000) -> int:  # Сумма цифр в числе 2^n
    str_number = str(2 ** n)
    return sum([int(i) for i in str_number])


if __name__ == "__main__":
    print(problem_16())
