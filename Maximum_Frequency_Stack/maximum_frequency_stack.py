from collections import deque
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.curr = defaultdict(deque)
        self.max_count = 0

    def push(self, val):
        self.count[val] += 1
        our_count = self.count[val]
        self.max_count = max(self.max_count, our_count)
        self.curr[our_count].append(val)

    def pop(self):
        our_val = self.curr[self.max_count].pop()
        self.count[our_val] -= 1
        if not self.curr[self.max_count]:
            self.max_count -= 1
        return our_val
