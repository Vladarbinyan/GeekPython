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
        try:
            with open(filename, "r", encoding='utf-8') as input_file:
                salaries = {}  # строки которые читаем из файла будем складывать в словарь, где ключ это сотрудник а
                # ЗП значение. Предполагаем что формат файла соответстует, поэтому проверки опускаем.
                for line in input_file.readlines():
                    person, amount = line.replace('\n', '').split(' ')
                    salaries.update({person: float(amount)})
        except IOError:
            print('some filesystem error')
            continue
        print(salaries)
        for person in salaries.keys():
            if salaries.get(person) < 20000:
                print(f'У сотрудника {person} оклад меньше 20000 рублей')
        print(f'Средняя величина дохода составила {round(sum(salaries.values()) / len(salaries), 2)} рублей')
        break

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
        try:
            with open(filename, "r", encoding='utf-8') as input_file:
                in_string = input_file.read()
                for eng, ru in my_dict.items():
                    in_string = in_string.replace(eng, ru)
        except IOError:
            print('some filesystem error')
            continue
        try:
            with open('en_'+filename, "w", encoding='utf-8') as output_file:
                output_file.write(in_string)
        except IOError:
            print('some filesystem error')
        print(f'Результат записан в файл: en_{filename}')
        break


