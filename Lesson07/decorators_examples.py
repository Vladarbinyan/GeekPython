#
# def my_calculator(operator):
#     def my_sum(a=7, b=6):
#         return a+b
#     def my_diff(a=7, b=6):
#         return a-b
#     if operator == '+':
#         return my_sum
#     if operator == '-':
#         return my_diff
#
#
# calcsum = my_calculator('+')
#
# print(calcsum())

import time


def my_timer(func):
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        delta_time = time.time() - start_time
        print(f'Время выполнения функции {delta_time}')
        return result

    return tmp


@my_timer
def my_sum(x, y):
    # time.sleep(0.0000001)
    return x + y


print(my_sum(5500000000000005454, 23546464646464))


def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('functions.log', 'a', encoding='utf-8') as logfile:
            logfile.write(
                f'Function name: {func.__name__} with result = {result}. Start at {time.ctime(time.time())}\n'
            )
        return result

    return wrapper


@my_timer
@logging
def my_diff(x, y):
    # time.sleep(0.0000001)
    return x - y


print(my_diff(5500000000000005454, 23546464646464))
