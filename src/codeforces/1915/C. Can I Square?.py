

import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    # For getting input from input.txt file
    sys.stdin = open('input.txt', 'r')

    # Printing the Output to output.txt file
    sys.stdout = open('output.txt', 'w')


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
