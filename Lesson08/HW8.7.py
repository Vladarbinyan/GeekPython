"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber():
    def __init__(self, real: float, imaginary: float):
        self._real = real
        self._imaginary = imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError('Складывать можно только комплексные числа.')
        a1 = self._real
        a2 = other._real
        b1 = self._imaginary
        b2 = other._imaginary
        return ComplexNumber(a1 + a2, b1 + b2)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError('Перемножать можно только комплексные числа.')
        a1 = self._real
        a2 = other._real
        b1 = self._imaginary
        b2 = other._imaginary
        return ComplexNumber(a1 * a2 - b1 * b2, a1 * b2 + b1 * a2)

    def __str__(self):
        return f"z = {self._real} {'+' if self._imaginary > 0 else '-'} {abs(self._imaginary)}i"  # Условие в f строке

    def __repr__(self):
        return self.__str__()


z1 = ComplexNumber(5, -6)
z2 = ComplexNumber(-3, 2)
print('Сложение')
print(z1)
print(z2)
print(z1+z2)

print('Умножение')
z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(-1, 1)
print(z1)
print(z2)
print(z1*z2)
