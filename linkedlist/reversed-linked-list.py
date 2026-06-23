from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)


def print_list(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print()


def reverse_list(head: ListNode | None) -> ListNode | None:
    if head is None:
        return

    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


print_list(node1)
reverse_list(node1)
print_list(node5)
