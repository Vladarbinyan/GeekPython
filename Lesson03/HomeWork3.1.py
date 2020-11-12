"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(numerator, denominator):
    """
    Функция принимает два числа и выполняет деление
    :param numerator: float
    :param denominator: float
    :return: Результат float или сообщение string
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return f'На ноль делить не умею!' # можно возвращать None


def str_float(string):
    """
    :param string:
    :return: float или None
    """
    try:
        return float(string)
    except ValueError:
        return


params = {'Числитель': float(), 'Знаменатель': float()}
while True:
    for key in params.keys():
        params.update({key: str_float(input(f'Введите {key} >>> '))})
    if None in params.values():
        print(f'Вводите пожалуйста числа!')
        continue
    print(division(params.get('Числитель'), params.get('Знаменатель')))
    break
