class Salary:
    _amount: int
    _vat: int
    _multiply: int

    def __init__(self, amount: int, vat: int = 0, multiply: int = 1):
        self._amount = amount
        self._vat = vat
        self._multiply = multiply

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._amount < other
        elif isinstance(other, Salary):
            return self._amount < other

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._amount > other
        elif isinstance(other, Salary):
            return self._amount > other

    def __eq__(self, other: 'Salary'):
        return self._amount == other._amount and self._vat == other._vat and self._multiply == other._myltiply


junior = Salary(200)
middle = Salary(500)
senior = Salary(1000)

print(junior > middle)
print(junior < 400.324)
print(junior == senior)
