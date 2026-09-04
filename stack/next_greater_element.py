def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    stack: list[int] = []
    paired: list[tuple[int, int]] = []

    for num in reversed(nums2):
        next_greater = -1

        while stack:
            top = stack[-1]
            if num > top:
                stack.pop()
                continue
            next_greater = top
            break

        stack.append(num)
        paired.append((num, next_greater))

    for i in range(len(nums1)):
        for pair in paired:
            if pair[0] == nums1[i]:
                nums1[i] = pair[1]
                break

    return nums1
