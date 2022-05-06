from my_tools.tools import timer

"""
Задача 13
Найдите первые десять цифр суммы следующих ста 50-значных чисел. Имя файла "50numbers.txt"
"""


def parse_numbers(file="50numbers.txt"):
    with open(file) as file:
        text = file.read()
    text = text.split('\n')
    return [int(i) for i in text]


@timer
def problem_13(n=10):
    lst = parse_numbers()
    return str(sum(lst))[:n]


if __name__ == "__main__":
    print(problem_13())
