from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    l = ListNode()
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
