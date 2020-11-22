"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
from abc import ABC


class EquipmentWarehouse:
    pass


class Equipment(ABC):
    _brand: str
    _model: str
    _serial: str
    _price: int

    def __init__(self, brand: str, model: str, serial: str = '', price: int = 0):
        """
        Базовый класс для оргтехники
        :param brand: Строка содержит имя производителя
        :param model: Модель устройства
        :param serial: Серийный номер, необязателен
        :param price: Цена, необязательна
        """
        self._brand = brand
        self._model = model
        self._serial = serial
        self._price = price


class Printer(Equipment):
    _printing_type: str
    _ppm: int
    _colored: bool
    _paper_size: str


class Scanner(Equipment):
    _max_resolution: str
    _type: str
    _auto_feeder: bool


class Photocopier(Equipment):
    _ppm: int
    _paper_tray_capacity: int
    _paper_size: str
