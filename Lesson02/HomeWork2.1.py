"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

list_of_any_types = ['text field',
                     55,
                     8484.4388,
                     [1, 2, 3, 4],
                     tuple('string in tuple'),
                     set('string in set'),
                     frozenset('string in frozenset'),
                     dict(name='John', age=10),
                     None,
                     False,
                     bytes([10, 20, 30, 40]),
                     ]

for element in list_of_any_types:
    print(type(element))
