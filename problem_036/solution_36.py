from my_tools.tools import timer, is_palindrome_str
"""
Задача 36
Десятичное число 585 = 1001001001 (в двоичной системе), является палиндромом по обоим основаниям.
Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.
(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).
"""


@timer
def problem_36(n=1000000):
    res = 0
    for i in range(1, n, 2):
        if all([is_palindrome_str(str(i)), is_palindrome_str(bin(i)[2:])]):
            res += i
    return res


if __name__ == "__main__":
    print(problem_36())
