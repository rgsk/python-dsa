def C(n, r):
    if r == 0:
        return 1
    if r > n // 2:
        return C(n, n - r)
    return n * C(n - 1, r - 1) // r
