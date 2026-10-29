from original_code import generate_students as gen1
from optimized_code import generate_students as gen2

students1 = gen1(100)
students2 = gen2(100)

assert len(students1) == 100
assert len(students2) == 100

assert all("id" in s for s in students1)
assert all("id" in s for s in students2)

assert all("marks" in s for s in students1)
assert all("marks" in s for s in students2)

print("All tests passed successfully")