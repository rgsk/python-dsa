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
