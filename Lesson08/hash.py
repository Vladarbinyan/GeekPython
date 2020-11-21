name = 'John'

print(hash(name))

tupl = (1, 2, 3)

print(hash(tupl))  # hash работает только с немутабельными значениями


class TestClass:
    firstname: str

    def __init__(self, params):
        self.__firstname = params
        self.my_list = [1, 2, 3]


a = TestClass('Artur')

print(hash(a))  # Не смотря на то что атрибуты класса можно изменять, hash работает на классах


class TestClassMyHash:
    firstname: str

    def __init__(self, params):
        self.__firstname = params
        self.my_list = [1, 2, 3]

    def __hash__(self):
        return hash(self.__firstname)  # Можем переопределить метод и возвращать в функцию hash то что мы хотим


b = TestClassMyHash('Anna')

print(hash(b))
print(b.__hash__()) # Оба варианта эквивалентны
