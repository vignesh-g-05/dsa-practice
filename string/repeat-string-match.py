def solution(s: list[str]) -> int:
    [a, b] = s
    text = a
    pattern = b
    count = 0
    while len(text) < len(pattern):
        text += a
        count += 1

    if pattern in text:
        return count

    text += a
    count += 1

    if pattern in text:
        return count

    return -1
