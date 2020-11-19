class MyIterator:
    def __init__(self, counter: int):
        self._counter = counter
        self._start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._start += 1
        if self._start >= self._counter:
            raise StopIteration
        else:
            return self._start


for i in MyIterator(10):
    print(i)
