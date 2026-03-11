from bisect import bisect_left, bisect_right
from collections import Counter


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
    n, m = li()
    tickets = li()
    customers = li()

    counts = Counter(tickets)
    values = sorted(counts)
    parent = list(range(len(values)))

    def find(x):
        if x < 0:
            return -1
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for max_price in customers:
        i = bisect_right(values, max_price) - 1
        i = find(i)

        if i == -1:
            print(-1)
            continue

        price = values[i]
        print(price)
        counts[price] -= 1
        if counts[price] == 0:
            parent[i] = find(i - 1)


if __name__ == "__main__":
    main()
