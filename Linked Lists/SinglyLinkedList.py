from Node import Node

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, val):

        # OBJECTIVE: Add a new node to the end of the list

        # Create a new node
        newNode = Node()
        newNode.val = val

        # If head is by itself, add newNode as head
        if self.head == None:
            self.head = newNode
        
        # If not, add newNode before tail node
        else:

            # Traverse linked list to the end
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next

            # Link last node with new node
            curNode.next = newNode

        self.size += 1

    def getHead(self):

        # OBJECTIVE: Return head node if it exists

        # If there's no head node, exit function
        if self.head == None:
            return

        return self.head

    def getSize(self):

        # OBJECTIVE: Get linked list size
        return self.size

    def printList(self):

        # OBJECTIVE: Print linked list from head

        # If linked list is empty, exit function
        if self.head == None:
            print("Linked list is empty")
            return

        # Get head node
        curNode = self.head

        # Traverse linked list
        while curNode != None:
            print(curNode.val, end=" ")
            curNode = curNode.next