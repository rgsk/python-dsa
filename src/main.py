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
    n = int(input())
    while n != 1:
        print(n, end=" ")
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
    print(1)


main()
