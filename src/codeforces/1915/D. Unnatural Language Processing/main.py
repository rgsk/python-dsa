

import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    sys.stdin = open(input_file_path, 'r')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')


# Greedy


def solve(s: str):
    n = len(s)
    i = 0
    while i + 3 < n:
        if s[i+3] == 'a' or s[i+3] == 'e':
            # CV
            print(s[i:i+2], end="")
            i += 2
        else:
            # CVC
            print(s[i:i+3], end="")
            i += 3
        print('.', end="")
    print(s[i:])


totalCases = int(input())

while totalCases > 0:
    n = int(input())
    string = input()
    solve(string)
    totalCases -= 1
