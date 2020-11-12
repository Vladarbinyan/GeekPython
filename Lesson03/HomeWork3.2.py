"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

params = {'имя': str(), 'фамилия': str(), 'год рождения': str(), 'город проживания': str(), 'email': str(), 'телефон': str()}


def print_user(**params):
    """ Функция печатает словарь где ключи это названия переданных параметров, и соответсвующие им значения """
    print(params)


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


while True:
    print('\"Данные пользователя." Меню: add - добавить запись, print - вывести запись, quit - выход')
    prompt = input('Введите команду: ')
    if prompt == 'add':
        for key in params.keys():
            params.update({key: input(f'{key} >>> ')})
    elif prompt == 'print':
        print_user(
            имя=params.get('имя'),
            фамилия=params.get('фамилия'),
            год_рождения=params.get('год рождения'),
            город_проживания=params.get('город проживания'),
            email=params.get('email'),
            телефон=params.get('телефон')
        )
    elif prompt == 'quit':
        break
    continue

