class MinStack:

    def __init__(self):
        self.stack: list[dict[str, int]] = []

    def push(self, value: int) -> None:
        new_element: dict[str, int] = {"value": value, "min": value}
        if len(self.stack) == 0:
            self.stack.append(new_element)
            return

        last_element = self.stack[-1]
        new_element["min"] = min(value, last_element["min"])
        self.stack.append(new_element)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0

        return self.stack[-1]["value"]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0

        return self.stack[-1]["min"]
