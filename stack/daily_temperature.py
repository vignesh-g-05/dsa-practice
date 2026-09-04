def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack: list[tuple[int, int]] = []

    for i, t in enumerate(temperatures):
        while stack and stack[-1][1] < t:
            stackI, _ = stack.pop()
            temperatures[stackI] = i - stackI
        stack.append((i, t))

    while stack:
        stackI, _ = stack.pop()
        temperatures[stackI] = 0
    return temperatures
