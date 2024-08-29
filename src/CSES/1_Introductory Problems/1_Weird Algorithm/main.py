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

while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
print(1)
