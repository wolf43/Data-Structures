"""This module sets up doubly linked lists in python."""


class Node(object):
    """The class is to define a single node of a linked list."""

    def __init__(self, data=None, next=None, previous=None):
        """Constructor for node class."""
        self.data = data
        self.next = next
        self.previous = previous

    def get_data(self):
        """Function to retrive data stored in a node."""
        return self.data

    def get_next(self):
        """Function to retrive the next node for a node."""
        return self.next

    def get_previous(self):
        """Function to retrive the previous node."""
        return self.previous


class DoublyLinkedList(object):
    """The class to setup doubly linked list."""

    def __init__(self, head=None, tail=None):
        """Constructor for DoublyLinkedList class."""
        self.head = head
        self.tail = tail

    def is_list_empty(self):
        """Check if the list is empty."""
        return not bool(self.head)

    def add_item_front(self, node):
        """Function to add element to the list."""
        # Special step to add first item
        if self.is_list_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def add_item_back(self, node):
        """Function to add element to the list."""
        # Special step to add first item
        if self.is_list_empty():
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

    def items_in_list(self):
        """Return the number of items in the list."""
        count = 0
        if self.is_list_empty():
            return count
        else:
            current = self.head
            while current:
                current = current.get_next()
                count += 1
            return count

    def print_list(self):
        """Print the items in the list."""
        current = self.head
        while current:
            print current.data
            current = current.get_next()

    def print_list_backwards(self):
        """Print the items in the list."""
        current = self.tail
        while current:
            print current.data
            current = current.get_previous()

    def is_value_in_list(self, value):
        """Check if value is in list."""
        present_status = False
        if self.is_list_empty():
            return present_status
        else:
            current = self.head
            while current:
                if current.data == value:
                    present_status = True
                    return present_status
                current = current.get_next()
        return present_status

    def remove_item(self, value):
        """Remove value from list if it exists."""
        if not self.is_value_in_list(value):
            raise ValueError("Can't remove item as it is not present in the list")
        else:
            current = self.head
            while current:
                if current.data == value:
                    if current == self.head:
                        self.head = current.get_next()
                    if current.get_next():
                        current.get_next().previous = current.get_previous()
                        if current.get_previous():
                            current.get_previous().next = current.get_next()
                    else:
                        self.tail = current.get_previous()
                        current.get_previous().next = current.get_next()
                current = current.get_next()

    def clear_list(self):
        """Remove entire list."""
        self.head = None
        self.tail = None
