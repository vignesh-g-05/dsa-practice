from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


class MyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def get(self, index: int):
        if not self.head:
            return -1
        i = 0
        current = self.head
        while current:
            if i == index:
                return current.data
            current = current.next
            i += 1
        return -1

    def addAtHead(self, data: Any):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, data: Any):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def addAtIndex(self, index: int, data: Any) -> None:
        new_node = Node(data)
        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head = new_node
            else:
                self.head = new_node
            return

        i = 0
        current = self.head
        while current:
            if index == i + 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            i += 1

    def deleteAtIndex(self, index: int):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next

        current = self.head
        i = 0
        while current:
            if i == index - 1:
                if current.next:
                    current.next = current.next.next
            i += 1
            current = current.next
