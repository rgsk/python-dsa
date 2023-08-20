# https://leetcode.com/problems/same-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(getList(self))


def formTree(values: list[int | None]):
    if not values:
        return None
    root = TreeNode(values[0])
    queue: List[Optional[TreeNode]] = [root]
    i = 1
    while i < len(values):
        top = queue.pop(0)
        if top is not None:
            top.left = TreeNode(values[i]) if values[i] != None else None
            i += 1
            queue.append(top.left)
            if i < len(values):
                top.right = TreeNode(values[i]) if values[i] != None else None
                i += 1
                queue.append(top.right)
        else:
            continue
    return root


def getList(root: Optional[TreeNode]):
    ans: list[None | int] = []
    queue = [root]
    while len(queue) > 0:
        top = queue.pop(0)
        if top is not None:
            ans.append(top.val)
        else:
            ans.append(None)
        if top:
            queue.append(top.left)
            queue.append(top.right)

    # remove all None from end of ans
    i = len(ans) - 1
    while i >= 0 and ans[i] == None:
        i -= 1
    return ans[0: i + 1]
