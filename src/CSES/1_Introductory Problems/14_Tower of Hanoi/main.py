import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


def move(n, s, d, a):
    if n == 1:
        print(f'{s} {d}')
        return
    move(n-1, s, a, d)
    print(f'{s} {d}')
    move(n-1, a, d, s)


def main():
    n = int(input())
    steps = 2**n - 1
    print(steps)
    move(n, 1, 3, 2)


main()
