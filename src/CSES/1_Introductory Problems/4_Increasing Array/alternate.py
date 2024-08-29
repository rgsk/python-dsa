import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


def main():
    n = int(input())
    elems = [int(v) for v in input().split()]
    ans = 0
    for i in range(1, n):
        ans += max(0, elems[i-1] - elems[i])
        elems[i] = max(elems[i], elems[i-1])
    print(ans)


main()
