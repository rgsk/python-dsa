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
    n = ii()
    events: List[List[int]] = []
    for _ in range(n):
        a, l = li()
        events.append([a, 1])
        events.append([l, -1])
    events.sort()
    occupied = max_occupied = 0
    for _, delta in events:
        occupied += delta
        max_occupied = max(max_occupied, occupied)
    print(max_occupied)


if __name__ == "__main__":
    main()
