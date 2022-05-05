from my_tools.tools import timer
"""
Задача 30
Удивительно, но существует только три числа, которые могут быть 
записаны в виде суммы четвертых степеней их цифр:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
1 = 1^4 не считается, так как это - не сумма.
Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.
Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
"""


@timer
def problem_30(power=5):
    res = []

    def max_len(power=power):
        n = 2
        while True:
            if len(str(n * (9 ** power))) < n:
                return n - 1
            else:
                n += 1

    for i in range(2, int("9" * max_len(power))):
        lst = [int(n) ** power for n in list(str(i))]
        if sum(lst) == i:
            res.append(i)

    return sum(res)


if __name__ == "__main__":
    print(problem_30())
