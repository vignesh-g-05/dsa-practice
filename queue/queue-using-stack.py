class MyQueue:

    def __init__(self):
        self.stack1: list[int] = []
        self.stack2: list[int] = []
        self.size: int = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return 0

        if len(self.stack2) > 0:
            self.size -= 1
            return self.stack2.pop()

        for _ in range(self.size):
            self.stack2.append(self.stack1.pop())

        self.size -= 1
        return self.stack2.pop()

    def peek(self) -> int:

        if self.empty():
            return 0

        if len(self.stack2) > 0:
            return self.stack2[-1]

        for _ in range(self.size):
            self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        return self.size == 0
