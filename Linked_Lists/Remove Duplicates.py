# Cracking the Coding Interview - pp. 94 - q 2.1

from SinglyLinkedList import SinglyLinkedList

class RemoveDuplicates:

    def setSol(self, curNode):

        """
            OBJECTIVE: Answer solution with a hash set
            Time Complexity: O(n) where n = length of linked list
            Space Complexity: O(n) where n = length of hash set
        """

        # Create a set
        valueSet = set()

        # Traverse linked list
        prevNode = curNode
        while curNode != None:

            # If value already exist inside of set, have prevNode connect to curNode.next
            if curNode.val in valueSet:
                prevNode.next = curNode.next
            
            # If not, add value to set and update prevNode
            else:
                valueSet.add(curNode.val)
                prevNode = curNode

            # Move to next node
            curNode = curNode.next

    def tortoiseAndHare(self, headNode):

        """
            OBJECTIVE: Remove duplicate nodes from linked list
            Time Complexity: O(n^2) where n = length of linked list. This algorithm involves create 2 pointers (tortoise and hare). For each node, the linked
                                list is traversed from tortoise node to the end.
            Space Complexity: O(1) because no large datasets were created. Only 2 new nodes were created, but they are constant.
        """

        # Create a tortoise node (slow node)
        tortoise = headNode

        # Move tortoise
        while tortoise != None:

            # Create a hare node
            hare = tortoise

            # Move hare and remove nodes with same value
            while hare.next != None:

                # If both nodes share the same value, move (hop) 2 nodes to the right
                if hare.next.val == tortoise.val:
                    hare.next = hare.next.next

                # If not, move to next node
                else:
                    hare = hare.next

            tortoise = tortoise.next
    
    def solOne(self, headNode):

        """
            OBJECTIVE: Sort unsorted linked list
            Time Complexity: O(n log n) where n = length of linked list.
            Space Complexity: O(n) where n = length of buffer[] list in sortLinkedList().
        """

        # If headNode is empty or by itself, exit function
        if headNode is None or headNode.next is None:
            return

        # Create a list
        buffer = list()

        # Traverse linked list
        curNode = headNode
        while curNode != None: # <= ".next" added since tail node is attached (it's still a node)

            # Add node's value to list
            buffer.append(curNode.val)

            # Move to next node
            curNode = curNode.next

        # Sort list
        buffer.sort()

        # Traverse linked list
        curNode = headNode
        while curNode != None: # <= ".next" added since tail node is attached (it's still a node)

            # Pop element from list and use it to update curNode's value
            curNode.val = buffer.pop(0)

            # Move to next node
            curNode = curNode.next

        # Traverse linked list
        prevNode = headNode
        curNode = headNode.next
        while curNode != None:

            # If current and last node share same value, delete last node
            if prevNode.val == curNode.val:
                prevNode.next = curNode.next

            # Move to next node
            curNode = curNode.next
        
def main():

    # Initialize linked list
    ll = SinglyLinkedList()
    ll.append(0)
    ll.append(0)
    ll.append(21)
    ll.append(12)
    ll.append(0)
    ll.append(0)
    ll.append(0)

    # Initialize solution
    sol = RemoveDuplicates()
    sol.tortoiseAndHare(ll.getHead())
    # sol.setSol(ll.getHead())
    # sol.solOne(ll.getHead())
    ll.printList()

main()