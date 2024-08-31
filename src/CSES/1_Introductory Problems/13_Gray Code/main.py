import os
import sys
from math import log2

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


def main():
    n = int(input())
    code = [0] * n
    print("".join(map(str, code)))
    for i in range(1, 2**n):
        lsb = i & (-i)
        lsb_index = int(log2(lsb))
        code[lsb_index] ^= 1
        print("".join(map(str, code[::-1])))


main()
