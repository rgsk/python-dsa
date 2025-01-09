nums = [1, 2, 3, 4, 5]
n = len(nums)
prefix_sum = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    prefix_sum[i] = nums[i - 1] + prefix_sum[i-1]


def get_sum(i, j):
    # j exclusive
    return prefix_sum[j] - prefix_sum[i]


def main():
    for i in range(n):
        for j in range(i, n + 1):
            if sum(nums[i:j]) != prefix_sum[j] - prefix_sum[i]:
                raise Exception('incorrect')
    print('correct')


main()
