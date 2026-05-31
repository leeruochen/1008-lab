class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, node):
        if self.head is None:
            self.head = self.tail = node # if list is empty, set head and tail to the new node
        else:
            self.head.prev = node # set current head's prev to new node
            node.next = self.head # set new node's next to current head
            self.head = node # update head to new node

    def delete(self, value):
        temp = self.head
        while temp is not None:
            if temp.data is not value:
                temp = temp.next # temp is not equal to value, move temp to next node
            else:
                if temp is self.head:
                    self.head = self.head.next # if temp is head, update head to next
                elif temp is self.tail:
                    self.tail = self.tail.prev # if temp is tail, update tail to prev
                else:
                    # if temp is in the middle, update prev and next pointers to skip temp
                    prev = temp.prev
                    succ = temp.next
                    prev.next = succ
                    succ.prev = prev
                del temp
                return
        print( 'Delete: Value not found' )

    def printList(self):
        print('Current list content:')
        temp = self.head
        while temp is not None:
            print( '[',temp.data,']' )
            temp = temp.next
        print()
