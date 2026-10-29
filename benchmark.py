import timeit

original_time = timeit.timeit(
    stmt="""
from original_code import main
main()
""",
    number=3
)

optimized_time = timeit.timeit(
    stmt="""
from optimized_code import main
main()
""",
    number=3
)

print("Original Time:", original_time)
print("Optimized Time:", optimized_time)

improvement = (
    (original_time - optimized_time)
    / original_time
) * 100

print(
    f"Performance Improvement: {improvement:.2f}%"
)