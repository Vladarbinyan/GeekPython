"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
"""


class Car:
    _speed: float
    _color: str
    _name: str
    _is_police: bool

    def __init__(self, name, color, speed):
        self._name = name
        self._color = color
        self._speed = speed
        self._is_police = False

    def go(self):
        print(f'{self.name()} поехала')

    def stop(self):
        print(f'{self.name()} остановилась')

    def turn(self, direction):
        print(f'{self.name()} повернула на {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

    def name(self):
        return f'Машина{" полиции" if self._is_police else ""} {self._name}'


class TownCar(Car):
    _speed_limit = 60

    def show_speed(self):
        if self._speed <= self._speed_limit:
            print(f'{self.name()}, текущая скорость {self._speed}')
        else:
            print(f'{self.name()}. Превышение скорости! Текущая скорость {self._speed}, лимит {self._speed_limit}')


class SportCar(Car):
    pass


class WorkCar(Car):
    _speed_limit = 40

    def show_speed(self):
        if self._speed <= self._speed_limit:
            print(f'Текущая скорость {self._speed}')
        else:
            print(f'{self.name()}. Превышение скорости! Текущая скорость {self._speed}, лимит {self._speed_limit}')


class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self._is_police = True


work_car01 = WorkCar('pizza hut01', 'красный', 66)
work_car02 = WorkCar('pizza hut02', 'зеленый', 45)
police_car01 = PoliceCar('dep 01', 'синий', 120)
sport_car = SportCar('драгстер', 'красный', 120)
town_car01 = TownCar('ласточка', 'металлик', 58)

work_car01.go()
work_car01.turn('юг')
work_car01.show_speed()
town_car01.go()
town_car01.show_speed()
town_car01.turn('север')
town_car01.stop()




