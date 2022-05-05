from my_tools.tools import timer

"""
Задача 22
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки 
в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте 
это значение на порядковый номер имени в отсортированном списке для получения количества 
очков имени.
Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 
3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 
очков.
Какова сумма очков имен в файле?
"""


def read_file_return_lst_names(file="names.txt"):
    with open(file) as file:
        text = file.read()
    text = text.replace('"', '').split(",")
    return sorted(text)


@timer
def problem_22():
    names = read_file_return_lst_names()
    lst_points = 0
    for ind, name in enumerate(names):
        points = 0
        for char in name:
            points += ord(char) - 64
        points *= (ind + 1)
        lst_points += points
    return lst_points


if __name__ == "__main__":
    print(problem_22())
