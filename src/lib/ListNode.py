from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @property
    def data(self):
        return self.val

    @data.setter
    def data(self, new_val: int):
        self.val = new_val


def asList(l: Optional[ListNode]) -> List[int]:
    if l == None:
        return []

    ans: List[int] = []
    t = l
    while t is not None:
        ans.append(t.val)
        t = t.next
    return ans


def makeList(elems: List[int]) -> Optional[ListNode]:
    if not elems:
        return None
    l = ListNode(-1)
    t = l
    for v in elems:
        t.next = ListNode(v)
        t = t.next
    return l.next


def getLength(head: Optional[ListNode]) -> int:
    temp = head
    count = 0
    while temp:
        temp = temp.next
        count += 1
    return count


def at(head: Optional[ListNode], idx: int):
    length = getLength(head)
    if idx < 0:
        idx = length + idx
    if idx < 0 or idx >= length:
        raise Exception("index out of range")
    temp = head
    while idx > 0:
        if temp is not None:
            temp = temp.next
        else:
            raise Exception("index out of range")
        idx -= 1
    return temp


def pop(head: Optional[ListNode], idx: int):
    if not head:
        return None
    if idx == 0 or idx == -getLength(head):
        return head.next
    length = getLength(head)
    if idx < 0:
        idx = length + idx
    if idx < 0 or idx >= length:
        raise Exception("index out of range")
    node = at(head, idx-1)
    node.next = node.next.next
    return head


def equal(first: Optional[ListNode], second: Optional[ListNode]):
    ft = first
    st = second

    while ft is not None and st is not None:
        if ft.val != st.val:
            return False
        ft = ft.next
        st = st.next

    if ft is None and st is None:
        return True
    return False


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    next = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


INT_MAX = (2 ** 31)-1


def mergeSort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    slow = head
    fast = head.next.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    left = mergeSort(head)
    right = mergeSort(mid)
    ans = ListNode(-1)
    temp = ans
    while left != None or right != None:
        n1 = left.val if left is not None else INT_MAX
        n2 = right.val if right is not None else INT_MAX

        if n1 < n2:
            temp.next = left
            assert isinstance(left, ListNode)  # alternative check
            left = left.next
        else:
            temp.next = right
            if right is not None:
                right = right.next
        if temp.next is not None:
            temp = temp.next
    return ans.next


def indexOf(head: Optional[ListNode], node: Optional[ListNode]):
    if not node:
        return -1
    idx = 0
    temp = head
    while temp:
        if node.val == temp.val:
            return idx
        idx += 1
        temp = temp.next
    return -1


def getNodes(head: Optional[ListNode]):
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes


def connectNodes(nodes: List[ListNode]):
    dummy = ListNode()
    temp = dummy
    for node in nodes:
        temp.next = node
        temp = temp.next
    temp.next = None
    return dummy.next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        assert slow is not None
        slow = slow.next

    return slow


class Node(ListNode):
    pass


def copy(head: Optional[ListNode]):
    dummy = ListNode(-1)
    dummy_temp = dummy
    temp = head
    while temp:
        dummy_temp.next = ListNode(temp.val)
        dummy_temp = dummy_temp.next
        temp = temp.next
    return dummy.next
