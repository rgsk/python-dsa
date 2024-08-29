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
last_index = 0
max_count = 0
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        max_count = max(max_count, i - last_index)
        last_index = i
max_count = max(max_count, len(s) - last_index)
print(max_count)
