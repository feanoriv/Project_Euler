from my_tools.tools import timer

"""
Задача 21
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, 
а каждое из чисел a и b - дружественным числом.
Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, 
поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
Подсчитайте сумму всех дружественных чисел меньше 10000.
"""


def divisors(n):
    res = [1]
    if n <= 1:
        return [0]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i ** 2 != n:
            res.append(i)
            res.append(int(n / i))
        elif i ** 2 == n:
            res.append(i)
    return res


@timer
def problem_21(n=10000):
    res = []
    for i in range(1, n + 1):
        a_num = sum(divisors(i))
        if i != a_num:
            if i == sum(divisors(a_num)):
                res.append(i)
    return res


if __name__ == "__main__":
    print(problem_21())