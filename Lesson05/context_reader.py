with open(r"D:\DevOps\Python\GeekPython\Lesson05\data.txt", "w+") as my_file:
    print('Print to x', file=my_file)
    print(my_file.read())

# print(type(my_file))

try:
    with open(r"D:\DevOps\Python\GeekPython\Lesson05\data.txt") as my_file:
        print(my_file.read())
except IOError:
    print('Some error')
