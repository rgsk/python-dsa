# https://leetcode.com/problems/same-tree/
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @property
    def data(self):
        return self.val

    @data.setter
    def data(self, new_val: int):
        self.val = new_val

    @property
    def value(self):
        return self.val

    @data.setter
    def value(self, new_val: int):
        self.val = new_val

    def __repr__(self) -> str:
        return str(getList(self))


def getHeight(root: TreeNode):
    if root is None:
        return 0
    else:
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        return max(left_height, right_height) + 1


def printHorizontal(root):
    def print_tree(root, level):
        if root is not None:
            print_tree(root.right, level + 1)
            print("    " * (level - 1) + "|---" + str(root.value))
            print_tree(root.left, level + 1)

    height = getHeight(root)
    print_tree(root, height)


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


INT_MAX = (2 ** 31)-1
INT_MIN = -(2 ** 31)


def levelOrderWithNoneNodes(root: Optional[TreeNode]) -> List[List[int]]:
    stack = [(root, 0)]
    ans: List[List[int]] = []
    while stack:
        last, idx = stack.pop()
        if idx == len(ans):
            ans.append([])
        if last:
            ans[idx].append(last.val)
            stack.append((last.right, idx + 1))
            stack.append((last.left, idx + 1))
        else:
            ans[idx].append(INT_MIN)
    return ans


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    stack = [(root, 0)]
    ans: List[List[int]] = []
    while stack:
        last, idx = stack.pop()
        if last:
            if idx == len(ans):
                ans.append([])
            ans[idx].append(last.val)
            stack.append((last.right, idx + 1))
            stack.append((last.left, idx + 1))
    return ans


def levelOrder2(root: Optional[TreeNode]) -> List[List[int]]:
    current_level_nodes = [root]
    ans: List[List[int]] = []
    while current_level_nodes:
        next_level_nodes = []
        row: List[int] = []

        for node in current_level_nodes:
            if node:
                row.append(node.val)
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)
        if row:
            ans.append(row)
        current_level_nodes = next_level_nodes
    return ans


def levelOrder3(root: Optional[TreeNode]) -> List[List[int]]:
    ans: List[List[int]] = []
    queue = deque([root, None])
    row: List[int] = []
    while queue:
        last = queue.popleft()
        if last:
            row.append(last.val)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        else:
            ans.append(row)
            row = []
            if queue:
                queue.append(None)
    return ans
