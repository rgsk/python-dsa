# export ONLINE_JUDGE=true
 
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
 

def main():
    n = int(input())
    for _ in range(n):
        def solve():
            n, k, q = [int(v) for v in input().split()]
            tempratures = [int(v) for v in input().split()]
            consecutive_valid_temps = []
            valid_temp_count = 0
            for temp in tempratures:
                if temp <= q:
                    valid_temp_count += 1
                else:
                    if valid_temp_count > 0:
                        consecutive_valid_temps.append(valid_temp_count)
                    valid_temp_count = 0
            if valid_temp_count > 0:
                consecutive_valid_temps.append(valid_temp_count)
            ans = 0
            for temp_count in consecutive_valid_temps:
                if temp_count >= k:
                    for i in range(k, temp_count + 1):
                        ans += temp_count - i + 1
            return ans

        print(solve())
 
main()