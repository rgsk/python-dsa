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
    def key(self):
        return self.val

    @data.setter
    def key(self, new_val: int):
        self.val = new_val

    @property
    def value(self):
        return self.val

    @data.setter
    def value(self, new_val: int):
        self.val = new_val

    def __repr__(self) -> str:
        return str(getList(self))

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinaryTreeNode(TreeNode):
    pass


def getHeight(root: Optional[TreeNode]):
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
    if values[0] is None:
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
    store = [root]
    ans: List[List[int]] = []
    while store:
        temp_store: List[Optional[TreeNode]] = []
        row = []
        anyNodeExists = any(store)
        for node in store:
            if node:
                row.append(node.val)
                temp_store.append(node.left)
                temp_store.append(node.right)
            else:
                row.append(INT_MIN)
                if anyNodeExists:
                    temp_store.append(None)
                    temp_store.append(None)
        ans.append(row)
        store = temp_store
    return ans


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    q: deque[TreeNode] = deque()
    if (root):
        q.append(root)
    ans: List[List[int]] = []
    while q:
        row = []
        for _ in range(len(q)):
            node = q.popleft()
            row.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(row)
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


def levelOrderNodes(root: Optional[TreeNode]) -> List[List[TreeNode]]:
    ans: List[List[TreeNode]] = []
    queue = deque([root, None])
    row: List[TreeNode] = []
    while queue:
        last = queue.popleft()
        if last:
            row.append(last)
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


def isLeaf(node: Optional[TreeNode]):
    return node and node.left is None and node.right is None


def getLeafs(root: Optional[TreeNode]):
    ans: List[TreeNode] = []

    def helper(node: Optional[TreeNode]):
        if node:
            if isLeaf(node):
                ans.append(node)
            else:
                helper(node.left)
                helper(node.right)
    helper(root)
    return ans


def findNode(root: Optional[TreeNode], val: int):
    def helper(node: Optional[TreeNode]):
        if node:
            if node.val == val:
                return node
            return helper(node.left) or helper(node.right)
    return helper(root)


def createTreeFromInorder(inorderTraversal, left, right):
    if left <= right:
        mid = (left + right) // 2
        node = TreeNode(inorderTraversal[mid])
        node.left = createTreeFromInorder(inorderTraversal, left, mid - 1)
        node.right = createTreeFromInorder(inorderTraversal, mid + 1, right)
        return node


def getInorderTraversal(root: TreeNode):
    values = []

    def inorder(root: Optional[TreeNode]):
        if root:
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
    inorder(root)
    return values


def getPreorderTraversal(root: TreeNode):
    values = []

    def preorder(root: Optional[TreeNode]):
        if root:
            values.append(root.val)
            preorder(root.left)
            preorder(root.right)
    preorder(root)
    return values


def getPostorderTraversal(root: TreeNode):
    values = []

    def postorder(root: Optional[TreeNode]):
        if root:
            postorder(root.left)
            postorder(root.right)
            values.append(root.val)
    postorder(root)
    return values


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        x = self.stack.pop()
        temp = x.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return x.val


# that's a nice trick to use yield for getting the next value in inorder
def tree_iter(root):
    if not root:
        return
    for val in tree_iter(root.left):
        yield val
    yield root.val
    for val in tree_iter(root.right):
        yield val
