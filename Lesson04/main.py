import sys
from Lesson04 import my_mod


try:
    file, user, salary = sys.argv
except ValueError:
    print('Invalid arguments')
    exit()

my_mod.hello(user)
print(my_mod.calculate(int(salary)))


