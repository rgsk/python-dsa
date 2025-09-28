# export ONLINE_JUDGE=true

def setup(func):
    """
    Decorator that:
      - when ONLINE_JUDGE is set:
        * redirects stdin from input.txt and stdout to output.txt
        * runs the decorated function
        * closes output, compares output.txt with correct_output.txt
        * reports the result to the real console
      - when ONLINE_JUDGE is not set: just runs the function normally
    """
    import os
    import sys

    def wrapper(*args, **kwargs):
        _original_stdout = sys.stdout
        script_directory = os.path.dirname(os.path.realpath(__file__))
        input_file_path = os.path.join(script_directory, 'input.txt')
        output_file_path = os.path.join(script_directory, 'output.txt')
        correct_output_file_path = os.path.join(script_directory, 'correct_output.txt')

        online = os.getenv("ONLINE_JUDGE") is not None

        # --- pre ---
        if online:
            try:
                sys.stdin = open(input_file_path, 'r')
            except Exception:
                # If input.txt doesn't exist, create it so the script doesn't crash
                sys.stdin = open(input_file_path, 'w')
            sys.stdout = open(output_file_path, 'w')

        # --- run ---
        try:
            result = func(*args, **kwargs)
        finally:
            # --- post ---
            if online:
                try:
                    sys.stdout.flush()
                    sys.stdout.close()
                except Exception:
                    pass

                # Compare files and print result to real console
                try:
                    with open(output_file_path, 'r', encoding='utf-8') as f_out:
                        out_raw = f_out.read()
                    with open(correct_output_file_path, 'r', encoding='utf-8') as f_correct:
                        cor_raw = f_correct.read()

                    def normalize(s: str) -> str:
                        # remove BOM, unify newlines, strip ends, collapse internal whitespace per line
                        s = s.lstrip('\ufeff').replace('\r\n', '\n').replace('\r', '\n').strip()
                        return '\n'.join(' '.join(line.split()) for line in s.splitlines())

                    out_norm = normalize(out_raw)
                    cor_norm = normalize(cor_raw)

                    sys.stdout = _original_stdout  # restore console output

                    if out_norm == cor_norm:
                        print("OK: output.txt matches correct_output.txt")
                    else:
                        print("MISMATCH: output.txt differs from correct_output.txt")

                        # Show first differing line (normalized) and also raw reprs for visibility
                        out_lines_raw = out_raw.replace('\r\n','\n').replace('\r','\n').splitlines()
                        cor_lines_raw = cor_raw.replace('\r\n','\n').replace('\r','\n').splitlines()
                        out_lines = out_norm.splitlines()
                        cor_lines = cor_norm.splitlines()
                        max_lines = max(len(out_lines), len(cor_lines))
                        for i in range(max_lines):
                            o = out_lines[i] if i < len(out_lines) else "<missing>"
                            c = cor_lines[i] if i < len(cor_lines) else "<missing>"
                            if o != c:
                                print(f"  Line {i+1}:")
                                print(f"    output : {o}")
                                print(f"    correct: {c}")
                                # Also show the raw strings to expose hidden chars
                                # o_raw = out_lines_raw[i] if i < len(out_lines_raw) else "<missing>"
                                # c_raw = cor_lines_raw[i] if i < len(cor_lines_raw) else "<missing>"
                                # print("  Raw (repr) for that line:")
                                # print(f"    output : {repr(o_raw)}")
                                # print(f"    correct: {repr(c_raw)}")
                                break
                except FileNotFoundError as e:
                    sys.stdout = _original_stdout
                    print(f"COMPARE SKIPPED: {e.filename} not found.")
                except Exception as e:
                    sys.stdout = _original_stdout
                    print(f"COMPARE ERROR: {e}")

        return result
    return wrapper

@setup
def main():
    t = int(input())
    for _ in range(t):
        def solve():
            n, k = [int(v) for v in input().split()]
            a = [int(v) for v in input().split()]

            for i in range(n):
                if a[i] % k == 0:
                    a[i] = k
                else:
                    a[i] = a[i] % k
            items = []
            for i in range(n):
                items.append([a[i], i])
            items.sort(key=lambda x: -x[0])
            order = [str(i + 1) for v, i in items]
            return " ".join(order)
        print(solve())

main()
