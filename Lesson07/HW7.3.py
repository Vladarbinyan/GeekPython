"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно. Сложение. Объединение двух
клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют две
клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение. Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух клеток. В классе необходимо реализовать метод
make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по
рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся. Например,
количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****. Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, cell_size: int):
        assert cell_size > 0, 'Задайте размер клетки целым числом больше нуля'
        self.__cell_size = cell_size

    def __str__(self):
        return f'Клетка размером {self.__cell_size}'

    def __add__(self, other):
        self.validate_item(other)
        return Cell(self.__cell_size + other.__cell_size)

    def __sub__(self, other):
        self.validate_item(other)
        value = self.__cell_size - other.__cell_size
        assert value > 0, 'Результат вычитания клеток должен быть больше нуля'
        return Cell(value)

    def __mul__(self, other):
        self.validate_item(other)
        return Cell(self.__cell_size * other.__cell_size)

    def __truediv__(self, other):
        self.validate_item(other)
        return Cell(self.__cell_size // other.__cell_size)

    def make_order(self, cols):
        if not isinstance(cols, int) or cols < 1:
            print('Задайте количество ячеек в ряду целым числом больше нуля')
            raise ValueError
        else:
            ordered_cell = ''
            for i in range(self.__cell_size // cols):
                ordered_cell += '*' * cols + '\n'
            ordered_cell += '*' * (self.__cell_size % cols) + '\n'
            return ordered_cell

    def validate_item(self, other):
        assert isinstance(other, self.__class__), 'Операции допустимы только между клетками'


cell01 = Cell(14)
print(cell01.make_order(5))

cell02 = Cell(7)
cell03 = cell01 + cell02
cell04 = cell02 - cell01
cell05 = cell03 - cell02
cell06 = cell03 / cell02

print(f'Умножение клеток: {cell01} * {cell02} = {cell01 * cell02}')
print(f'Деление клеток: {cell01} / {cell02} = {cell01 / cell02}')
print(f'Сложение клеток: {cell01} + {cell02} = {cell01 + cell02}')
print(f'Вычитание клеток: {cell01} - {cell02} = {cell01 - cell02}')
