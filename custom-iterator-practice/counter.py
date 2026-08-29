class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        Value = self.current
        self.current += 1
        return Value

for num in Counter(1, 5):
    print(num)

c = Counter(1, 5)
it = iter(c)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
