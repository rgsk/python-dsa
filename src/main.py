# export ONLINE_JUDGE=true

import os
import sys
from math import log2

if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    try:
        sys.stdin = open(input_file_path, 'r')
    except Exception as e:
        sys.stdin = open(input_file_path, 'w')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')


def main():
    t = int(input())
    while t > 0:
        n, f, k = [int(v) for v in input().split()]
        arr = [int(v) for v in input().split()]
        favourite = arr[f - 1]
        arr.sort(reverse=True)
        value = arr[k - 1]
        if value < favourite:
            print("YES")
        elif value > favourite:
            print("NO")
        else:
            if k < n and arr[k] == favourite:
                print("MAYBE")
            else:
                print("YES")
        t -= 1


main()
