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


def nextPermutation(elems):
    lastRise = -1
    n = len(elems)
    for i in range(n - 1):
        if elems[i+1] > elems[i]:
            lastRise = i
    if lastRise == -1:
        return list(reversed(elems))
    firstElementFromLastGreaterThanLastRise = -1
    for i in range(n - 1, lastRise, -1):
        if elems[i] > elems[lastRise]:
            firstElementFromLastGreaterThanLastRise = i
            break
    elems[lastRise], elems[firstElementFromLastGreaterThanLastRise] = elems[firstElementFromLastGreaterThanLastRise], elems[lastRise]
    elems[lastRise + 1:] = list(reversed(elems[lastRise + 1:]))
    return elems


def getAdjListFromEdges(edges, V):
    adjList = [[] for _ in range(V)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
    return adjList


def getCharacterIndex(c):
    return ord(c) - 97


def getCharacterFromIndex(i):
    return chr(i + 97)
