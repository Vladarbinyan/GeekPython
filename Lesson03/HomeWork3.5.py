"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""
total = 0


def adder(*numbers):
    global total
    for el in numbers:
        if el == 'q':
            return 'stop'
        current = str_float(el)
        if current is not None:
            total += current
    return


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


def str_float(string):
    """
    :param string:
    :return: float или None
    """
    try:
        return float(string)
    except ValueError:
        return


while True:
    input_string = input(
        'Введите строку чисел разделенных пробелами, для завершения работы вместо числа введите символ \"q" \n'
    )
    if is_empty(input_string):
        print('Пустая строка')
        continue
    else:
        numbers = input_string.split()
        result_code = adder(*numbers)
        print(total)
        if result_code == 'stop':
            break
