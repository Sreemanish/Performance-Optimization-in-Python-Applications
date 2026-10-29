import random
import time

def generate_students(n):
    students = []

    for i in range(n):
        students.append({
            "id": i,
            "name": f"Student_{i}",
            "marks": [random.randint(50,100) for _ in range(5)]
        })

    return students


def calculate_average(students):

    averages = []

    for student in students:
        total = sum(student["marks"])
        avg = total / len(student["marks"])
        averages.append(avg)

    return averages


def find_student(students, target_id):

    for student in students:

        if student["id"] == target_id:
            return student

    return None


def duplicate_check(students):

    duplicates = []

    for s1 in students:
        count = 0

        for s2 in students:

            if s1["id"] == s2["id"]:
                count += 1

        if count > 1:
            duplicates.append(s1)

    return duplicates


def top_students(students):

    sorted_students = sorted(
        students,
        key=lambda x: sum(x["marks"]),
        reverse=True
    )

    return sorted_students[:10]


def main():

    students = generate_students(5000)

    calculate_average(students)

    find_student(students, 4000)

    duplicate_check(students)

    top_students(students)


if __name__ == "__main__":
    main()