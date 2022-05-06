from my_tools.tools import timer

"""
Задача 54

*** пропущено описание правил покера с примерами ***

Файл poker.txt содержит одну тысячу различных ставок для игры двух игроков. 
В каждой строке файла приведены десять карт (отделенные одним пробелом): первые пять - 
карты 1-го игрока, оставшиеся пять - карты 2-го игрока. Можете считать, что все ставки 
верны (нет неверных символов или повторов карт), ставки каждого игрока не следуют в 
определенном порядке, и что при каждой ставке есть безусловный победитель.
Сколько ставок выиграл 1-й игрок?
Примечание: карты в текстовом файле обозначены в соответствии с английскими наименованиями 
достоинств и мастей: T - десятка, J - валет, Q - дама, K - король, A - туз; S - пики, 
C - трефы, H - червы, D - бубны.
"""


@timer
def problem_54():
    """Функции, которые начинаются с 'is_' возвращают False если комбинация отсутствует,
    а если такая комбинация есть то возвращает число, х_уу_уу_уу_уу_уу,
    где х - комбинация(от 9 - флэш роял до 0 - старшая карта), а
    уу - карты в порядке значимости и убывания.
    Любая комбинация описанная таким способом даёт число, которое можно сравнивать с другим
    и выявлять более сильную комбинацию путём сравнения этих чисел."""

    def get_comps(file="p054_poker.txt"):
        with open(file) as file:
            text = file.read()
        return text.split("\n")[:-1]

    def get_comps_players(s: str):
        s = s.replace("2", "02")
        s = s.replace("3", "03")
        s = s.replace("4", "04")
        s = s.replace("5", "05")
        s = s.replace("6", "06")
        s = s.replace("7", "07")
        s = s.replace("8", "08")
        s = s.replace("9", "09")
        s = s.replace("T", "10")
        s = s.replace("J", "11")
        s = s.replace("Q", "12")
        s = s.replace("K", "13")
        s = s.replace("A", "14")
        s = s.split(" ")
        for i, sim in enumerate(s):
            s[i] = [s[i][:-1], s[i][-1]]
        s1 = s[:5]
        s2 = s[5:]
        return s1, s2

    def is_royal_flush(lst: list):
        suit = set()
        value = set()
        for i in lst:
            value.add(i[0])
            suit.add(i[1])
        if len(suit) == 1 and value == {"10", "11", "12", "13", "14"}:
            return 90000000000
        else:
            return False

    def is_straight_flush(lst: list):
        suit = set()
        value = set()
        for i in lst:
            value.add(i[0])
            suit.add(i[1])
        if len(suit) == 1 and len(value) == 5:
            lst = sorted(list(value), reverse=True)
            for ind, el in enumerate(lst[:-1]):
                if int(el) - int(lst[ind + 1]) == 1:
                    continue
                else:
                    return False
            return int("8" + "".join(lst))
        else:
            return False

    def is_four_of_kind(lst: list):
        suit = []
        value = []
        for i in lst:
            value.append(i[0])
            suit.append(i[1])
        value = sorted(value)
        if len(set(value[1:])) == 1:
            return int("7" + "".join(value[1:]) + value[0])
        if len(set(value[:-1])) == 1:
            return int("7" + "".join(value[:-1]) + value[-1])
        else:
            return False

    def is_full_house(lst: list):
        suit = []
        value = []
        for i in lst:
            value.append(i[0])
            suit.append(i[1])
        value = sorted(value)
        if len(set(value[2:])) == 1 and len(set(value[:2])) == 1:
            return int("6" + "".join(value[2:]) + "".join(value[:2]))
        if len(set(value[3:])) == 1 and len(set(value[:3])) == 1:
            return int("6" + "".join(value[:3]) + "".join(value[3:]))
        else:
            return False

    def is_flush(lst: list):
        suit = set()
        value = []
        for i in lst:
            value.append(i[0])
            suit.add(i[1])
        value = sorted(value, reverse=True)
        if len(suit) == 1:
            return int("5" + "".join(value))
        else:
            return False

    def is_straight(lst: list):
        value = []
        for i in lst:
            value.append(i[0])
        value = sorted(value, reverse=True)
        if len(set(value)) == 5 and int(value[0]) - int(value[4]) == 4:
            return int("4" + "".join(value))
        else:
            return False

    def is_three_of_kind(lst: list):
        value = []
        for i in lst:
            value.append(i[0])
        value = sorted(value, reverse=True)
        if len(set(value)) == 3:
            if len(set(value[:3])) == 1:
                return int("3" + "".join(value[:3]) + value[3] + value[4])
            if len(set(value[1:4])) == 1:
                return int("3" + "".join(value[1:4]) + value[0] + value[4])
            if len(set(value[2:])) == 1:
                return int("3" + "".join(value[2:]) + value[0] + value[1])
        else:
            return False

    def is_two_pairs(lst: list):
        value = []
        for i in lst:
            value.append(i[0])
        value = sorted(value, reverse=True)
        if len(set(value)) == 3:
            if len(set(value[:2])) == 1 and len(set(value[3:])) == 1:
                return int("2" + "".join(value[:2]) + value[3] + value[4] + value[2])
            if len(set(value[:2])) == 1 and len(set(value[2:4])) == 1:
                return int("2" + "".join(value[:2]) + value[2] + value[3] + value[4])
            if len(set(value[1:3])) == 1 and len(set(value[3:])) == 1:
                return int("2" + "".join(value[1:3]) + value[3] + value[4] + value[0])
        else:
            return False

    def is_one_pairs(lst: list):
        value = []
        for i in lst:
            value.append(i[0])
        value = sorted(value, reverse=True)
        if len(set(value)) == 4:
            if len(set(value[:2])) == 1:
                return int("1" + "".join(value[:2]) + value[2] + value[3] + value[4])
            if len(set(value[1:3])) == 1:
                return int("1" + "".join(value[1:3]) + value[0] + value[3] + value[4])
            if len(set(value[2:4])) == 1:
                return int("1" + "".join(value[2:4]) + value[0] + value[1] + value[4])
            if len(set(value[3:])) == 1:
                return int("1" + "".join(value[3:]) + value[0] + value[1] + value[2])
        else:
            return False

    def is_high_card(lst: list):
        suit = set()
        value = []
        for i in lst:
            value.append(i[0])
            suit.add(i[1])
        value = sorted(value, reverse=True)
        if len(set(value)) == 5 and len(suit) > 1:
            return int("0" + "".join(value))
        else:
            return False

    res = 0
    lst_comps = get_comps()
    for comp in lst_comps:
        s1, s2 = get_comps_players(comp)
        if is_royal_flush(s1):
            s1 = is_royal_flush(s1)
        elif is_straight_flush(s1):
            s1 = is_straight_flush(s1)
        elif is_four_of_kind(s1):
            s1 = is_four_of_kind(s1)
        elif is_full_house(s1):
            s1 = is_full_house(s1)
        elif is_flush(s1):
            s1 = is_flush(s1)
        elif is_straight(s1):
            s1 = is_straight(s1)
        elif is_three_of_kind(s1):
            s1 = is_three_of_kind(s1)
        elif is_two_pairs(s1):
            s1 = is_two_pairs(s1)
        elif is_one_pairs(s1):
            s1 = is_one_pairs(s1)
        elif is_high_card(s1):
            s1 = is_high_card(s1)

        if is_royal_flush(s2):
            s2 = is_royal_flush(s2)
        elif is_straight_flush(s2):
            s2 = is_straight_flush(s2)
        elif is_four_of_kind(s2):
            s2 = is_four_of_kind(s2)
        elif is_full_house(s2):
            s2 = is_full_house(s2)
        elif is_flush(s2):
            s2 = is_flush(s2)
        elif is_straight(s2):
            s2 = is_straight(s2)
        elif is_three_of_kind(s2):
            s2 = is_three_of_kind(s2)
        elif is_two_pairs(s2):
            s2 = is_two_pairs(s2)
        elif is_one_pairs(s2):
            s2 = is_one_pairs(s2)
        elif is_high_card(s2):
            s2 = is_high_card(s2)

        if s1 > s2:
            res += 1
    return res


if __name__ == "__main__":
    print(problem_54())
