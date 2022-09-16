class dictionary_iter:
    def __init__(self, data):
        self.data = list(data.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration
        result = self.data[self.i]
        self.i += 1
        return result


result = dictionary_iter({"name": "Peter", "age": 24})

for x in result:
    print(x)