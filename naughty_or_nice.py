def naughty_or_nice_list(santa_list, *args, **kwargs):
    final_list = {'Nice': [], 'Naughty': [], 'Not found': []}

    for command in args:
        is_unique = False
        data = command.split('-')
        num, category = int(data[0]), data[1]
        selected_kid = None
        for el in santa_list:
            if el[0] == num and is_unique:
                is_unique = False
                break
            elif el[0] == num:
                selected_kid = el[1]
                is_unique = True

        if is_unique:
            santa_list.remove((num, selected_kid))
            final_list[category].append(selected_kid)

    for name, category in kwargs.items():
        is_unique = False
        selected_kid = None

        for el in santa_list:
            if name == el[1] and is_unique:
                is_unique = False
                break
            elif name == el[1]:
                selected_kid = el[0]
                is_unique = True

        if is_unique:
            santa_list.remove((selected_kid, name))
            final_list[category].append(name)

    for el in santa_list:
        final_list['Not found'].append(el[1])

    result = ""
    if final_list['Nice'] != []:
        result += f"Nice: {', '.join(final_list['Nice'])}\n"
    if final_list['Naughty'] != []:
        result += f"Naughty: {', '.join(final_list['Naughty'])}\n"
    if final_list['Not found'] != []:
        result += f"Not found: {', '.join(final_list['Not found'])}"

    return result.strip()


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
    ))