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
    n, m, k = li()
    applicants = li()
    apartments = li()
    applicants.sort()
    apartments.sort()
    i = 0
    j = 0
    matches = 0
    while i < n and j < m:
        if apartments[j] < applicants[i] - k:
            j += 1
        elif apartments[j] > applicants[i] + k:
            i += 1
        else:
            matches += 1
            i += 1
            j += 1

    print(matches)


if __name__ == "__main__":
    main()
