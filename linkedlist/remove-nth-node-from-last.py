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


def remove_nth_element_two_pass(head: ListNode | None, n: int) -> ListNode | None:
    if not head:
        return None

    size = 0
    curr = head
    while curr:
        size += 1
        curr = curr.next

    target_idx = size - n
    if target_idx == 0:
        return head.next

    curr = head
    for _ in range(target_idx - 1):
        curr = curr.next  # type: ignore[reportOptionalMemberAccess]
    curr.next = curr.next.next  # type: ignore[reportOptionalMemberAccess]
    return head


def remove_nth_element_one_pass(head: ListNode | None, n: int) -> ListNode | None:
    if head is None:
        return None

    first_ptr = head
    second_ptr = ListNode(0, head)

    for _ in range(n - 1):
        first_ptr = first_ptr.next  # type: ignore[reportOptionalMemberAccess]

    while first_ptr and first_ptr.next:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next  # type: ignore[reportOptionalMemberAccess]

    if second_ptr.next == head:  # type: ignore[reportOptionalMemberAccess]
        return head.next

    second_ptr.next = second_ptr.next.next  # type: ignore[reportOptionalMemberAccess]
    return head


head = remove_nth_element_one_pass(node5, 1)

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print(None)
