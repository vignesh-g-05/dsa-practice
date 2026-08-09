def solution(s: str) -> str:
    num_stack: list[int] = []
    str_stack: list[str] = []
    k = 0
    for c in s:
        if c.isdigit():
            k *= 10
            k += int(c)
            continue

        if k > 0:
            num_stack.append(k)
            k = 0

        if c != "]":
            str_stack.append(c)
            continue

        decoded_part = ""

        while True:
            char = str_stack.pop()
            if char != "[":
                decoded_part = char + decoded_part
                continue

            str_stack.append(decoded_part * num_stack.pop())
            break

    return "".join(str_stack)
