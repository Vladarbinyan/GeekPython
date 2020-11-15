"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка.
"""
from os import path

def is_empty(string):
    if string.isspace() or not bool(string):
        return True


def file_write(filename, strings):
    try:
        with open(filename, "w", encoding='utf-8') as my_file:
            print(strings, file=my_file)
    except IOError:
        print('some filesystem error')


"""
Конструкцию ниже взял отсюда: https://goo-gl.su/iJsBk
Раз уж люди плюсуют, то, думаю, стоит объяснить код: iter(input, "") будет yield'ить результат вызова функции 
input без аргументов, пока input() не вернёт пустую строку (""). Далее мы просто объединяем через "\n" все результаты 
из этого генератора. 
"""

print('Введите текст для записи в файл. Для окончания ввода нажите Enter на пустой строке')
strings = "\n".join(iter(input, ""))

if not is_empty(strings):
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
            file_write(filename, strings)
            break


