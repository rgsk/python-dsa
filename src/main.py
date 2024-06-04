import os
import sys

if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    try:
        sys.stdin = open(input_file_path, 'r')
    except Exception as e:
        sys.stdin = open(input_file_path, 'w')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')

MOD = 1000000007


def main():
    n = int(input())
    total = (n * (n + 1)) // 2

    if total % 2 == 0:
        halfSum = total // 2
        dp = [0] * (halfSum + 1)

        for value in range(n + 1, 0, -1):
            prev = dp[:]
            for remaining in range(halfSum + 1):
                if value == n + 1:
                    if remaining == 0:
                        dp[remaining] = 1
                    else:
                        dp[remaining] = 0
                else:
                    if remaining >= value:
                        dp[remaining] = (
                            prev[remaining] +
                            prev[remaining - value]
                        ) % MOD

        res = dp[halfSum]
        print((res * pow(2, MOD - 2, MOD)) % MOD)  # Using modular inverse of 2
    else:
        print(0)


main()
