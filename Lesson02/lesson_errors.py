
user = {"name": "John"}

try:
    print(user["age"])
except KeyError:
    print('Key not found')

