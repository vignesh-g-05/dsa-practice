from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


nodea3 = ListNode(4)
nodea2 = ListNode(2, nodea3)
nodea1 = ListNode(1, nodea2)

nodeb4 = ListNode(4)
nodeb3 = ListNode(3, nodeb4)
nodeb2 = ListNode(2, nodeb3)
nodeb1 = ListNode(1, nodeb2)


def rotate_list(head: ListNode | None, k: int) -> ListNode | None:
    if not head or not head.next:
        return head

    # Find Length
    length = 0
    curr = head
    while curr:
        curr = curr.next
        length += 1

    # move fast pointer k % length times
    fast = head
    slow = head
    for _ in range(k % length):
        fast = fast.next

    # move fast to end and slow to fast
    while fast.next:
        fast = fast.next
        slow = slow.next

    fast.next = head
    head = slow.next
    slow.next = None
    return head


head = rotate_list(nodeb1, 3)
head = head

while head:
    print(head.val, end=" -> ")
    head = head.next
print(None)
