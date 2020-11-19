class MyIterator:
    def __init__(self, counter: int, start=0):
        self._counter = counter
        self._start = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self._start += 1
        if self._start >= self._counter:
            raise StopIteration
        else:
            return self._start


for i in MyIterator(15, 1):
    print(i)
