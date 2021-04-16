import psutil
import time

# psutil.test()
bt = psutil.boot_time()
print(f'Ваша система была загружена: {time.ctime(bt)}')
print('Активные подлючения')
for con in psutil.net_connections():
    print(con)



