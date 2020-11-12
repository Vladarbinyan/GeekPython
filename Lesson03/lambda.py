named_lambda = lambda name: f'Hi, {name}!!!'

print(named_lambda('Holly'))

print(
    (lambda name: f"Hi, {name}!!!")
    ("Holly"))


print(
    (lambda x: x ** 2)
    (4))

print(
    (lambda *numbers: type(numbers))
    (4, 6, 8))
