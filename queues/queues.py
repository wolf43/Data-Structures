"""This module implements queues using python lists."""


class Queue(object):
    """Implementation of a queue using a python list."""

    def __init__(self, limit=10):
        """Constructor for Queue class."""
        self.queue = []
        self.limit = limit

    def is_queue_empty(self):
        """Check if the queue is empty."""
        return self.queue == []

    def is_queue_full(self):
        """Check is the queue is full."""
        return len(self.queue) == self.limit

    def put(self, item):
        """Insert item at end of queue."""
        if self.is_queue_full():
            raise ValueError("Can't add item, queue is full")
        else:
            self.queue.insert(0, item)

    def get(self):
        """Remove an item from front of queue."""
        if self.is_queue_empty():
            raise ValueError("Can't retrive item, queue is empty")
        else:
            self.queue.pop()

    def size(self):
        """Return the size of queue."""
        return len(self.queue)

    def print_queue(self):
        """Print the entire queue."""
        print self.queue

    def peek(self):
        """Look at item at front of queue without modifying it."""
        return self.queue[self.size() - 1]

    def clear_queue(self):
        """Clear the queue."""
        self.queue = []
