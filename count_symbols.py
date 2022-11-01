input_string = input()
symbols = {}

for el in input_string:
    if el in symbols:
        symbols[el] += 1
    else:
        symbols[el] = 1

for el, qty in sorted(symbols.items()):
    print(f"{el}: {qty} time/s")