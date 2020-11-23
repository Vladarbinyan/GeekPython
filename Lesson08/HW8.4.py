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

    def __init__(self, brand: str, model: str):
        """
        Базовый класс для оргтехники
        :param brand: Строка содержит имя производителя
        :param model: Модель устройства
        """
        self._brand = brand
        self._model = model


class Printer(Equipment):
    _printing_type: str
    _ppm: int
    _colored: bool
    _paper_size: str

    def __init__(self, brand: str, model: str, printing_type: str, ppm: int, colored: bool, paper_size: str):
        super().__init__(brand, model)
        self._printing_type = printing_type
        self._ppm = ppm
        self._colored = colored
        self._paper_size = paper_size


class Scanner(Equipment):
    _max_resolution: str
    _scanner_type: str
    _auto_feeder: bool

    def __init__(self, brand: str, model: str, max_resolution: str, scanner_type: str, auto_feeder: bool):
        super().__init__(brand, model)
        self._max_resolution = max_resolution
        self._scanner_type = scanner_type
        self._auto_feeder = auto_feeder


class Photocopier(Equipment):
    _ppm: int
    _paper_tray_capacity: int
    _paper_size: str

    def __init__(self, brand: str, model: str, ppm: int, paper_tray_capacity: int, paper_size: str):
        super().__init__(brand, model)
        self._ppm = ppm
        self._paper_tray_capacity = paper_tray_capacity
        self._paper_size = paper_size


printer = Printer('Xerox', 'wc3025', 'laser', 25, True, 'A4')
scanner = Scanner('Epson', 'Perfection V19', '4800dpi', 'Flatbed', False)
photocopier = Photocopier('Ricoh', 'DD 5450', 150, 1500, 'A3')
print(printer.__dict__)
print(scanner.__dict__)
print(photocopier.__dict__)
