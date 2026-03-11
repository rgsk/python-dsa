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
    n, x = li()
    weights = li()
    weights.sort()
    gondolas = 0
    l = 0
    r = n - 1
    while l <= r:
        if l == r:
            l += 1
        elif weights[l] + weights[r] <= x:
            l += 1
            r -= 1
        else:
            r -= 1
        gondolas += 1
    print(gondolas)


if __name__ == "__main__":
    main()
