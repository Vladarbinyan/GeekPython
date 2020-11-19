from abc import ABC, abstractmethod


class AbstractUser(ABC):
    @abstractmethod
    def show_name(self):
        pass


class Person(AbstractUser):

    def show_name(self):
        print('It`s a person')


class User(AbstractUser):

    def show_name(self):
        print('It`s a user')


class CompositeUser(AbstractUser):
    def __init__(self, children: list):
        self._children = children

    def show_name(self):
        for item in self._children:
            item.show_name()


p = Person()
u = User()
compose = CompositeUser([p, u])
compose.show_name()
