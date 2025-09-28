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
                        out_content = f_out.read().rstrip()
                    with open(correct_output_file_path, 'r', encoding='utf-8') as f_correct:
                        correct_content = f_correct.read().rstrip()

                    sys.stdout = _original_stdout  # restore console output

                    if out_content == correct_content:
                        print("OK: output.txt matches correct_output.txt")
                    else:
                        print("MISMATCH: output.txt differs from correct_output.txt")
                        out_lines = out_content.splitlines()
                        cor_lines = correct_content.splitlines()
                        max_lines = max(len(out_lines), len(cor_lines))
                        for i in range(max_lines):
                            o = out_lines[i] if i < len(out_lines) else "<missing>"
                            c = cor_lines[i] if i < len(cor_lines) else "<missing>"
                            if o != c:
                                print(f"  Line {i+1}:\n    output : {o}\n    correct: {c}")
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

            def getForD(d):
                min_ops = float('inf')
                for i in range(n):
                    rem = a[i] % d
                    min_ops = min(min_ops, 0 if rem == 0 else d - rem)
                return min_ops

            if k == 4:
                count_even = sum(1 for v in a if v % 2 == 0)
                return min(getForD(k), max(0, 2 - count_even))
            else:
                return getForD(k)

        print(solve())

main()
