# FIFO - First in, first out

from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.appendleft(value)

    def deleteOne(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return len(self.container) == 0

queue = Queue()

# push()
queue.push(1)
queue.push(2.5)
queue.push(3)

# deleteOne()
print(queue.deleteOne())

# peek()
print(queue.peek())

# size()
print(queue.size())

# isEmpty()
print(queue.isEmpty())