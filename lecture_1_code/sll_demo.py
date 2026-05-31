from singlylinkedlist import SinglyLinkedList
from singlylinkedlist import SinglyListNode

aList = SinglyLinkedList()
aNode = SinglyListNode(40)
aList.insertAtHead(aNode)
aNode2 = SinglyListNode(30)
aList.insertAtHead(aNode2)
aNode3 = SinglyListNode(10)
aList.insertAtHead(aNode3)
aList.printList()


bList = SinglyLinkedList()
bNode = SinglyListNode(35)
bList.insertAtHead(bNode)
bNode2 = SinglyListNode(25)
bList.insertAtHead(bNode2)
bNode3 = SinglyListNode(15)
bList.insertAtHead(bNode3)
bList.printList()

# Merge the two lists
mergedList = aList.mergeLinkedList(bList)
mergedList.printList()
