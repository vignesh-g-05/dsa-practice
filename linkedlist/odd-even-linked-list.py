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


def odd_even_linked_list(head: ListNode | None) -> ListNode | None:
    if not head:
        return None

    odd_ptr = head
    even_ptr = head.next

    if not even_ptr:
        return head
    first_even = even_ptr
    curr = head.next.next
    is_odd = True

    while curr:
        print(curr.val)
        if is_odd:
            odd_ptr.next = curr
            odd_ptr = curr
        else:
            even_ptr.next = curr
            even_ptr = curr
        is_odd = not is_odd
        curr = curr.next

    odd_ptr.next = first_even
    even_ptr.next = None
    return head


head = odd_even_linked_list(node1)

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print(None)
