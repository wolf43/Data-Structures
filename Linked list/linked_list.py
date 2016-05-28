"""This module sets up sigly linked lists in python."""


class Node(object):
    """The class is to define a single node of a linked list."""

    def __init__(self, data=None, next=None):
        """Constructor for node class."""
        self.data = data
        self.next = next

    def get_data(self):
        """Function to retrive data stored in a node."""
        return self.data

    def get_next(self):
        """Function to retrive the next node for a node."""
        return self.next

    def next_exists(self):
        """Function to check if next node exists for a node."""
        return bool(self.next)


class LinkedList(object):
    """Class to setup a linked list."""

    def __init__(self, head=None):
        """Constructor for linked list."""
        self.head = head

    def add_element(self, data):
        """Function to add node at the head of a linked list."""
        new_node = Node(data, self.head)
        self.head = new_node

    def add_element_at_pos_n(self, data, position):
        """Add elements with data at position n."""
        if position == 1:
            self.add_element(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in xrange(2, position):
                if not current.next:
                    print "Can't insert at position: " + str(position)
                    print "Linked list shorter than that"
                    raise ValueError
                current = current.get_next()
            new_node.next = current.next
            current.next = new_node

    def get_count(self):
        """Get the number of items in linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def print_list(self):
        """Print all elements of the list."""
        current = self.head
        while current:
            print current.data
            current = current.get_next()

    def is_value_in_list(self, data):
        """Search for data in linked list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.get_next()
        return False

    def remove_value(self, data):
        """Remove data from list if it exists."""
        if not self.is_value_in_list(data):
            print "Value: " + str(data) + " not in list"
            return False
        else:
            current = self.head
            previous = self.head
            while current:
                if current.data == data:
                    if current == self.head:
                        self.head = current.get_next()
                        return True
                    previous.next = current.next
                    return True
                previous = current
                current = current.get_next()

    def clear_list(self):
        """Remove entire list."""
        self.head = None

N1 = Node(9)
L1 = LinkedList(N1)
L1.add_element(8)
L1.add_element(6)
L1.add_element(5)
L1.add_element(3)
L1.print_list()
print "Count before insert: " + str(L1.get_count())


L1.add_element_at_pos_n(7, 4)
L1.print_list()
print "Count after insert at pos 4: " + str(L1.get_count())

L1.add_element_at_pos_n(4, 2)
L1.print_list()
print "Count after insert at pos 2: " + str(L1.get_count())

L1.add_element_at_pos_n(2, 1)
L1.print_list()
print "Count after insert at pos 1: " + str(L1.get_count())


print L1.is_value_in_list(34)
print L1.is_value_in_list(3)

print "Removing 3"
L1.remove_value(3)
L1.print_list()

print "Removing 2"
L1.remove_value(2)
L1.print_list()

print "Removing 6"
L1.remove_value(6)
L1.print_list()

print "Removing 8"
L1.remove_value(8)
L1.print_list()

print "Removing 9"
L1.remove_value(9)
L1.print_list()

print "Removing 34"
L1.remove_value(34)
L1.print_list()

print "Deleting list"
L1.clear_list()
L1.print_list()
