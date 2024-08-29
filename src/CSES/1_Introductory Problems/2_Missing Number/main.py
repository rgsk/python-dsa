import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass

n = int(input())
numbers = [int(v) for v in input().split()]

xor = 0

for i in range(1, n + 1):
    xor ^= i

for v in numbers:
    xor ^= v

print(xor)
