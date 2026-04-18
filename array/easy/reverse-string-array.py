"""
344. Reverse String

Approach 1: Two Pointers (In-place swap from both ends)
Time: O(n)
Space: O(1)

Approach 2: Index-based symmetric swap
Time: O(n)
Space: O(1)
"""


def approach1(s: list[str]) -> list[str]:
    start = 0
    end = len(s) - 1

    while start < end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1

    return s


def approach2(s: list[str]) -> list[str]:
    for i in range(len(s) // 2):
        x = len(s) - i - 1
        temp = s[i]
        s[i] = s[x]
        s[x] = temp

    return s
