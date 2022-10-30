collection = ["-", ",", ".", "!", "?"]

with open('./text_1.txt', 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for symbol in collection:
                result = result.replace(symbol, '@')
            print(result)
        index += 1