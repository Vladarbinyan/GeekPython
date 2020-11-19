class Person:
    _name: str
    _lastname: str
    def __init__(self, name, lastname):
        self._name = name
        self._lastname = lastname
    @property
    def show_name(self):
        return f'{self._name} {self._lastname}'



john = Person('John', 'Doe')
print(john.show_name)
