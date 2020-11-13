# import time
from time import time as std_time, sleep

start = std_time()

print(f'Started at {start}')
sleep(2)
print(f'End at {std_time()}')
