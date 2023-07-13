# LIFO - Last in, first out

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def deleteOne(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return len(self.container) == 0
    
stack = Stack()

# push()
stack.push(1)
stack.push(2.5)
stack.push(3)

# deleteOne()
stack.deleteOne()

# peek()
print(stack.peek())

# size()
print(stack.size())

# isEmpty()
print(stack.isEmpty())