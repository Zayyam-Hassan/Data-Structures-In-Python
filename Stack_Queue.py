from LinkedList import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        current_node = Node(data)
        current_node.next = self.top
        self.top = current_node

    def pop(self):
        if not self.top:
            raise IndexError("pop from empty stack")
        current_node = self.top
        self.top = self.top.next
        return current_node.data

    def __count_helper(self, current_node):
        if not current_node:
            return 0
        return 1 + self.__count_helper(current_node.next)

    def size(self):
        return self.__count_helper(self.top)

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            raise IndexError("peek from empty stack")


class Queue:
    def __init__(self):
        self.front = None

    def __init(self):
        self.front = None

    def push(self, data):
        if self.front is None:
            self.front = Node(data)
            return
        current_node = self.front
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)

    def pop(self):
        if self.front is None:
            return
        current_node = self.front
        self.front = current_node.next
        return current_node.data

    def get_front(self):
        return self.front.data

    def isempty(self):
        return self.front is None
