import sys
from math import ceil
from typing import List

# Redirect standard input to read from the file
# comment this line when submitting the solution
sys.stdin = open('./input.txt', 'r')

# Read the number of test cases
num_test_cases = int(input())

# Create empty lists to store the values of 'a' and 'b'
a_values: List[int] = []
b_values: List[int] = []

# Read 'a' and 'b' values for each test case
for _ in range(num_test_cases):
    a, b = map(int, input().split())
    d = ceil(a/b)
    print(b*d-a)

# Restore standard input to its original state
sys.stdin = sys.__stdin__
