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
    movies: List[List[int]] = []
    for _ in range(n):
        movies.append(li())
    movies.sort(key=lambda x: x[1])
    last_end = movies[0][1]
    count = 1
    for i in range(1, n):
        if movies[i][0] >= last_end:
            count += 1
            last_end = movies[i][1]
    print(count)


if __name__ == "__main__":
    main()
