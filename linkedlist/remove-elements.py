from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
    new_head = head

    while new_head and new_head.val == val:
        new_head = new_head.next
    if new_head is None:
        return
    prev = new_head
    curr = new_head.next

    while curr:
        if curr.val == val:
            prev.next = curr.next
            curr = curr.next
            continue
        prev = curr
