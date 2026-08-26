class TwoQueues:

    def __init__(self):
        self.q1: list[int] = []
        self.q2: list[int] = []
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return 0

        for _ in range(self.size - 1):
            self.q2.append(self.q1.pop(0))

        removed = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        self.size -= 1
        return removed

    def top(self) -> int:
        if self.empty():
            return 0

        for _ in range(self.size - 1):
            self.q2.append(self.q1.pop(0))

        top_element = self.q1.pop(0)
        self.q2.append(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return len(self.q1) == 0


class OneQueue:

    def __init__(self):
        self.q: list[int] = []
        self.size = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return 0

        for _ in range(self.size - 1):
            self.q.append(self.q.pop(0))

        self.size -= 1
        return self.q.pop(0)

    def top(self) -> int:
        if self.empty():
            return 0

        for _ in range(self.size - 1):
            self.q.append(self.q.pop(0))

        top_element = self.q.pop(0)
        self.q.append(top_element)
        return top_element

    def empty(self) -> bool:
        return len(self.q) == 0


stack = OneQueue()

stack.push(1)
stack.push(2)
stack.pop()
stack.push(3)
print(stack.top())

print(stack.q)
