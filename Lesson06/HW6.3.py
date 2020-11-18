"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income = {'wage': float, 'bonus': float}

    def __init__(self, name, surname, position, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии состоавит: {sum(self._income.values())}'


ivanov = Position('Alexander', 'Ivanov', 'manager', 72378.50, 25000.25)

print(ivanov.get_full_name())
print(ivanov.get_total_income())

ivanov.name = 'Boris' # Подправим атрибут
print(ivanov.get_full_name())
