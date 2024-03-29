from my_tools.tools import timer

"""
Задача 15
Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только 
вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке 20×20?
"""

# Верхние узлы
# 1х1 - 1
# 2х2 - 1 2
# 3х3 - 1 3 6
# 4х4 - 1 4 10 20
# 5х5 - 1 5 15 35 70
# Расчёт узлов 6х6:
# 6х6 - (1) (1+5) (1+5+15) (1+5+15+35) (1+5+15+35+70) (1+5+15+35+70)*2
# 6х6 - 1 6 21 56 126 252
# 7х7 - (1) (1+6) (1+6+21) (1+6+21+56) (1+6+21+56+126) (1+6+21+56+126+252) (1+6+21+56+126)*2


@timer
def problem_15(n=20) -> int:  # Принимает разрядность сетки
    n += 1  # Количество узлов в сетке на 1 больше чем разрядность
    lst = [1]
    res = [1]
    for i in range(1, n + 1):
        for k in range(len(lst)):
            res[k] = sum(lst[k:])
        res.insert(0, 2 * res[0])
        res = lst
    return res[0]


if __name__ == "__main__":
    print(problem_15())
