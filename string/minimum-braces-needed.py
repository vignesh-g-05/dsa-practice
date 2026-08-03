def solution(s: str) -> int:
    if not s:
        return 0
    open_brackets = 0
    extra_brackets = 0
    for c in s:
        if c == "(":
            open_brackets += 1
        elif open_brackets == 0:
            extra_brackets += 1
        else:
            open_brackets -= 1

    return extra_brackets + open_brackets
