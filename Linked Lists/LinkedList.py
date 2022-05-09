from Node import Node

class LinkedList:

    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.size = 0

    def append(self, val):

        # OBJECTIVE: Add a new node to the end of the list

        # Create a new node
        newNode = Node()
        newNode.val = val

        # If head is by itself, add newNode after it
        if self.head.next == None:

            # Connect newNode to head and tail nodes
            newNode.prev = self.head
            newNode.next = self.tail

            # Connect head and tail nodes to newNode
            self.head.next = newNode
            self.tail.prev = newNode
        
        # If not, add newNode before tail node
        else:

            # Get node before tail
            lastNode = self.tail.prev

            # Connect lastNode to newNode and vice versa
            lastNode.next = newNode
            newNode.prev = lastNode

            # Connect newNode to tail node and vice versa
            newNode.next = self.tail
            self.tail.prev = newNode

        self.size += 1

    def getHead(self):

        # OBJECTIVE: Return head node if it exists

        # If there's no head node, exit function
        if self.head.next == None:
            return

        return self.head.next

    def getSize(self):

        # OBJECTIVE: Get linked list size
        return self.size

    def printList(self):

        # OBJECTIVE: Print linked list from head

        # If linked list is empty, exit function
        if self.head.next == None:
            print("Linked list is empty")
            return

        # Get head node
        curNode = self.head.next

        # Traverse linked list
        while curNode.next != None:
            print(curNode.val, sep=" => ", end=" ")
            curNode = curNode.next