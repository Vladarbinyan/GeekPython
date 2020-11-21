class Printable:
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Person(Printable):
    def __init__(self, name):
        self._name = name
        self._age = 10


john = Person('John')
print(john)
