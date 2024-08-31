import os
import sys
from collections import defaultdict

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


def main():
    s = input()
    mp = defaultdict(int)
    for c in s:
        mp[c] += 1
    odd_char = None
    for c in mp:
        if mp[c] % 2:
            if odd_char:
                print("NO SOLUTION")
                return
            odd_char = c
    s1 = ""
    s2 = ""
    for c in mp:
        if c != odd_char:
            half = mp[c]//2
            s1 += c * half
            s2 += c * half
    if odd_char:
        print(s1 + odd_char * mp[odd_char] + s2[::-1])
    else:
        print(s1 + s2[::-1])


main()
