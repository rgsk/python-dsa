from __future__ import annotations

import builtins
import io
import sys
from functools import wraps

INPUT_TXT_VAR = "input_txt"
OUTPUT_TXT_VAR = "output_txt"


def setup(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        old_input = builtins.input
        old_stdout = sys.stdout
        output_stream = None
        should_check_output = OUTPUT_TXT_VAR in func.__globals__
        try:
            if INPUT_TXT_VAR in func.__globals__:
                input_txt = func.__globals__[INPUT_TXT_VAR]
                stream = io.StringIO(str(input_txt).lstrip("\n"))
                builtins.input = lambda: stream.readline().rstrip("\n")

            if should_check_output:
                old_stdout = sys.stdout
                output_stream = io.StringIO()
                sys.stdout = output_stream

            return func(*args, **kwargs)
        finally:
            builtins.input = old_input
            if should_check_output:
                assert output_stream is not None
                sys.stdout = old_stdout
                output_txt = output_stream.getvalue()
                print(output_txt, end="")
                print(f"------")

                correct_txt = str(func.__globals__[OUTPUT_TXT_VAR])

                def normalize(txt: str) -> str:
                    txt = txt.lstrip("\ufeff").replace(
                        "\r\n", "\n").replace("\r", "\n").strip()
                    return "\n".join(" ".join(line.split()) for line in txt.splitlines())

                output_norm = normalize(output_txt)
                correct_norm = normalize(correct_txt)

                if output_norm == correct_norm:
                    print(f"OK: output matches {OUTPUT_TXT_VAR}")
                else:
                    print(f"MISMATCH: output differs from {OUTPUT_TXT_VAR}")

                    output_lines = output_norm.splitlines()
                    correct_lines = correct_norm.splitlines()
                    max_lines = max(len(output_lines), len(correct_lines))
                    for i in range(max_lines):
                        output_line = output_lines[i] if i < len(
                            output_lines) else "<missing>"
                        correct_line = correct_lines[i] if i < len(
                            correct_lines) else "<missing>"
                        if output_line != correct_line:
                            print(f"  Line {i + 1}:")
                            print(f"    output : {output_line}")
                            print(f"    correct: {correct_line}")
                            break

    return wrapper
