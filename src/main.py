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
    n = ii()
    arr = li()
    arr.sort()
    distinct = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            distinct += 1
    print(distinct)


if __name__ == "__main__":
    main()
