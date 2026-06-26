class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next: ListNode | None = next


c3 = ListNode(5)
c2 = ListNode(4, c3)
c1 = ListNode(8, c2)

b3 = ListNode(1, c1)
b2 = ListNode(6, b3)
b1 = ListNode(5, b2)

a2 = ListNode(1, c1)
a1 = ListNode(4, a2)


def find_intersection_using_set(headA: ListNode, headB: ListNode) -> ListNode | None:
    node_set = set[ListNode]()
    ptr_a = headA
    ptr_b = headB

    while ptr_a or ptr_b:
        if ptr_a == ptr_b:
            return ptr_a
        if ptr_a in node_set:
            return ptr_a
        if ptr_b in node_set:
            return ptr_b

        if ptr_a:
            node_set.add(ptr_a)
            ptr_a = ptr_a.next
        if ptr_b:
            node_set.add(ptr_b)
            ptr_b = ptr_b.next
    return None


def find_intersection_using_two_pointer(
    headA: ListNode, headB: ListNode
) -> ListNode | None:
    ptr_a = headA
    ptr_b = headB
    len_a = 0
    len_b = 0

    while ptr_a or ptr_b:
        if ptr_a:
            len_a += 1
            ptr_a = ptr_a.next
        if ptr_b:
            len_b += 1
            ptr_b = ptr_b.next

    diff = len_a - len_b
    longer = headA
    shorter = headB

    if len_b > len_a:
        diff = len_b - len_a
        longer = headB
        shorter = headA

    for _ in range(diff):
        longer = longer.next

    while longer:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
    return None


res = find_intersection_using_two_pointer(a1, b1)

print(res.val)
