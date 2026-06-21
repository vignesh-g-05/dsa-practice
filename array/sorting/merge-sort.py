def sort(arr1: list[int], arr2: list[int]):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    result: list[int] = []
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len1:
        result.append(arr1[i])
        i += 1

    while j < len2:
        result.append(arr2[i])
        j += 1

    return result


def merge_sort(arr: list[int], start: int, end: int) -> list[int]:
    if start == end:
        return [arr[start]]
    mid = (start + end) // 2
    left_arr = merge_sort(arr, start, mid)
    right_arr = merge_sort(arr, mid + 1, end)
    return sort(left_arr, right_arr)


def solution(input: list[int]) -> list[int]:
    return merge_sort(input, 0, len(input) - 1)
