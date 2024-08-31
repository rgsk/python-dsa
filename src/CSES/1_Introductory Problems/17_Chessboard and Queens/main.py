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
    board = []
    for _ in range(8):
        board.append([v for v in input()])

    def is_safe(r, c):
        for i in range(r + 1):
            if board[i][c] == 'Q':
                return False
            if c-i >= 0 and board[r-i][c-i] == 'Q':
                return False
            if c+i < 8 and board[r-i][c+i] == 'Q':
                return False
        return True

    count = 0

    def solve(r):
        nonlocal count
        if r == 8:
            count += 1
            return
        for c in range(8):
            if is_safe(r, c) and board[r][c] != '*':
                board[r][c] = 'Q'
                solve(r + 1)
                board[r][c] = '.'

    solve(0)
    print(count)


main()
