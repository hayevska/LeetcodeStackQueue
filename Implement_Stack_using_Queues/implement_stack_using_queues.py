class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return not self.items

class MyStack(object):

    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_1.enqueue(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue_1.items) > 1:
            self.queue_2.enqueue(self.queue_1.dequeue())
        our_el = self.queue_1.dequeue()
        for _ in range(len(self.queue_2.items)):
            self.queue_1.enqueue(self.queue_2.dequeue())
        return our_el

    def top(self):
        """
        :rtype: int
        """
        return self.queue_1.items[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue_1.items
