"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def is_empty(string):
    if string.isspace() or not bool(string):
        return True


products = []
# Тестовые данные, можно раскоментировать чтоб легче проверялось
# products = [(1, {'Product name': 'Computer', 'Price': 100000, 'Quantity': 2, 'Units': 'pcs'}),
#             (2, {'Product name': 'Printer', 'Price': 10000, 'Quantity': 5, 'Units': 'pcs'})]


# Создание базы Товаров, организую в бесконечном цикле меню добавления товаров в базу.
while True:
    print(
        'Структура \"Товары" для вставки нового товара введите \"add", для анализа данных \"analysis", для выхода '
        'введите \"quit"')
    print(*products, sep='\n')
    prompt = input()
    if prompt == 'quit':
        break
    elif prompt == 'add':
        product = input('Введите название товара >>> ')
        if is_empty(product):
            print('Название не можеты быть пустым!')
            continue
        price = input(f'Введите цену на {product} >>> ')
        if not is_digit(price):
            print('Цена должна выражаться числом, разделитель дробной части \".", придется начать сначала')
            continue
        quantity = input(f'Введите количество {product} >>> ')
        if not is_digit(quantity):
            print('Количество должно выражаться числом, разделитель дробной части \".", придется начать сначала')
            continue
        unit = input(f'Введите единицу измерения {product} >>> ')
        if is_empty(unit):
            print('Единица измерения не можеты быть пустой! Придется начать сначала')
            continue
        products.append(
            (len(products) + 1, {'Product name': product, 'Price': price, 'Quantity': quantity, 'Units': unit}))
        # Фомируем анализ базы товаров
    elif prompt == 'analysis':
        if products:
            analysis = {'Product name': set(), 'Price': set(), 'Quantity': set(), 'Units': set()}
            for el in products:
                for feature in el[1]:
                    analysis[feature].add(el[1].get(feature))
            print('===========Результат анализа==========')
            print(analysis)
            print('------------------Выход----------------')
            break
        else:
            print('Нечего анализировать, структура \"Товары" пуста')
    else:
        continue
