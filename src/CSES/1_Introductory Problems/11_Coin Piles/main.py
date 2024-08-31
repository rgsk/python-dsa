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
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        if (a + b) % 3 == 0 and a <= 2*b and b <= 2*a:
            print("YES")
        else:
            print("NO")
        t -= 1


main()
