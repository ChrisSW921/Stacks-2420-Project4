class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
        self.size += 1

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        raise IndexError

    def top(self):
        if not self.is_empty():
            return self.top_item.get_value()
        raise IndexError

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def clear(self):
        while not self.is_empty():
            self.pop()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
