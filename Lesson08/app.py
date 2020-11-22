import psutil


class Car:
    _model: str
    _price: int

    def __init__(self, model, price):
        self._model = model
        self._price = price


class CarFactory:
    model = 'Uadio'
    common_price = 4000

    def build(self, count=1):
        cars = []
        for i in range(count):
            cars.append(Car(self.model, self.common_price))
        return cars


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f'Не хватает места для машин. Нужно {self.needle} а имеется {self.current}'


class CarStock:
    max_count: int
    cars: list

    def __init__(self, count=0):
        self.max_count = count
        self.cars = []

    def store(self, cars: list):
        if (len(self.cars) + len(cars)) > self.max_count:
            raise CapacityException(self.max_count, len(self.cars) + len(cars))
        self.cars.extend(cars)


class NotEnoughMoneyException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f'Не хватает денег на покупку машины. Нужно {self.needle}, а имеется {self.current}'


class Customer:
    _money: int

    def __init__(self, money):
        self._money = money

    def buy(self, car: Car):
        if car._price > self._money:
            raise NotEnoughMoneyException(self._money, car._price)
        self._money -= car._price


factory = CarFactory()
stock = CarStock(6)
john = Customer(500)

car_list = factory.build(4)
stock.store(car_list)
try:
    john.buy(stock.cars[1])
except NotEnoughMoneyException as exception:
    print(f'У вас не хватает {exception.needle - exception.current}')
    print(exception)
