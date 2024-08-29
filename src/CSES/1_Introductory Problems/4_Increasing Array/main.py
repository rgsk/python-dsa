import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


n = int(input())
elems = [int(v) for v in input().split()]
max_on_left = elems[0]
ans = 0
for i in range(1, n):
    ans += max(0, max_on_left - elems[i])
    max_on_left = max(max_on_left, elems[i])
print(ans)
