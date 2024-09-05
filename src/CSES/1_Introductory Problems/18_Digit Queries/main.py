import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


def solve(n: int):
    start = 1
    length = 1
    count = 9
    while n > length * count:
        n -= length * count
        length += 1
        start *= 10
        count *= 10
    start += (n - 1) // length
    ans = str(start)[(n-1) % length]
    return ans


def main():
    t = int(input())
    while t > 0:
        n = int(input())
        print(solve(n))
        t -= 1


main()
