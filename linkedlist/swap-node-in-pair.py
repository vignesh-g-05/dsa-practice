from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


nodea3 = ListNode(4)
nodea2 = ListNode(2, nodea3)
nodea1 = ListNode(1, nodea2)

nodeb4 = ListNode(4, nodea3)
nodeb3 = ListNode(3, nodeb4)
nodeb2 = ListNode(2, nodeb3)
nodeb1 = ListNode(1, nodeb2)


def rotate_list(head: ListNode | None, k: int) -> ListNode | None:
    if not head or not head.next:
        return head

    prev = ListNode()
    prev.next = head
    curr = head
    nxt = head.next
    head = nxt
    while curr and nxt:
        prev.next = nxt
        curr.next = nxt.next if nxt else None
        if nxt:
            nxt.next = curr
        prev = curr
        curr = prev.next
        nxt = curr.next if curr else None
    return head


head = rotate_list(nodeb1, 3)

while head:
    print(head.val, end=" -> ")
    head = head.next
print(None)
