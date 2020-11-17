class Human:
    # Пример определения атрибутов класса, при таком подходе легче получить некорректное поведение, так,
    # если у экземпляра класса не будет задан атрибут, python этого не заметит
    # age = 0
    # firstname = ''
    # lastname = ''
    # weight = 80

    # Пример определения только типа атрибутов. Более явный подход, он предпочтительнее.
    age: int
    firstname: str
    lastname: str
    weight: int
    _password: str # Protected на уровне соглашения между разработчиками
    __bank_account: str # Private, но при желании можно получить доступ через obj._Human__bank_account

    # Счетчик экземпляров класса
    counter: int = 0

    def info(self):
        print(f'I am {self.firstname}, my age {self.age}, and my weight is {self.weight}')

    # Переопределяем init, для того чтобы определить конструктор объектов класса.
    def __init__(self, firstname, lastname, age, weight=0):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.weight = weight
        Human.counter += 1  # При указании self итерируем counter экземпляра, а при указании класса - counter класса.
        self._init_password()
        self.__bank_account = '100000053' # Private, доступно только внутри класса и методов класса

    def _init_password(self): # Protected на уровне соглашения между разработчиками
        self._password = '1234567890'

    def show_bank_account(self):
        print(f'Account: {self.__bank_account[:5]}******')


john = Human('John', 'Baburo', 27, 80)
print(Human.counter)
artur = Human('Artur', 'Baburo', 50)

print(john._Human__bank_account) # способ получить private
john.show_bank_account()


# artur = Human()

# john.age = 27
# john.weight = 80
# artur.age = 50
# artur.weight = 75
# artur.lastname = 'Baburo'
# artur.firstname = 'Artur'
# john.lastname = 'Baburo'
# john.firstname = 'John'

print(john, artur)
# print(artur.age, artur.lastname, john.weight)
john.info()
artur.info()

print(Human.counter)


