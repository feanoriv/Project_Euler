from my_tools.tools import timer, is_prime

"""
Задача 3
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


@timer
def problem_3_1(n=600851475143):
    square_root = int(n ** 0.5) + 1
    while True:
        for i in range(2, square_root):
            if is_prime(n):
                return int(n)
            if n % i == 0:
                n = n / i
                break


if __name__ == "__main__":
    print(problem_3_1())
