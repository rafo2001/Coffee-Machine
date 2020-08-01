class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        el = self.stack[len(self.stack) - 1]
        self.stack.remove(len(self.stack) - 1)
        return el

    def peek(self):
        el = self.stack[len(self.stack) - 1]
        return el

    def is_empty(self):
        return len(self.stack) == 0
