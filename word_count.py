import re

def read_words():
    with open('./words.txt', 'r') as file:
        return file.read().split(' ')

def count_words_in_file(words):
    words_count = {
        word: 0 for word in words
    }

    with open('./text1.txt', 'r') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                words_count[word] += words_in_line.count(word)

    return words_count

words_count = count_words_in_file(read_words())

[
    print(f"{w} - {c}") for w, c in sorted(words_count.items(), key=lambda x: x[1], reverse=True)
]