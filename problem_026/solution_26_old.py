from my_tools.tools import timer

"""
Задача 26
Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей 
со знаменателями от 2 до 10 даны ниже:
1/2	=	0.5
1/3	=	0.(3)
1/4	=	0.25
1/5	=	0.2
1/6	=	0.1(6)
1/7	=	0.(142857)
1/8	=	0.125
1/9	=	0.(1)
1/10	=	0.1
Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. 
Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.
Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую 
длинную повторяющуюся последовательность цифр.
"""


# Это катамаран, сделанный из обломков велосипедов, соединённый костылями и изолентой(белой). Удалять жалко.
@timer
def problem_26_old(n=1000, length=3000):
    res = [0, [1]]
    for i in range(1, n + 1):
        base = 1
        lst = []
        for k in range(length):
            if base < i and base != 0:
                base *= 10
                if base < i and base != 0:
                    base *= 10
                    lst.append(0)
                    if base > i:
                        continue
                    if base < i and base != 0:
                        base *= 10
                        lst.append(0)
                        if base > i:
                            continue
                        if base < i:
                            base *= 10
                            lst.append(0)
                            if base > i:
                                continue
            if base == 0:
                lst.append(0)
            if base >= i:
                x = base // i
                base = base % i
                lst.append(x)

        flag = True
        seq = lst[::-1]
        for j in range(int(length / 3), 1, -1):
            if seq[0:j] == seq[j:j * 2] and seq[0 + 1:j + 1] != seq[0:j]:
                seq = seq[0:j]
                for k in range(1, j):
                    if seq[0:k] == seq[k:2 * k]:
                        if flag:
                            seq = seq[0:k]
                            if len(seq) > len(res[1]):
                                res[0], res[1] = i, seq
                            flag = False
                            break
                if flag:
                    if len(seq) > len(res[1]):
                        res[0], res[1] = i, seq
                        break

    return res[0]  # , len(res[1])


if __name__ == "__main__":
    print(problem_26_old())
