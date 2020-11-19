"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать перегрузку
метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        for row in matrix:
            if len(row) != self._cols:
                print('матрица должна быть прямоугольной')
                raise ValueError  # Возможность создавать новые матрицы через try
        self.__matrix = matrix

    def __str__(self):
        matrix_print = '\n'
        for row in self.__matrix:
            for el in row:
                matrix_print += f'{el:5d}'
            matrix_print += '\n'
        return matrix_print

    def __add__(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            print('Второй объект не матрица')
            raise ValueError
        if self._rows != other._rows or self._cols != other._cols:
            print('Нельзя складывать матрицы разной размерности')
            raise ValueError
        result_matrix = []
        for row in range(self._rows):
            new_row = []
            for el in range(self._cols):
                new_row.append(self.__matrix[row][el] + other.__matrix[row][el])
            result_matrix.append(new_row)
        return Matrix(result_matrix)


m0 = Matrix([[31, 22], [37, 43], [51, 86]])
m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(m1)
print(m2)
print(m3)

try:
    m4 = m0 + m1
except ValueError:
    print('Можно складывать только матрицы, которые обладают одинаковой размерностью')

try:
    m4 = m1 + m2
except ValueError:
    print('Проверьте операнды')

print(m4)
