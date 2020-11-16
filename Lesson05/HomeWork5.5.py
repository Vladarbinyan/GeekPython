"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from functools import reduce
from os import path


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


def file_read(filename):
    """
    :param filename:
    :return: str or None
    """
    try:
        with open(filename, "r", encoding='utf-8') as input_file:
            strings = input_file.read()
            return strings
    except IOError:
        print('some filesystem error')
        return


while True:
    filename = input(
        'Введите имя файла в текущей директории, для выхода без чтения оставьте поле пустым >>> ')
    if is_empty(filename):
        print('Чтение отменено, выход')
        break
    elif not path.exists(filename):
        print('Файл не существует, введите другое имя файла')
        continue
    else:
        subjects = {}
        my_dict = {'(л)': '', '(пр)': '', '(лаб)': '', '.': '', '—': ''}
        in_string = file_read(filename)
        if in_string is not None:
            for seq, new_seq in my_dict.items():  # Заменяю последовательности по словарю на пробелы,
                # возможно не лучшая реализация, но зато наглядно и читаемо.
                in_string = in_string.replace(seq, new_seq)
            for line in in_string.split('\n'):
                subject, amount = line.split(':')
                amount = [int(i) for i in amount.split()]  # преобразуем строку в список значений, затем значения в int
                subjects[subject] = (reduce(lambda x, y: x + y, amount, 0))
            print(subjects)
            break
        else:
            continue
