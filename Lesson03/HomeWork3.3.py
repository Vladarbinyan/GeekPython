"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(arg1, arg2, arg3):
    """
    Возвращает сумму наибольших двух аргументов.
    :param arg1: int or float
    :param arg2: int or float
    :param arg3: int or float
    :return: int or float
    """
    args = [arg1, arg2, arg3]
    args.sort(reverse=True)
    return args[0] + args[1]


print(my_func(11, 5.7, 7.8))
