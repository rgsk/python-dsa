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
    s1 = []
    s2 = []
    if n % 4 == 0:
        print('YES')
        while n != 0:
            s1.append(n)
            n -= 1
            s2.append(n)
            n -= 1
            s2.append(n)
            n -= 1
            s1.append(n)
            n -= 1
        print(len(s1))
        print(*s1)
        print(len(s2))
        print(*s2)
    elif n % 4 == 3:
        print('YES')
        while n != 3:
            s1.append(n)
            n -= 1
            s2.append(n)
            n -= 1
            s2.append(n)
            n -= 1
            s1.append(n)
            n -= 1
        s1.append(3)
        s2.append(2)
        s2.append(1)
        print(len(s1))
        print(*s1)
        print(len(s2))
        print(*s2)
    else:
        print('NO')


main()
