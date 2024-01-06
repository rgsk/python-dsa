

import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    # For getting input from input.txt file
    sys.stdin = open('input.txt', 'r')

    # Printing the Output to output.txt file
    sys.stdout = open('output.txt', 'w')


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
