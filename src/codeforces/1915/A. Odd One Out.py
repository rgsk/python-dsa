

import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    # For getting input from input.txt file
    sys.stdin = open('input.txt', 'r')

    # Printing the Output to output.txt file
    sys.stdout = open('output.txt', 'w')


totalCases = int(input())

while totalCases > 0:
    xor = 0
    for v in input().split(' '):
        xor ^= int(v)
    print(xor)

    totalCases -= 1
