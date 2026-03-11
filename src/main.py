from bisect import bisect_left, bisect_right
from collections import Counter
from typing import Any, List, Tuple


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
    def solve():
        n, x = li()
        values = li()
        enumerated = [(v, i) for i, v in enumerate(values)]
        enumerated.sort()
        l = 0
        r = n - 1
        while l < r:
            total = enumerated[l][0] + enumerated[r][0]
            if total == x:
                return f'{enumerated[l][1] + 1} {enumerated[r][1] + 1}'
            elif total < x:
                l += 1
            else:
                r -= 1
        return 'IMPOSSIBLE'
    print(solve())


if __name__ == "__main__":
    main()
