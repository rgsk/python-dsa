class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0

    def front(self):
        return self.left.data

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.left = self.right = new_node
        else:
            self.right.next = new_node
            self.right = new_node
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.left.data
            self.left = self.left.next
            self.size -= 1
            return item
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def queue_size(self):
        return self.size
