def reverse_text(text):
    i = len(text) - 1
    while i > -1:
        yield text[i]
        i -= 1
