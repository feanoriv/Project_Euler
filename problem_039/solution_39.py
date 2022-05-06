from my_tools.tools import timer
"""
Задача 39
Если p - периметр прямоугольного треугольника с целочисленными длинами 
сторон {a,b,c}, то существует ровно три решения для p = 120:
{20,48,52}, {24,45,51}, {30,40,50}
Какое значение p ≤ 1000 дает максимальное число решений?
"""


@timer
def problem_39(n=1000):
    res = []
    for a in range(1, n):
        for b in range(1, n):
            if a < b:
                c = (a*a + b*b) ** 0.5
                if c == int(c):
                    res.append(a + b + c)
    max_count = [0, 0]
    for i in res:
        if i <= n:
            count = res.count(i)
            if count > max_count[0]:
                max_count[0] = count
                max_count[1] = i

    return max_count


if __name__ == "__main__":
    print(problem_39())
