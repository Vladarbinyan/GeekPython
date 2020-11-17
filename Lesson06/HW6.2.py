"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _name: str
    _length: float
    _width: float
    __asphalt_density = 2500  # 25кг * 1м * 1м * 100см = 2500кг.

    def __init__(self, name, length, width):
        self._name = name
        self._length = length
        self._width = width

    def info(self):
        return f'{self._name}: длина - {self._length}м; ширина - {self._width}м.'

    def calc(self, thickness):
        asphalt_mass = self._length * self._width * self.__asphalt_density / 1000 * thickness / 100
        return f'Для покрытия {self.info()} толщиной {thickness}см. понадобится {asphalt_mass} тонн асфальта'


m51 = Road('Трасса м51', 20, 5000)
print(m51.info())
print(m51.calc(5))
