def solution(grid: list[list[int]]) -> int:
    queue: list[dict[str, int]] = []
    m = len(grid)
    n = len(grid[0])

    for row in range(m):
        for col in range(n):
            if grid[row][col] == 2:
                queue.append({"x": row, "y": col, "min": 0})
    total_minutes = 0

    while queue:
        cell = queue.pop(0)

        x = cell["x"]
        y = cell["y"]
        minute = cell["min"] + 1
        total_minutes = max(minute - 1, total_minutes)

        if x < m - 1 and grid[x + 1][y] == 1:
            grid[x + 1][y] = 2
            queue.append({"x": x + 1, "y": y, "min": minute})

        if x > 0 and grid[x - 1][y] == 1:
            grid[x - 1][y] = 2
            queue.append({"x": x - 1, "y": y, "min": minute})

        if y < n - 1 and grid[x][y + 1] == 1:
            grid[x][y + 1] = 2
            queue.append({"x": x, "y": y + 1, "min": minute})

        if y > 0 and grid[x][y - 1] == 1:
            grid[x][y - 1] = 2
            queue.append({"x": x, "y": y - 1, "min": minute})

    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                return -1

    return total_minutes
