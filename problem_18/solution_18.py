from my_tools.tools import timer

"""
Задача 18
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз 
на смежные числа, максимальная сумма до основания составляет 23.
3
7 4
2 4 6
8 5 9 3
То есть, 3 + 7 + 4 + 9 = 23.
Найдите максимальную сумму пути от вершины до основания следующего треугольника (triangle.txt):
Примечание: Так как в данном треугольнике всего 16384 возможных 
маршрута от вершины до основания, эту задачу можно решить 
проверяя каждый из маршрутов. Однако похожая Задача 67 с 
треугольником, состоящим из сотни строк, не решается перебором 
(brute force) и требует более умного подхода! ;o)
"""


def parse_triangle(file="triangle.txt") -> list:
    with open(file) as file:
        text = file.read()
    res = []
    for elem in text.split("\n"):
        res.append([int(num) for num in elem.split(" ")])
    return res


@timer
def problem_18():
    lst = parse_triangle()[::-1]  # Начало итераций с основания
    for ind, line in enumerate(lst):
        if ind == len(lst) - 1:
            return line[0]
        for i in range(len(lst[ind + 1])):
            lst[ind + 1][i] = lst[ind + 1][i] + max(lst[ind][i], lst[ind][i + 1])


if __name__ == "__main__":
    print(problem_18())
