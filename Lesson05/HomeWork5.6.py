"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json
from os import path


def str_float(string):
    """
    :param string:
    :return: float или None
    """
    try:
        return float(string)
    except ValueError:
        print(f'Ошибка преобразования {string}')
        return 0


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


def calc_profit(proceeds, costs):
    return round(str_float(proceeds) - str_float(costs), 2)


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
        'Введите имя файла в текущей директории, для выхода без чтения оставьте поле пустым (образец в файле firms) '
        '>>> ')
    if is_empty(filename):
        print('Чтение отменено, выход')
        break
    elif not path.exists(filename):
        print('Файл не существует, введите другое имя файла')
        continue
    else:
        firms = {}
        out_data = []
        in_string = file_read(filename)
        if in_string is not None:
            for line in in_string.split('\n'):
                firm, form, proceeds, costs = line.split()
                firms[firm] = calc_profit(proceeds, costs)
            print('Прибыль (положительные числа) и убытки (отрицательные числа) по компаниям')
            print(firms)
            out_data.append(firms)
            profits = [i for i in firms.values() if i > 0]
            average_profit = sum(profits)/len(profits)
            out_data.append({'average_profit': average_profit})
            print(f'Средняя прибыль {average_profit}')
            try:
                with open('firms_data.json', 'w') as file_stream:
                    json.dump(out_data, file_stream)
                    print('Данные записаны в \"firms_data.json"')
            except IOError:
                print('Ошибка при записи файла')

            break
        else:
            continue
