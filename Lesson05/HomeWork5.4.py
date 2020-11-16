"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce
from random import randint
from os import path


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


def file_write(filename, strings):
    """
    :param filename:
    :param strings:
    :return: True or False
    """
    try:
        with open(filename, "w", encoding='utf-8') as out_file:
            print(strings, file=out_file)
            return True
    except IOError:
        print('some filesystem error')
        return False


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
        'Введите имя файла (запись файла в текущую директорию), для выхода без записи оставьте поле пустым >>> ')
    if is_empty(filename):
        print('Запись отменена')
        break
    elif path.exists(filename):
        print('Файл уже существует, введите другое имя файла')
        continue
    else:
        strings = ''
        for i in range(50):
            strings += str(randint(0, 2000)) + ' '
        if file_write(filename, strings):
            print(f'Результат записан в файл: {filename}')
        break
numbers = file_read(filename).split()
if numbers is not None:
    numbers = [int(i) for i in numbers]
    print(reduce(lambda x, y: x + y, numbers, 0))
