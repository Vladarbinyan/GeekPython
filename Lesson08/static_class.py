import random

random.Random


class Operations:
    @staticmethod
    def lower_string(content: str):
        return content.lower()

    @classmethod
    def normalize(cls, content):
        a = cls.lower_string(content)
        return cls.upper_string(a)

    @staticmethod
    def upper_string(content: str):
        return content.upper()


temp_string = 'Hello'
print(Operations.lower_string(temp_string))
print(Operations.normalize(temp_string))
