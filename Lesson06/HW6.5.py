"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    _title: str

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    _title = 'Ручка'

    def draw(self):
        print(f'{self._title} написала')


class Pencil(Stationery):
    _title = 'Карандаш'

    def draw(self):
        print(f'{self._title} нарисовал')


class Handle(Stationery):
    _title = 'Маркер'

    def draw(self):
        print(f'{self._title} раскрасил')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
