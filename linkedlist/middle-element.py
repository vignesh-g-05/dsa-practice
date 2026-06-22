from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


def middle_node_using_array(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    nodes: list[ListNode] = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    mid = len(nodes) // 2
    return nodes[mid]


def middle_node_using_two_ptr(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

middle_element = middle_node_using_two_ptr(node1)

if middle_element is None:
    print("empty list")
else:
    print(middle_element.val, middle_element.next)
