"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
весна, лето, осень). Напишите решения через list и через dict.
"""

list_months = ['Зима', 'Зима',
               'Весна', 'Весна', 'Весна',
               'Лето', 'Лето', 'Лето',
               'Осень', 'Осень', 'Осень',
               'Зима']  # Индекс это номер месяца минус единица
dict_months = {12: 'Зима', 1: 'Зима', 2: 'Зима',
               3: 'Весна', 4: 'Весна', 5: 'Весна',
               6: 'Лето', 7: 'Лето', 8: 'Лето',
               9: 'Осень', 10: 'Осень', 11: 'Осень'}  # Ключи соотвествуют номерам месяца
# Реализация словаря от Geekbrains
dict_months_gb = {'Зима': (12, 1, 2),
                  'Весна': (3, 4, 5),
                  'Лето': (6, 7, 8),
                  'Осень': (9, 10, 11)}

# Бесконечный цикл, пока пользователь не введет то что нужно
while True:
    month = input('Введите номер месяца от 1 до 12 >>> ')
    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            print(f'Вы ввели {month}')
            print(f'Месяц по списку {list_months[month - 1]}')
            print(f'Месяц по словарю {dict_months.get(month)}')
            for season, months in dict_months_gb.items():
                if month in months:
                    print(f'Месяц по словарю (Решение ДЗ GB) {season}')
                    break
            break
    print('Вы ошиблись при вводе')
