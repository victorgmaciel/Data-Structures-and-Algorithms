"""
Linked Lists

every linked list consists of nodes. 
Every node has two components:
1. Data
2. Next

Data, stores an element of data that can be:
- string
- char
- integer
- any other type of object. 

Next, is a pointer that points from one node to another. 

Lets say we have a linked list as follows:

____       _____      _____
|A| | ---> |B| | ---> |C| |---> 


Here we can see three nodes. 
the start of the linked list is referred as the HEAD.
Head, is a pointer that points to the beginning of the Linked List. 

If we wanted to traverse through this linked list above, 
we'll start at the head.

The last node points to a null object referred as None. It signifies the end of the list.

Finally, lets get started on the implementation!
"""


from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
class LinkedList:
    def __init__(self):
        self.head = None

"""
By creating the class Node and giving the self and data arguments, we will have every node containing a data and a next. 

By creating the LinkedList class, we're definind the head pointer which will point to the first node in the LinkedList, for now and like the next attribute, they're both equal None. 
"""

"""Now we'll talk about insertion for linked lists
- append
- prepend
insert_after_node
"""

"""Append
 This method inserts an element at the end of the linked list. 

"""
def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    last_node = self.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node

"""
Here we have a new defined new_node using the Node class defined early. It has data and next fields. 

the if statement checks if the linked list is empty, if so new_node is now the head of the list."""
