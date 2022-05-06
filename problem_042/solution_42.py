from my_tools.tools import timer, get_num_char
"""
Задача 42
n-й член последовательности треугольных чисел задается как tn = ½n(n+1). 
Таким образом, первые десять треугольных чисел:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в 
алфавите, и складывая эти значения, мы получим числовое значение слова. 
Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t10. 
Если числовое значение слова является треугольным числом, то мы назовем это слово треугольным словом.
Используя words.txt (щелкнуть правой кнопкой мыши и выбрать 
'Save Link/Target As...'), 16 КБ текстовый файл, содержащий около двух тысяч 
часто используемых английских слов, определите, сколько в нем треугольных слов.
"""


def get_list_names_from_file(file="p042_words.txt") -> list:
    with open(file) as file:
        text = file.read().replace('"', "").split(",")
    return text


@timer
def problem_42():
    triangle_numbers = [int((n * (n + 1)) / 2) for n in list(range(1, 100))]
    words = get_list_names_from_file()
    res = 0
    for word in words:
        sum_chars = 0
        for char in word:
            sum_chars += get_num_char(char)
        if sum_chars in triangle_numbers:
            res += 1
    return res


if __name__ == "__main__":
    print(problem_42())
