n = int(input())
student_strings = [input() for _ in range(n)]

students_grades = {}

for student in student_strings:
    name, grade_string = student.split(" ")
    grade = float(grade_string)
    if name not in students_grades:
        students_grades[name] = []

    students_grades[name].append(grade)

for student, grades in students_grades.items():
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_average = f"{(sum(grades) / len(grades)):.2f}"
    print(f'{student} -> {grades_formatted} (avg: {grades_average})')

