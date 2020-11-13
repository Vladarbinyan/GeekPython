import itertools

for x in itertools.count(100, 10):
    if x > 200:
        break
    print(x)
print('done')
