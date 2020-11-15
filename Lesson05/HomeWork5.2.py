"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
from os import path

def is_empty(string):
    if string.isspace() or not bool(string):
        return True


print('Выполняет чтение файла, посдчет количества строк и количества слов в каждой строке')
while True:
    filename = input(
        'Введите имя файла в текущей директории, для выхода без чтения оставьте поле пустым >>> ')
    if is_empty(filename):
        print('Запись отменена')
        break
    elif not path.exists(filename):
        print('Файл не существует, введите другое имя существующего файла')
        continue
    else:
        try:
            with open(filename, "r", encoding='utf-8') as my_file:
                file_data_lines = []
                for line in my_file.readlines():
                    file_data_lines.append(line)
        except IOError:
            print('Some error')
        break

print(f'Файл содержит {len(file_data_lines)} строк')
for i, el in enumerate(file_data_lines):
    print(f'Строка {i+1} состоит из {len(el.split())} слов')

