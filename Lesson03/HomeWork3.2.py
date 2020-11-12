"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_contacts(**params):
    print(*params)


def is_empty(string):
    if string.isspace() or not bool(string):
        return True

"""
Буду реализовывать с помощью словаря....
"""
# while True:
#     input_string = input('Введите через запятую: имя, фамилия,год рождения, город проживания, email, телефон')
#     if is_empty(input_string):
#         continue
#     else:
#         new_user = input_string.split(',')
#         user_contacts()