from my_tools.tools import timer, sieve_of_eratosthenes

"""
Задача 10
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""


@timer
def problem_10(n=2000000):  # n - до скольки считать
    return sum(sieve_of_eratosthenes(n))


if __name__ == "__main__":
    print(problem_10())
