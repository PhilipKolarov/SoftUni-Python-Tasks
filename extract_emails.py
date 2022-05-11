import re

text = input()
expression = r"( |^)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*"
host_expression = r"[a-zA-Z]+(-[a-zA-z]+)*(\.[a-zA-Z]+(-[A-Za-z]+)*)+"

pattern = rf"{expression}@{host_expression}"

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])