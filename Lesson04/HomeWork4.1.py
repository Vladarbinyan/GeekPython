"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""
import sys


def str_float(string):
    """
    :param string:
    :return: float или None
    """
    try:
        return float(string)
    except ValueError:
        return 0


def salary(hours_worked, hour_rate, allowance):
    return str_float(hours_worked) * str_float(hour_rate) + str_float(allowance)


try:
    file, user, hours_worked, hour_rate, allowance = sys.argv
except ValueError:
    print('Invalid arguments')
    exit()
print(salary(hours_worked, hour_rate, allowance))
