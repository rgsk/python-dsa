import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(script_directory, 'input.txt')):
    sys.stdin = open(os.path.join(script_directory, 'input.txt'), 'r')
    try:
        sys.stdout = open(os.path.join(script_directory, 'output.txt'), 'w')
    except Exception as e:
        pass

ways = 0
visited = [[False for _ in range(7)] for _ in range(7)]
path = ""


def is_valid(i: int, j: int):
    return i >= 0 and j >= 0 and i < 7 and j < 7 and (not visited[i][j])


def dfs(i: int, j: int, steps: int):
    global ways
    if i == 6 and j == 0:
        if steps == 48:
            ways += 1
        return
    if (is_valid(i+1, j) and is_valid(i-1, j)) and (not is_valid(i, j-1) and not is_valid(i, j+1)):
        return
    if (is_valid(i, j+1) and is_valid(i, j-1)) and (not is_valid(i+1, j) and not is_valid(i-1, j)):
        return

    visited[i][j] = True
    if (path[steps] == '?' or path[steps] == 'D') and is_valid(i + 1, j):
        dfs(i + 1, j, steps + 1)
    if (path[steps] == '?' or path[steps] == 'U') and is_valid(i - 1, j):
        dfs(i - 1, j, steps + 1)
    if (path[steps] == '?' or path[steps] == 'R') and is_valid(i, j + 1):
        dfs(i, j + 1, steps + 1)
    if (path[steps] == '?' or path[steps] == 'L') and is_valid(i, j - 1):
        dfs(i, j - 1, steps + 1)
    visited[i][j] = False


def main():
    global path
    path = input()
    dfs(0, 0, 0)
    print(ways)


main()
