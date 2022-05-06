from my_tools.tools import timer, is_prime
"""
Задача 41
Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 
до n используется в нем ровно один раз. К примеру, 2143 является 4-значным 
пан-цифровым числом, а также простым числом.
Какое существует наибольшее n-значное пан-цифровое простое число?
"""


@timer
def problem_41(n=7):
    for i in range(7654321, 1234567, -2):  # Для n=(9,8,6,5,3,2) такого числа нет, т.к. сумма цифр кратна 3.
        if i % 2 != 0:
            str_num = str(i)
            if ("0" not in str_num) and ("9" not in str_num) and ("8" not in str_num):
                if len(set(list(str_num))) == n:
                    if is_prime(i):
                        return i


if __name__ == "__main__":
    print(problem_41())
