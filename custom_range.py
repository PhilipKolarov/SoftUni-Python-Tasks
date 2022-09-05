class custom_range:
    def __init__(self, first, final):
        self.first = first
        self.final = final
        self.next_value = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value > self.final:
            raise StopIteration

        return_value = self.next_value
        self.next_value += 1
        return return_value

