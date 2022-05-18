expression = input()

opening_brackets = []

pairs = {'(': ')', '[': ']', '{': '}'}

balanced = True
for ch in expression:
    if ch in '({[':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        final_opening_brackets = opening_brackets.pop()
        if pairs[final_opening_brackets] != ch:
            balanced = False

    if not balanced:
        break

if not balanced or opening_brackets != []:
    print("NO")
else:
    print("YES")