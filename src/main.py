from collections import Counter
from typing import List


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
    arr = []
    for _ in range(3):
        arr.append(li())
    clone = [row[:] for row in arr]
    for i in range(3):
        for j in range(3):
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < 3 and 0 <= nj < 3:
                    clone[ni][nj] += arr[i][j]

    for i in range(3):
        for j in range(3):
            if clone[i][j] % 2:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end='')
        print()


if __name__ == "__main__":
    main()
    main()
