"""
1796. Second Largest Digit in a String

Approach:
Time: O(log n)
Space: O(1)
"""


def approach(s: str) -> int:
    max = -1
    sec_max = -1
    for i in range(len(s)):
        str = s[i]
        if not str.isdigit():
            continue
        num = int(str)
        if num > max:
            sec_max = max
            max = num
        elif num > sec_max and num != max:
            sec_max = num

    return sec_max
