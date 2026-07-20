def solution(num: str) -> str:
    target_idx = -1
    for i in range(len(num) - 1, -1, -1):
        n = int(num[i])
        if n % 2 != 0:
            target_idx = i
            break

    if target_idx == -1:
        return ""

    return num[: target_idx + 1]
