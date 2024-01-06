import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    try:
        sys.stdin = open(input_file_path, 'r')
    except Exception as e:
        sys.stdin = open(input_file_path, 'w')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')

totalCases = int(input())

initial_xor = ord('A') ^ ord('B') ^ ord('C')

while totalCases > 0:
    for _ in range(3):
        xor = initial_xor
        for v in input():
            if v != '?':
                xor ^= ord(v)
        if xor != 0:
            print(chr(xor))

    totalCases -= 1
