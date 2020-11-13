def user_generator():
    for user in ['Vasya', 'Petya', 'Nina']:
        yield user


print(user_generator()) # Сам генератор
print(user_generator().__next__()) # Генерируем следующее значение. Если выйти за пределы генератора можно получить
# StopIteration
for user_item in user_generator(): # При обращении к генератору из цикла, StopIteration ведет к завершению цикла
    print(user_item)
