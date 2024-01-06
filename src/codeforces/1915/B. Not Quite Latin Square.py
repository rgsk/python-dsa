

import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    # For getting input from input.txt file
    sys.stdin = open('input.txt', 'r')

    # Printing the Output to output.txt file
    sys.stdout = open('output.txt', 'w')


totalCases = int(input())

initial_xor = ord('A') ^ ord('B') ^ ord('C')

while totalCases > 0:
    for _ in range(3):
        xor = initial_xor
        for v in input():
            if v != '?':
                xor ^= ord(v)
        if xor != 0:
            print(chr(xor))

    totalCases -= 1
