"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionException(Exception):
    def __str__(self):
        return f'Вы пытаетесь делить на ноль. Выполнение операции невозможно!'


def my_div(nominator, denominator):
    if denominator == 0:
        raise MyZeroDivisionException
    else:
        return nominator / denominator


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
    user_input = input(f'Введите два числа, в качестве разделителя укажите символ "/" (например 5/6) >>> ')
    try:
        nominator, denominator = user_input.split('/')
    except ValueError:
        print('Ошибка ввода!')
        continue
    nominator = str_float(nominator)
    denominator = str_float(denominator)
    if nominator is None or denominator is None:
        print('Пожалуйста вводите только числа')
        continue
    else:
        try:
            print(f'Результат деления: {my_div(nominator, denominator)}')
            break
        except MyZeroDivisionException as exception:
            print(exception)
