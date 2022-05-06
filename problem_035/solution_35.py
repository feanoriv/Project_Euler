from my_tools.tools import timer, is_prime
"""
Задача 35
Число 197 называется круговым простым числом, потому что все перестановки его цифр 
с конца в начало являются простыми числами: 197, 719 и 971.
Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
Сколько существует круговых простых чисел меньше миллиона?
"""


def check_variations_is_prime(n: str):
    for i in range(len(n)):
        n = n[1:] + n[0]
        if not is_prime(int(n)):
            return False
    return True


@timer
def problem_35(n=1000000):
    res = 1
    for i in range(3, n, 2):
        if any(n in ["0", "2", "4", "6", "8"] for n in str(i)):
            continue
        if is_prime(i):
            if check_variations_is_prime(str(i)):
                res += 1
    return res


if __name__ == "__main__":
    print(problem_35())
