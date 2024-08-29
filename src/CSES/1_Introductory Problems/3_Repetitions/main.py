import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass


s = input()
cur = s[0]
count = 1
max_count = 1
for i in range(1, len(s)):
    if s[i] != cur:
        max_count = max(max_count, count)
        cur = s[i]
        count = 1
    else:
        count += 1
max_count = max(max_count, count)
print(max_count)
