from my_tools.tools import timer


"""
Задача 64
Любой квадратный корень является периодическим, если записать его в виде непрерывных дробей.
Первые десять представлений непрерывных дробей (иррациональных) квадратных корней:
√2=[1;(2)], период = 1
√3=[1;(1,2)], период = 2
√5=[2;(4)], период = 1
√6=[2;(2,4)], период = 2
√7=[2;(1,1,1,4)], период = 4
√8=[2;(1,4)], период = 2
√10=[3;(6)], период = 1
√11=[3;(3,6)], период = 2
√12= [3;(2,6)], период = 2
√13=[3;(1,1,1,1,6)], период = 5
Период является нечетным у ровно четырех непрерывных дробей при N ≤ 13.
У скольких непрерывных дробей период является нечетным при N ≤ 10000?
"""


def sqrt_sequence(x: int) -> list:  # Возвращает циклическую последовательность
    a, b, c = 1, x, int(x**0.5)
    a1, b1, c1 = a, b, c
    seq = []
    while True:
        a1 = (b1 - c1 ** 2) / a1
        res = int((b1**0.5 + c1) / a1)
        seq.append(res)
        c1 = abs(c1 - a1 * res)
        if a1 == a and c1 == c:
            return seq


@timer
def problem_64(n=10000):
    res = 0
    for i in range(2, n + 1):
        if i**0.5 == int(i**0.5):  # Отсекаются квадраты целых чисел
            continue
        if len(sqrt_sequence(i)) % 2 != 0:
            res += 1
    return res


if __name__ == "__main__":
    print(problem_64())
