class Person:
    _first_name: str
    _last_name: str

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def fullname(self):
        return f'{self._first_name} {self._last_name}'


class User(Person):
    login: str
    password: str

    def __init__(self, first_name: str, last_name: str, login: str): # Перегрузка конструктора класса
        super().__init__(first_name, last_name)
        self.login = login

    def log_in(self):
        print(f'Welcome, {self.fullname()}!')

class InfoPrinter:
    def info(self, class_object):
        if isinstance(class_object, Person): # Метод isinstance определяет класс к которому относится экземпляр,
            # необходимо учитывать что при наследовании экземпляр имеет отношение ко всем вышестоящим предкам. Данный
            # пример показывает что такая проверка будет работать некорректно, так как User унаследован от Person
            print('It`s a class - Person')
        elif isinstance(class_object, User):
            print('It`s a class - User')
        else:
            print('Unknown class/type')


john = User('John', 'Doe', 'johny')
john.log_in()
artur = Person('Artur', 'Doe')
printer = InfoPrinter()

printer.info(john)
printer.info(artur)
printer.info(printer)
printer.info([])
