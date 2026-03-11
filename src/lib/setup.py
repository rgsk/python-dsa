from __future__ import annotations

import builtins
from functools import wraps


def setup(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        old_input = builtins.input
        try:
            input_txt = func.__globals__["input_txt"]
            tokens = iter(str(input_txt).split())
            builtins.input = lambda: next(tokens)
            return func(*args, **kwargs)
        finally:
            builtins.input = old_input

    return wrapper


def ii():
    return int(input())


def li():
    return list(map(int, input().split()))
