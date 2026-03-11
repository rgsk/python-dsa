from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
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
        mp = defaultdict(int)
        for i in range(n):
            if x - values[i] in mp:
                return f'{mp[x - values[i]] + 1} {i + 1}'
            mp[values[i]] = i
        return 'IMPOSSIBLE'
    print(solve())


if __name__ == "__main__":
    main()
