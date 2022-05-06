from my_tools.tools import timer, is_prime, multiply

"""
Задача 5
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""


# Итерация проводится с шагом равным произведению простых чисел в диапазоне от 2 до "n",
# т.к. искомое число гарантированно кратно этому произведению
@timer
def problem_5(n=20):
    list_simple_numbers = [x for x in range(2, n + 1) if is_prime(x)]
    step = multiply(list_simple_numbers)
    res = 0
    while res <= multiply(list(range(1, n + 1))):
        res += step
        if all([res % x == 0 for x in list(range(1, n + 1))]):
            return res


if __name__ == "__main__":
    print(problem_5())
