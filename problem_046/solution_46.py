from my_tools.tools import timer, is_prime
"""
Задача 46
Кристиан Гольдбах показал, что любое нечетное составное число можно 
записать в виде суммы простого числа и удвоенного квадрата.
9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2
Оказалось, что данная гипотеза неверна.
Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы 
простого числа и удвоенного квадрата?
"""


@timer
def problem_46(n=10000):
    res = set()
    nums = set([n for n in range(2, n) if not (is_prime(n)) and (n % 2 != 0)])
    prime_numbers = set([n for n in range(2, n) if is_prime(n)])
    double_squares = [2 * n ** 2 for n in range(1, int(n ** 0.5))]
    for i in range(4, n):
        if i in prime_numbers or i % 2 == 0:
            continue
        for d_s in double_squares:
            if d_s >= i:
                break
            if i - d_s in prime_numbers:
                res.add(i)
                break
    result = []
    for i in nums:
        if i not in res:
            result.append(i)
    return min(result)


if __name__ == "__main__":
    print(problem_46())
