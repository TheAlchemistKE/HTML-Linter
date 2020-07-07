class Stack:
    def __init__(self):
        self.stack_items = []

    def push(self, item):
        self.stack_items.append(item)

    def pop(self):
        if self.stack_items:
            return self.stack_items.pop()
        return False

    def peek(self):
        pass