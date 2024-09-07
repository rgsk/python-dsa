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
    print(2 ** n % (10 ** 9 + 7))


main()


[["1", "1", "0", "0", "0"],
 ["1", "1", "0", "0", "0"],
 ["0", "0", "1", "0", "0"],
 ["0", "0", "0", "1", "1"]]
