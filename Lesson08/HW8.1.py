"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class MyData:
    _day: int
    _month: int
    _year: int

    def __init__(self, content: str):
        self.__content = content
        self._day, self._month, self._year = self.extractor(content)

    @classmethod
    def extractor(cls, content: str):
        tmp = content.split('-')
        tmp = [int(i) for i in tmp]
        if cls.validator(tmp):
            day, month, year = tmp
            return day, month, year
            # return f'Вы указали: {day} число, {month} месяц, {year} год' Если лишить класс атрибутов и
            # конструктора, и оставить только методы extractor и validator то можем сразу возвращать строку.
        else:
            return None

    @staticmethod
    def validator(content: list):
        # Упрощенная валидация. Валидатор не учитывает различие в количестве дней в разных месяцах
        if not 0 < content[0] <= 31:
            raise ValueError('День месяца должен находится в диапазоне от 1 до 31')
        elif not 0 < content[1] <= 12:
            raise ValueError('Месяц должен находится в диапазоне от 1 до 12')
        elif not 1900 < content[2] <= 2999:
            raise ValueError('Год должен находится в диапазоне от 1900 до 2999')
        else:
            return True

    def __str__(self):
        return f'Вы указали: {self._day} число, {self._month} месяц, {self._year} год'


dat = MyData('15-03-1983')
print(dat)
print(MyData('11-12-2000'))
