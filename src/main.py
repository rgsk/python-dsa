# export ONLINE_JUDGE=true

import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    try:
        sys.stdin = open(input_file_path, 'r')
    except Exception as e:
        sys.stdin = open(input_file_path, 'w')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')

totalCases = int(input())


while totalCases > 0:
    a, b, c = [int(v) for v in input().split()]
    total = a + 2 * b + 3 * c
    if total % 2 == 0:
        print(0)
    else:
        print(1)
    totalCases -= 1
