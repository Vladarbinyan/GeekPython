class Person:
    def __init__(self, attrs: dict):
        self._attributes = attrs

    def __del__(self):
        print('Person removed')

    def __str__(self):
        return f'Person: {self._attributes["name"]} {self._attributes["lastname"]}'

    def __repr__(self):  # representation переадресация вызова на str. Для корректного отображения, например в списке,
        return self.__str__()

    def __getitem__(self, item):
        return self._attributes[item]

    def __setattr__(self, key, value):
        if '_attributes' in self.__dict__:
            self._attributes[key] = value
        else:
            super().__setattr__(key, value)


john = Person({'name': 'John', 'lastname': 'Doe', 'age': 30})
artur = Person({'name': 'Artur', 'lastname': 'Doe', 'age': 40})

# del john
users = [john, artur]
# print(john._attributes.values())
# print(john)

john.job = 'Developer'
print(users)  # работает благодаря __repr__
print(john['name'])
print(john['job'])
print(artur['name'])
