"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
+ 33 + 333 = 369.
"""

number = input('Введите число >>> ')

# Решение без цикла

nnn = int(number * 3)
nn = int(number * 2)
n = int(number)
print('Решение без цикла')
print(f'{n} + {nn} + {nnn} = {n + nn + nnn}')


print('Решение с помощью цикла')
counter = 0
result = 0
while counter < 3:
    if counter > 0:
        print('+')
    counter += 1
    print(int(number * counter))
    result += int(number * counter)
else:
    print(f'= {result}')
