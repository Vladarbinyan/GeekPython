"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""
from abc import ABC


class NotEnoughEquipment(Exception):
    def __init__(self, item, current, needle):
        self.current = current
        self.needle = needle
        self.item = item

    def __str__(self):
        return f'{self.item} не хватает для списания со склада. Вы запросили {self.needle}, а имеется {self.current}'


class Warehouse:
    _stored_equipment = {}

    def __init__(self, name: str):
        self._name = name

    def put_item(self, item: 'Equipment', amount: int):
        self._stored_equipment.update({item: amount})

    def get_item(self, item: 'Equipment', amount: int):
        if self._stored_equipment.get(item) is None:
            print(f'Позиция {item} отсутствует на складе')
        elif self._stored_equipment.get(item) >= amount:
            self._stored_equipment[item] = self._stored_equipment.get(item) - amount
        else:
            raise NotEnoughEquipment(
                item, self._stored_equipment.get(item), amount)

    @property
    def info(self):
        return f'{self._stored_equipment}'


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

    def __str__(self):
        return f'{self._brand} {self._model}'

    def __repr__(self):
        return self.__str__()


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
print(printer)

store01 = Warehouse('Склад хранения оргтехники')
store01.put_item(printer, 4)
store01.put_item(scanner, 10)
print(store01.info)
store01.get_item(printer, 2)
store01.get_item(photocopier, 2)
print(store01.info)
