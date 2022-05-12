from my_tools.tools import timer


"""
Задача 63
Пятизначное число 16807 = 7^5 является также пятой степенью натурального числа. Аналогично, 
девятизначное число 134217728 = 8^9 является девятой степенью.
Сколько существует n-значных натуральных чисел, являющихся также и n-ми степенями натуральных чисел?
"""


@timer
def problem_63():
    def len_num(n: int) -> int:
        return len(str(n))
    res = 0
    for i in range(1, 100):
        for k in range(1, 100):
            if len_num(i**k) == k:
                res += 1
    return res


if __name__ == "__main__":
    print(problem_63())
