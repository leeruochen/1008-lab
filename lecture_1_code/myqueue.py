from singlylinkedlist import SinglyLinkedList
from singlylinkedlist import SinglyListNode

class MyQueue:
    def __init__(self):
        self.list = SinglyLinkedList()
    
    def enqueue(self, value):
        new_node = SinglyListNode(value)
        self.list.insertAtHead(new_node)

    def printQueue(self):
        self.list.printList()
    
    def dequeue(self):
        if self.list.head is None:
            print("Queue is empty, cannot dequeue.")
            return None
        
        # To dequeue, we need to find the last node (the tail) and remove it
        prev = None
        temp = self.list.head
        
        # iterates till the tail node is reached
        while temp.next is not None:
            prev = temp
            temp = temp.next
        
        # temp is now the tail node
        value = temp.data
        
        if prev is not None:
            prev.next = None  # Remove the tail node
        else:
            self.list.head = None  # Queue had only one element, now it's empty
        
        del temp  # Free the memory of the dequeued node
        return value
    
    # queue follows FIFO, so peek returns tail value as enqueue adds to head
    def peek(self):
        if self.list.head is None:
            print("Queue is empty, cannot peek.")
            return None
        
        temp = self.list.head
        while temp.next is not None:
            temp = temp.next
        
        return temp.data  # Return the value of the tail node without removing it