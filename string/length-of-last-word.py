def solution(s: str) -> int:
    length = 0
    full_length = len(s) - 1
    for i in range(full_length, -1, -1):
        char = s[i]
        if char == " " and length == 0:
            continue
        elif char != " ":
            length += 1
        else:
            return length
    return full_length + 1
