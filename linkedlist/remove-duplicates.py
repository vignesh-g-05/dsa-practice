from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


node5 = ListNode(3)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)


def remove_duplicate_elements(head: ListNode | None, n: int) -> ListNode | None:
    if not head:
        return None

    ptr_1 = head
    ptr_2 = head.next

    while ptr_2:
        if ptr_1.val != ptr_2.val:
            ptr_1.next = ptr_2
            ptr_1 = ptr_2
        ptr_2 = ptr_2.next

    ptr_1.next = None

    return head
