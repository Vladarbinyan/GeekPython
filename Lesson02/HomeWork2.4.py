"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

while True:
    input_string = input('Введите строку из нескольких слов, слова разделяйте пробелом. '
                         'По окончании ввода нажмите Enter >>> ')
    if input_string.isspace() or not bool(input_string):
        print('Введена пустая строка')
        continue
    else:
        list_of_words = input_string.split(' ')
        for i, word in enumerate(list_of_words):
            print(i + 1, word[0:10] if len(word) > 10 else word)
        break

# Geekbrains

words = input('Введите строку из нескольких слов >>> ').split()

for idx, value in enumerate(words, start=1):
    print(f'{idx}. {value[:10]}')
