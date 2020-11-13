def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return


def hello(name):
    print(f'Hello, {name}!')
