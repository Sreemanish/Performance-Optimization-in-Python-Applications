import random


def generate_students(n):
    return [
        {
            "id": i,
            "name": f"Student_{i}",
            "marks": [random.randint(50,100) for _ in range(5)]
        }
        for i in range(n)
    ]


def calculate_average(students):

    return [
        sum(student["marks"]) / len(student["marks"])
        for student in students
    ]


def find_student(students, target_id):

    student_dict = {
        student["id"]: student
        for student in students
    }

    return student_dict.get(target_id)


def duplicate_check(students):

    seen = set()
    duplicates = []

    for student in students:

        sid = student["id"]

        if sid in seen:
            duplicates.append(student)

        seen.add(sid)

    return duplicates


def top_students(students):

    return sorted(
        students,
        key=lambda x: sum(x["marks"]),
        reverse=True
    )[:10]


def main():

    students = generate_students(5000)

    calculate_average(students)

    find_student(students, 4000)

    duplicate_check(students)

    top_students(students)


if __name__ == "__main__":
    main()