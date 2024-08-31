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
    apples = [int(v) for v in input().split()]
    INT_MAX = (2 ** 31)-1
    ans = INT_MAX

    def solve(i, s1, s2):
        nonlocal ans
        if i == len(apples):
            ans = min(ans, abs(s1 - s2))
            return
        solve(i + 1, s1 + apples[i], s2)
        solve(i + 1, s1, s2 + apples[i])

    solve(0, 0, 0)
    print(ans)


main()
