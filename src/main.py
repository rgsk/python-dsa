# export ONLINE_JUDGE=true

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
    n = int(input())
    values = [int(v) for v in input().split()]
    values.sort()
    median_idx = ceil(n/2) - 1
    ops = 1
    i = median_idx + 1
    while i < n and values[i] == values[median_idx]:
        i += 1
        ops += 1
    print(ops)
    t -= 1
