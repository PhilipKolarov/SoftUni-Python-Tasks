n = int(input())
unique_elements = set()

for _ in range(n):
    elements = input()
    elements_list = [x for x in elements.split()]
    for el in elements_list:
        unique_elements.add(el)

for el in unique_elements:
    print(el)