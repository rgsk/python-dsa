from typing import List


def monotonic(nums: List[int]):
    st: List[int] = []
    ans = [-1] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        while st and st[-1] <= nums[i]:
            st.pop()
        ans[i] = st[-1] if st else -1
        st.append(nums[i])
    return ans


def circular_monotonic(nums: List[int]):
    st: List[int] = []
    n = len(nums)
    ans = [-1] * n
    for i in range(2*n-1, -1, -1):
        while st and st[-1] <= nums[i % n]:
            st.pop()
        if i < n:
            ans[i] = st[-1] if st else -1
        st.append(nums[i % n])
    return ans
