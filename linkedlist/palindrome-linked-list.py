from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


node5 = ListNode(1)
node4 = ListNode(2, node5)
node3 = ListNode(3, node4)
node2 = ListNode(5, node3)
node1 = ListNode(1, node2)


def find_palindrome(head: ListNode | None):
    if head is None:
        return False
    if head.next is None:
        return True

    # Find the middle element
    slow_ptr = fast_ptr = head

    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    # Reverse the linked list
    prev = None
    curr = slow_ptr
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # check for palindrome
    first_ptr = head
    second_ptr = prev
    while second_ptr:
        if first_ptr.val != second_ptr.val:
            return False
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next
    return True
