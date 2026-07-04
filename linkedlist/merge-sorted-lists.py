from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


nodea3 = ListNode(4)
nodea2 = ListNode(2, nodea3)
nodea1 = ListNode(1, nodea2)

nodeb4 = ListNode(9)
nodeb3 = ListNode(4, nodeb4)
nodeb2 = ListNode(3, nodeb3)
nodeb1 = ListNode(1, nodeb2)


def merge_sorted_lists(list1: ListNode | None, list2: ListNode | None):
    if not list1:
        return list2
    if not list2:
        return list1

    ptr_1 = list1
    ptr_2 = list2
    head = ListNode()
    tail = head

    while ptr_1 and ptr_2:
        new_node = ListNode()
        if ptr_1.val <= ptr_2.val:
            new_node.val = ptr_1.val
            ptr_1 = ptr_1.next
        else:
            new_node.val = ptr_2.val
            ptr_2 = ptr_2.next
        tail.next = new_node
        tail = new_node

    while ptr_1:
        new_node = ListNode(ptr_1.val)
        tail.next = new_node
        tail = new_node
        ptr_1 = ptr_1.next

    while ptr_2:
        new_node = ListNode(ptr_2.val)
        tail.next = new_node
        tail = new_node
        ptr_2 = ptr_2.next

    return head.next


head = merge_sorted_lists(nodea1, nodeb1)

while head:
    print(head.val, end=" -> ")
    head = head.next
print(None)
