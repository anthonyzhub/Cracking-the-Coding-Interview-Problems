# Cracking the Coding Interview - pp. 94 - q 2.3

from SinglyLinkedList import SinglyLinkedList

class DeleteMiddleNode:

    def solOne(self, midNode):

        """
            OBJECTIVE: Given a middle node, delete it while still keeping the linked list connected as one.
            Time Complexity: O(n/2) where n = length of linked list. The function is given the middle node of
                            a linked list. I only need to traverse the right-half of the linked list, instead
                            of the entire list.
            Space Complexity: O(1) because all 3 pointers take constant space. No large data structures were
                            created.    
        """

        # Create 2 pointers
        prevNode = midNode
        curNode = midNode
        nextNode = curNode.next

        # Swap values between curNode and nextNode until the end of the linked list
        movePrev = False
        while nextNode != None:

            # Swap values
            tmpValue = curNode.val
            curNode.val = nextNode.val
            nextNode.val = tmpValue

            # Move nodes
            curNode = curNode.next
            nextNode = nextNode.next

            # After first loop, start to move prevNode. 
            if movePrev == False:
                movePrev = True
            else:
                prevNode = prevNode.next

        # Disconnect prevNode from remaining nodes
        prevNode.next = None

        # Delete last node which is curNode. nextNode is already empty because it went pass the linked list
        del curNode
        del nextNode

def main():

    # Initialize linked list
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.printList()
    print()

    # Delete middle node
    sol = DeleteMiddleNode()
    sol.solOne(ll.getMiddle())
    ll.printList()

main()