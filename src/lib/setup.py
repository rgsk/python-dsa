from __future__ import annotations

import builtins
import io
from functools import wraps


def setup(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        old_input = builtins.input
        try:
            input_txt = func.__globals__["input_txt"]
            stream = io.StringIO(str(input_txt).lstrip("\n"))
            builtins.input = lambda: stream.readline().rstrip("\n")
            return func(*args, **kwargs)
        finally:
            builtins.input = old_input

    return wrapper
