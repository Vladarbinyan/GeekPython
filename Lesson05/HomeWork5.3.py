"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников. Пример файла:

Иванов 23543.12
Петров 13749.32

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

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


print(
    'Первая часть. Выполняет чтение файла, определяет сотрудников с окладом менее 20 тыс, '
    'вычисляет средний доход по всем сотрудникам')
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
        salaries = {}  # строки которые читаем из файла будем складывать в словарь, где ключ это сотрудник а
        # ЗП значение. Предполагаем что формат файла соответстует, поэтому проверки опускаем.
        in_string = file_read(filename)
        if in_string is not None:
            for line in in_string.split('\n'):
                if not is_empty(line):
                    person, amount = line.split(' ')
                    salaries.update({person: float(amount)})
            # print(salaries)
            for person in salaries.keys():
                if salaries.get(person) < 20000:
                    print(f'У сотрудника {person} оклад меньше 20000 рублей')
            print(f'Средняя величина дохода составила {round(sum(salaries.values()) / len(salaries), 2)} рублей')
            break
        else:
            continue

print('Вторая часть. Считывание числительных из файла, перевод и запись в новый файл')

my_dict = {'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
           'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять'}

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
        in_string = file_read(filename)
        for eng, ru in my_dict.items():
            in_string = in_string.replace(eng, ru)
        if file_write('en_' + filename, in_string):
            print(f'Результат записан в файл: en_{filename}')
        break
