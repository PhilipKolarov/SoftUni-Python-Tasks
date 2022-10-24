from string import punctuation
punctuation_set = set(punctuation)

def counter(line):
    letter_count = 0
    symbol_count = 0
    for el in line:
        if el.isalpha():
            letter_count += 1
        elif el in punctuation_set:
            symbol_count += 1

    return letter_count, symbol_count


with open('./text_1.txt') as file, open('./output.txt', 'w') as new_file:
    for index, line in enumerate(file):
        letter_count, symbol_count = counter(line)
        new_file.write(f"Line {index + 1}: {line.strip()} ({letter_count}) ({symbol_count})\n")
