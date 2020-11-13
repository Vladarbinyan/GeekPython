"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
"""

number = int(input('Введите положительное целое число >>> '))
# Перед первой итерацией проинициализируем значение самой большой цифры, начав с хвоста, и отрежем хвост от нашего числа
maximum = number % 10
head = number // 10
# В цикле продолжим отрезать от хвоста и сравнивать
while head > 0:
    if maximum < head % 10:
        maximum = head % 10
    head = head // 10
else:
    print(f'В числе {number}, самая большая цифра это {maximum}')