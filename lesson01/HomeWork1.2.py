"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
в формате чч:мм:сс. Используйте форматирование строк.
"""

counter = 5
while counter > 0:
    time_in_seconds = int(input('Введите время в секундах >>> '))
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds - hours * 3600) // 60
    seconds = time_in_seconds - hours * 3600 - minutes * 60
    print(f'Время по формату чч:мм:сс -> {hours:02}:{minutes:02}:{seconds:02}')
    print('----------------------------------------------------------')
    counter -= 1
else:
    print('done')
