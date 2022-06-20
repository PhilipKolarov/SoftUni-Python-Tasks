n = int(input())
intersection_longest = set()

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = [int(num) for num in first_range.split(',')]
    second_start, second_end = [int(num) for num in second_range.split(',')]

    first_set = set(range(first_start, first_end+1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(intersection_longest):
        intersection_longest = intersection

print(f"Longest intersection is [{', '.join([str(a) for a in intersection_longest])}] with length {len(intersection_longest)}")


