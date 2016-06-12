"""This module implements stacks using python lists."""


class Stack(object):
    """Implementation of a stack using a python list."""

    def __init__(self, limit=10):
        """Constructor for Stack class."""
        self.stack = []
        self.limit = limit

    def is_stack_empty(self):
        """Check if the stack is empty."""
        return self.stack == []

    def is_stack_full(self):
        """Check is the stack is full."""
        return len(self.stack) == self.limit

    def push(self, item):
        """Insert item to top of stack."""
        if self.is_stack_full():
            raise ValueError("Can't add item to stack, stack is full")
        else:
            self.stack.append(item)

    def pop(self):
        """Remove an item from top of stack."""
        if self.is_stack_empty():
            raise ValueError("Can't retrive item from stack, stack is empty")
        else:
            self.stack.pop()

    def size(self):
        """Return the size of stack."""
        return len(self.stack)

    def print_stack(self):
        """Print the item stack."""
        print self.stack

    def peek(self):
        """Look at top of stack without modifying it."""
        return self.stack[self.size() - 1]

    def clear_stack(self):
        """Clear the stack."""
        self.stack = []
