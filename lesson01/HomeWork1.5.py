"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = int(input('Введите прибыль фирмы >>> '))
costs = int(input('Введите затраты фирмы >>> '))

if proceeds > costs:
    print('Фирма получила прибыль')
    income = proceeds - costs
    print(f'Рентабельность выручки составила {income/proceeds:.2%}')
    employees = int(input('Введите количество сотрудников фирмы >>> '))
    if employees > 0:
        print(f'Прибыль на одного сотрудника составила {income/employees}')
    else:
        print('Введенно некорректное количество сотрудников')
elif proceeds < costs:
    print('Фирма сработала в убыток')
else:
    print('Фирма сработала в ноль')