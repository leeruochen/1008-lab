class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.data is value: # see if temp matches with value, if not move temp to next node
                return temp
            temp = temp.next
        print( 'Search Error: Value not found' )

    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head # set new node's next to current head
            self.head = node # update head to new node

    def delete(self, value):
        prev = None
        temp = self.head
        while temp is not None:
            if temp.data is not value:
                prev = temp # keep track of prev node
                temp = temp.next # set node to next since it is not equal
            else:
                if temp == self.head:
                    self.deleteAtHead()
                else:
                    prev.next = temp.next
                    del temp
                return
        print( 'Value ', value, ' cannot be found' )

    def deleteAtHead(self):
        # Delete the first node in the list.
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        self.head = self.head.next

    def printList(self):
        print('Current list content:')
        temp = self.head
        while temp is not None:
            print( '[',temp.data,']' )
            temp = temp.next
        print()

    # q4, returns a new list containing data in non-decreasing order
    def mergeLinkedList(self, list2):
        if self.head is None:
            self.head = list2.head
            return self
        elif list2.head is None:
            return self
    
        mergedList = SinglyLinkedList()

        dummy = SinglyListNode(0)
        current = dummy

        temp1 = self.head
        temp2 = list2.head

        # compare nodes from both lists and insert the smaller one into the merged list
        while temp1 is not None and temp2 is not None:
            if temp1.data <= temp2.data:
                current.next = temp1
                temp1 = temp1.next
            else:
                current.next = temp2
                temp2 = temp2.next

            current = current.next

        # Append any remaining nodes from either list
        if temp1 is not None:
            current.next = temp1

        elif temp2 is not None:
            current.next = temp2

        mergedList.head = dummy.next
        return mergedList