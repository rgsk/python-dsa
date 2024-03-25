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

for tc in range(int(input())):
    a, b, c = map(int, input().split())
    print(1 if a < c else -1, end=" ")
    print(b if c < a * b else -1)
