import os
import sys
from math import ceil

if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    try:
        sys.stdin = open(input_file_path, 'r')
    except Exception as e:
        sys.stdin = open(input_file_path, 'w')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')

t = int(input())

while t > 0:
    a, b = [int(v) for v in input().split(' ')]
    c = ceil(a/b)
    print(c*b - a)
    t -= 1
