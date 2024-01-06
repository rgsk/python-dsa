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

import math

totalCases = int(input())

while totalCases > 0:
    n = int(input())
    s = sum([int(v) for v in input().split(' ')])
    root = int(math.sqrt(s))
    if root * root == s:
        print("YES")
    else:
        print("NO")

    totalCases -= 1
