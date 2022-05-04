from my_tools.tools import timer, is_prime

"""
Задача 7
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?
"""


@timer
def problem_7(n=10001):
    number = 2
    number_primary = 0
    while True:
        if is_prime(number):
            number_primary += 1
            if number_primary == n:
                return number
        number += 1


if __name__ == "__main__":
    print(problem_7())
