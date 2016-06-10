# Doubly linked lists
### Definition
A doubly linked list is a data structure in which the elements present in the data structure have links to the next and previous items. The advantage it has over singly linked list is that it can be traversed in both direction. The main disadvantage is more storage requirements as each node stores a reference to another node.

### The attributes of each node are
* Data: Value of the item
* Next: Reference to next item in the list. None for last item in the list
* Previous: Reference to previous item in the list. None for first item in the list

### Operations on the list
* Add item: At the beginning or the end
* Print list: Print all elements on the list. Can print forwards or backwards
* Number of items in the list: Count the number of items in the list
* Presence of value in list: Return bool
* Remove item: Remove an item from the list
