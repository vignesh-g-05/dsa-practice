from collections.abc import Callable


def eval_rpn(tokens: list[str]) -> int:
    operation_map: dict[str, Callable[[int, int], int]] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),
    }
    stack: list[int] = []

    for token in tokens:
        if token not in operation_map:
            stack.append(int(token))
            continue

        operation = operation_map[token]
        right = stack.pop()
        left = stack.pop()
        result = operation(left, right)
        stack.append(result)

    return stack.pop()
