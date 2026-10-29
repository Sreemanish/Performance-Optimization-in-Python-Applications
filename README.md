# Performance Optimization in Python Applications

## Project Overview

This project focuses on identifying and optimizing performance bottlenecks in a Python application. The application processes student records and performs operations such as average calculation, student lookup, duplicate detection, and ranking top-performing students.

The primary objective was to analyze performance using profiling tools, identify inefficient code segments, apply optimization techniques, and compare execution times before and after optimization.

## Project Structure

Performance Optimization/

├── original_code.py
├── optimized_code.py
├── benchmark.py
├── test_functionality.py
├── performance_report.md
├── README.md
├── original_profile.txt
└── optimized_profile.txt

## Technologies Used
* Python 3
* cProfile
* timeit

## Performance Analysis
The original application was profiled using cProfile to identify performance bottlenecks.

The analysis revealed that the duplicate_check() function consumed the majority of the execution time due to its nested loop implementation.

### Original Complexity

* Duplicate Detection: O(n²)
* Student Search: O(n)

### Optimized Complexity
* Duplicate Detection: O(n)
* Student Search: O(1)

## Optimization Techniques
1. Replaced nested loops with set-based duplicate detection.
2. Used dictionary lookups for faster student retrieval.
3. Applied list comprehensions to improve processing speed.
4. Reduced redundant computations and unnecessary iterations.

## Benchmark Results
Metric	Original	Optimized
Execution Time	2.590 sec	0.033 sec
Performance Improvement	-	98.71%

## Testing
The application was tested after optimization to verify that functionality remained unchanged.
Run:
python test_functionality.py
Expected Output:
All tests passed successfully

## Profiling
Generate profiling reports using:
* python -m cProfile original_code.py > original_profile.txt
* python -m cProfile optimized_code.py > optimized_profile.txt

## Conclusion
The project successfully demonstrates how proper algorithm selection and efficient data structures can significantly improve application performance. The optimized version achieved a 98.71% reduction in execution time while maintaining functional correctness.