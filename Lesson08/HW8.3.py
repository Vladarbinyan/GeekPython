"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
только числами. Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не
фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран. Подсказка: для
данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного
элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться.
"""


def str_float(string: str):
    """
    :param string:
    :return: float или None
    """
    try:
        return float(string.replace(',', '.'))
    except ValueError:
        return


class MyNotNumberException(Exception):
    def __str__(self):
        return f'Вводите пожалуйста только числа'


class MyNumbersList:
    def __init__(self):
        self.__numbers_list = []

    def append(self, user_content: str):
        next_number = str_float(user_content)
        if next_number is None:
            raise MyNotNumberException
        else:
            self.__numbers_list.append(next_number)

    def __str__(self):
        return f'Печать списка: {self.__numbers_list}'


numbers = MyNumbersList()

while True:
    user_input = input(
        f'Введите любое число. Для прекращения ввода введите "stop". Печать списка "print" >>> '
    )
    if user_input == 'stop':
        break
    elif user_input == 'print':
        print(numbers)
        continue
    else:
        try:
            numbers.append(user_input)
        except MyNotNumberException as e:
            print(e)
            continue


