"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


while True:
    input_string = input('Введите в строку список элементов, элементы разделяйте пробелом. '
                         'По окончании ввода нажмите Enter\n')
    if is_empty(input_string):
        print('Не могу работать с пустой строкой')
        continue
    elements_list = input_string.split(' ')
    print(f'Введенная последовательность: \n {elements_list}')

    for el in range(0, len(elements_list), 2):  # Бежим по списку с шагом 2
        if el + 1 < len(elements_list):  # Чтобы случайно не вылезти за пределы индекса
            elements_list[el], elements_list[el + 1] = elements_list[el + 1], elements_list[el]
    break
print(f'Результат обработки: \n {elements_list}')
