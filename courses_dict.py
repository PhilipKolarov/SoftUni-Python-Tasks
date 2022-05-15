courses_dict = {}
input_string = input()
while input_string != "end":
    input_string = list(input_string.split(" : "))
    course_name = input_string[0]
    student_name = input_string[1]
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)
    input_string = input()

for key, value in courses_dict.items():
    print(f"{key}: {len(courses_dict[key])}")
    new_value = "\n-- ".join(value)
    print(f'-- {new_value}')