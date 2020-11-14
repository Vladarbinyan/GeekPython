"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import cycle, count


def my_iterator(start):
    for el in count(start):
        if el > 10:
            break
        else:
            yield el


def my_list_iterator(*any_list):
    c = 0
    for el in cycle(any_list):
        if c > 10:
            break
        else:
            c += 1
            yield el


for i in my_iterator(3):
    print(i)

names = ['Adam', 'Alex', 'Anna', 'Artur', 'Gleb']

for name in my_list_iterator(*names):
    print(name)
