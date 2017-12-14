class Queue:
    class Node:
        def __init__(self, item, _next):
            self.item = item
            self.next = _next

    class Iterator:
        def __init__(self, current):
            self.current = current

        def __next__(self):
            if self.current is None:
                raise StopIteration
            item = self.current.item
            self.current = self.current.next
            return item

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def enqueue(self, item):
        old_last = self.last
        self.last = self.Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.n += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.first.item
            self.first = self.first.next
            self.n -= 1
            if self.is_empty():
                self.last = None
            return item

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.n

    def peek(self):
        return self.first.item

    def __iter__(self):
        return self.Iterator(self.first)
