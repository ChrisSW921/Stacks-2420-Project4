"""Stack module"""

class Node:
    """Node Class"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        """Sets next node"""
        self.next_node = next_node

    def get_next_node(self):
        """Gets next node"""
        return self.next_node

    def get_value(self):
        """Gets value"""
        return self.value


class Stack:
    """Stack class"""
    def __init__(self, limit=1000):
        self.top_item = None
        self.ssize = 0

    def push(self, value):
        """Push item"""
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
        self.ssize += 1

    def pop(self):
        """Pop item"""
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.ssize -= 1
            return item_to_remove.get_value()
        raise IndexError

    def top(self):
        """Get top item"""
        if not self.is_empty():
            return self.top_item.get_value()
        raise IndexError

    def size(self):
        """Get size"""
        return self.ssize

    def is_empty(self):
        """Tel if it is empty"""
        return self.ssize == 0

    def clear(self):
        """Clear stack"""
        while not self.is_empty():
            self.pop()
