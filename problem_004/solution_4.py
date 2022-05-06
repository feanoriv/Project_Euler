from my_tools.tools import timer, is_palindrome

"""
Задача 4
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


@timer
def problem_4(n=3):  # n - разрядность чисел
    max_palindrome = 0
    n1, n2 = int(n * "9"), int(n * "9")
    for i in range(n1, 0, -1):
        for k in range(n2, 0, -1):
            mul = i * k
            if mul < max_palindrome:
                break
            if is_palindrome(mul):
                max_palindrome = mul
    return max_palindrome


if __name__ == "__main__":
    print(problem_4())
