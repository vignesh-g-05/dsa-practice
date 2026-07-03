from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


nodea3 = ListNode(3)
nodea2 = ListNode(4, nodea3)
nodea1 = ListNode(2, nodea2)

nodeb3 = ListNode(4)
nodeb2 = ListNode(6, nodeb3)
nodeb1 = ListNode(5, nodeb2)


def failed_version(l1: ListNode, l2: ListNode):
    # convert list into numbers
    num_1 = num_2 = 0
    curr_1 = l1
    curr_2 = l2
    while curr_1 or curr_2:
        if curr_1:
            num_1 *= 10
            num_1 += curr_1.val
            curr_1 = curr_1.next
        if curr_2:
            num_2 *= 10
            num_2 += curr_2.val
            curr_2 = curr_2.next

    total = num_1 + num_2
    print(total, num_1, num_2)

    # Convert total into list
    head = ListNode(0)

    if total == 0:
        return head

    curr = head

    while total > 0:
        val = total % 10
        total = total // 10
        new_node = ListNode(val)
        curr.next = new_node
        curr = curr.next

    return head.next


def sum_of_two_numbers(l1: ListNode, l2: ListNode):
    head = ListNode(0)
    carry = 0
    curr = head
    curr_1 = l1
    curr_2 = l2
    while curr_1 or curr_2 or carry:
        num_1 = curr_1.val if curr_1 else 0
        num_2 = curr_2.val if curr_2 else 0
        total = num_1 + num_2 + carry

        if total > 9:
            carry = total // 10
            total = total % 10
        else:
            carry = 0

        curr_1 = curr_1.next if curr_1 else None
        curr_2 = curr_2.next if curr_2 else None
        new_node = ListNode(total)
        curr.next = new_node
        curr = curr.next
    return head.next


head = sum_of_two_numbers(nodea1, nodeb1)

while head:
    print(head.val, end=" -> ")
    head = head.next
print(None)
