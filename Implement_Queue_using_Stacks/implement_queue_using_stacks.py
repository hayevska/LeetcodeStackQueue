class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items

class MyQueue(object):

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        for _ in range(len(self.stack_1.items)):
            self.stack_2.push(self.stack_1.pop())
        our_el = self.stack_2.pop()
        for _ in range(len(self.stack_2.items)):
            self.stack_1.push(self.stack_2.pop())
        return our_el

    def peek(self):
        """
        :rtype: int
        """
        return self.stack_1.items[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_1.items
