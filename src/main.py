from collections import Counter
from typing import Any, List


def ii():
    return int(input())


def li():
    return list(map(int, input().split()))


def setup(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@setup
def main():
    board = []
    for _ in range(8):
        board.append([v for v in input()])
    diag_tr_to_bl = [False] * 15
    diag_tl_to_br = [False] * 15
    rows = [False] * 8
    cols = [False] * 8

    def update(r, c, val):
        board[r][c] = 'Q' if val else '.'
        rows[r] = val
        cols[c] = val
        diag_tr_to_bl[r + c] = val
        diag_tl_to_br[r - c + 7] = val

    def is_safe(r, c):
        return not rows[r] and \
            not cols[c] and \
            not diag_tr_to_bl[r + c] and \
            not diag_tl_to_br[r - c + 7]

    count = 0

    def helper(r):
        nonlocal count
        if r == 8:
            count += 1
            return
        for c in range(8):
            if is_safe(r, c) and board[r][c] != '*':
                update(r, c, True)
                helper(r + 1)
                update(r, c, False)

    helper(0)
    print(count)


if __name__ == "__main__":
    main()
