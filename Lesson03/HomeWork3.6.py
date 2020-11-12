"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу
должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать
написанную ранее функцию int_func().
"""


def int_func(word: str):
    return word.capitalize()


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


while True:
    input_string = input('Введите слово или строку слов разделенных пробелами \n')
    if is_empty(input_string):
        print('Пустая строка')
        continue
    else:
        words = input_string.split()
        capitalized_words = []
        for word in words:
            capitalized_words.append(int_func(word))
        print(capitalized_words)
        break
