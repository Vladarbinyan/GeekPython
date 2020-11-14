import json

with open('person.json', 'r') as file_stream:
    person = json.load(file_stream)


print(person)
print(sum(person['salaries']))

print(json.loads('{"name": "John", "age": 40, "salaries": [100, 200, 160]}')) # пример чтения JSON из строки
