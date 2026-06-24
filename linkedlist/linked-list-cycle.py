from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
node5.next = node2


def find_list_cycle(head: ListNode | None):
    if head is None or head.next is None:
        return False
    list_set = set[ListNode]()
    curr = head

    while curr.next:
        if curr in list_set:
            return True
        list_set.add(curr)
        curr = curr.next

    return False


def floyds_algorithim(head: ListNode | None):
    """
    if two people runs at a different speed in a circular path
    they will definitely meet each other at some point
    """
    if head is None or head.next is None:
        return False
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next  # type: ignore[PyrightreportOptionalMemberAccess]
        if slow_ptr == fast_ptr:
            return True

    return False
