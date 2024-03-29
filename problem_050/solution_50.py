from my_tools.tools import timer, is_prime
"""
Задача 50
Простое число 41 можно записать в виде суммы шести последовательных простых чисел:
41 = 2 + 3 + 5 + 7 + 11 + 13
Это - самая длинная сумма последовательных простых чисел, в результате которой
получается простое число меньше одной сотни.
Самая длинная сумма последовательных простых чисел, в результате которой получается
простое число меньше одной тысячи, содержит 21 слагаемое и равна 953.
Какое из простых чисел меньше одного миллиона можно записать в виде суммы 
наибольшего количества последовательных простых чисел?
"""


@timer
def problem_50(n=1000_000):
    stack = 0
    res = [0, 0]
    lst = [n for n in range(2, int(n / 250)) if is_prime(n)]
    for i in range(len(lst)):
        for k in range(20, 999):
            if i + k >= len(lst):
                break
            if is_prime(sum(lst[i:i + k])) and sum(lst[i:i + k]) <= n:
                stack = k
            else:
                if res[0] < stack:
                    res[0] = stack
                    res[1] = sum(lst[i:i + k - 1])
    return res


if __name__ == "__main__":
    print(problem_50())
