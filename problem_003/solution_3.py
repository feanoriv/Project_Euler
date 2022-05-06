from my_tools.tools import timer, is_prime

"""
Задача 3
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


# Проверка осуществляется только до корня заданного числа
# Если число "х" является делителем, то так же проверяется его пара - "у" (х*у = res)
@timer
def problem_3(n=600851475143):
    square_root = int(n ** 0.5) + 1
    multipliers = set()
    for i in range(2, square_root):
        if n % i == 0:
            if is_prime(int(n / i)):
                return int(n / i)
            if is_prime(i):
                multipliers.add(i)
    return max(multipliers)


if __name__ == "__main__":
    print(problem_3())
