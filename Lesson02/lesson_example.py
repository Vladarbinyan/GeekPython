# login = None
#
# if login is None:
#     print("Forbidden")
# passport = '5003711042'
# passport_serial = passport[0:4]
# passport_number = passport[4:]
#
# print(f'Серия {passport_serial} и номер {passport_number}')

# Dictionaries

# old_dict = dict(name='John', age=10)
# new_dict = {'name': 'Ivan', 'age': 10}
#
# print(old_dict.keys())
# print(old_dict.values())
#
# print(old_dict['age'])
# print(old_dict.get('age'))
# print(old_dict.get('surname'))
#
# if old_dict.get('surname') is None:
#     print('No key \"surname"')

print(bool(10 > 5))
print(bool(None))

byte_string = b'Hello world!'
simple_string = 'Hello world!'
byte_array_string = bytearray(byte_string)
# bytearray обладает свойствами кортежа, неизменяемость.
# Меньший расход памяти, к примеру: bytearray используют для работы с файлами

print(byte_string)
print(type(byte_string))
print(type(simple_string))
print(type(byte_array_string))

name = 'John'
byte_name = name.encode("UTF-8")
