from my_tools.tools import timer, factorial
"""
Задача 34
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""


@timer
def problem_34():
    res = 0
    limit = 50000  # Лимит уточнён после получения ответа
    for i in range(3, limit):
        sum_factorials = sum([factorial(int(i)) for i in list(str(i))])
        if sum_factorials == i:
            res += i
    return res


if __name__ == "__main__":
    print(problem_34())
