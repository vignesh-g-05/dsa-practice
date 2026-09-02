def remove_outer_parentheses(string: str):
    output: list[str] = []
    depth = 0

    for char in string:
        if char == "(":
            if depth > 0:
                output.append(char)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                output.append(char)

    return "".join(output)
