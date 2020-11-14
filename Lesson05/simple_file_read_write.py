my_file = open(
    r"D:\DevOps\Python\GeekPython\Lesson05\data.txt", "w")  # r raw или сырая строка. Можно применять для пути к
# файлу, второй параметр вид доступа к файлу (например w, a, r)

# print(my_file.readline())

# for line in my_file.readlines():
#     print(line.replace('\n', ''))

# print(my_file.read())

# for data in my_file.read(1024):
#     print(data)

print(my_file.closed)
print(my_file.mode)
print(my_file.name)

if my_file.writable():
    my_file.write('New line\n')

    strings = ['John\n', 'Kate\n']
    my_file.writelines(strings)
else:
    print('error')

my_file.close()
