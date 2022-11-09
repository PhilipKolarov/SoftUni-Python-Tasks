input_string = input()
n, m = [int(x) for x in input_string.split()]
n_set = set()
unique_set = set()

for _ in range(n):
    element = input()
    n_set.add(element)

for _ in range(m):
    element = input()
    if element in n_set:
        unique_set.add(element)

for el in unique_set:
    print(el)

#Or add m element to m_set and then do result = n_set.intersection(m_set) and print individual elements in result