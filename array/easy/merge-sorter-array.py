from typing import Any


def solution(input: dict[str, Any]) -> list[int]:
    nums1: list[int] = input.get("nums1") or []
    nums2: list[int] = input.get("nums2") or []
    m: int = input.get("m") or 0
    n: int = input.get("n") or 0

    ptr1 = m - 1
    ptr2 = n - 1
    ptr3 = m + n - 1

    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] > nums2[ptr2]:
            nums1[ptr3] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[ptr3] = nums2[ptr2]
            ptr2 -= 1
        ptr3 -= 1

    while ptr2 >= 0:
        nums1[ptr3] = nums2[ptr2]
        ptr2 -= 1
        ptr3 -= 1

    return nums1
