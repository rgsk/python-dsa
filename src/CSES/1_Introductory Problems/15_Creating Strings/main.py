import os
import sys
from typing import List

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass

ans = []


def solve(i: int, s: List[str]):
    if i == len(s):
        ans.append("".join(s))
        return
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            continue
        seen.add(s[j])
        s[i], s[j] = s[j], s[i]
        solve(i+1, s)
        s[j], s[i] = s[i], s[j]


def main():
    s = [v for v in input()]
    solve(0, s)
    print(len(ans))
    ans.sort()
    for v in ans:
        print(v)


main()
