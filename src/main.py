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
    n, t = li()
    s = [v for v in input()]
    while t > 0:
        i = 0
        while i < n - 1:
            if s[i] == 'B' and s[i+1] == 'G':
                s[i], s[i+1] = s[i+1], s[i]
                i += 2
            else:
                i += 1
        t -= 1
    print("".join(s))


if __name__ == "__main__":
    main()
