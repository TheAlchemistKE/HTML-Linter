class Stack:
    """
        This class contains the implementation of the Stack Data Structure.
    """
    def __init__(self):
        """
            This method contains the instantiation of the Stack as a list.
        """
        self.stack_items = []

    def push(self, item):
        """
            In this method we add items to the top of the stack. This method returns nothing, it just adds the given element to the Stack.
        """
        self.stack_items.append(item)

    def pop(self):
        """
            In this method we remove the top most item off the stack if the Stack is not empty. This method returns the top most item that has been removed or False if the Stack is empty.
        """
        if self.stack_items:
            return self.stack_items.pop()
        return False

    def peek(self):
        """
            This method enables us to be able to see what element is at the top of the stack therego this is the element to be popped if need be. The stack must be non-empty for this to work, if it isn't the method returns False.
        """
        if self.stack_items:
            return self.stack_items[-1]
        return False