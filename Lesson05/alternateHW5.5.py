import re

with open("file55", "r", encoding="utf-8") as test_file:
    lines = test_file.readlines()
    study = {}
    for line in lines:
        subject, hours = line.strip().split(':')
        hours = re.findall(r'\d+', hours)
        summ = 0
        for hour in hours:
            summ += float(hour)
        study[subject] = summ

print(f'Результат:\n{study}')