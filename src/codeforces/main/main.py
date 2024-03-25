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

for tc in range(int(input())):
    n, x = [int(v) for v in input().split()]
    elements = [int(v) for v in input().split()]
    maximum = sum([ceil(v / x) for v in elements])
    minimum = ceil(sum(elements) / x)
    print(f'{minimum} {maximum}')
