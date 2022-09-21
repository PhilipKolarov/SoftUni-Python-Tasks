class vowels:
    vowels_string = 'eyuioa'

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].lower() not in self.vowels_string:
                self.index += 1
                continue

            new_value = self.text[self.index]
            self.index += 1
            return new_value

        raise StopIteration
