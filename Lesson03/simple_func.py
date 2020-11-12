def hello(name):
    print(f'Hello, {name}!')


def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return


print(calculate(50000))
print(calculate('string'))

