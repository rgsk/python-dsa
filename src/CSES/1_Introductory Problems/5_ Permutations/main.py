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
    if n == 1:
        print(1)
    elif n <= 3:
        print('NO SOLUTION')
    else:
        # print odds in reverse direction
        s = n if n % 2 else n - 1
        while s > 0:
            print(s, end=' ')
            s -= 2
        # print evens in reverse direction
        s = n if n % 2 == 0 else n - 1
        while s > 0:
            print(s, end=' ')
            s -= 2


main()
