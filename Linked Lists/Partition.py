# Cracking the Coding Interview - pp. 95 - q 2.4

from SinglyLinkedList import SinglyLinkedList

class Solution:

    def bookSol(self, headNode, pivot):

        """
            OBJECTIVE: Partition linked list with any elements smaller than or equal to pivot appearing first,
                        then add remaining elements to the end of the list.

            NOTE: We're assuming that keeping the linked list in its original order doesn't matter.
            
            Time Complexity: O(n) where n = length of linked list. The linked list is being traversed twice.

            Space Complexity: O(1) because no dynamic data structures were created. The 2 nodes that were created
                            will always take up the same amount of space.
        """

        # Create 2 new nodes
        newHead = headNode
        newTail = headNode

        # Iterate linked list
        curNode = headNode
        while curNode != None:

            # Get node after curHead
            nextNode = curNode.next

            # If curNode.val is less than pivot, insert it in front of newHead
            if curNode.val < pivot:
                curNode.next = newHead
                newHead = curNode

            # If curNode.val is greater than or equal to pivot, add after tail
            else:
                newTail.next = curNode
                newTail = curNode

            # Move node
            curNode = nextNode

        # Set tailNode's next pointer to None
        newTail.next = None

        # Return new head node
        return newHead

    def solOne(self, headNode, pivot):

        """
            OBJECTIVE: Partition linked list with any elements smaller than or equal to pivot appearing first,
                        then add remaining elements to the end of the list.

            NOTE: We're assuming that keeping the linked list in its original order doesn't matter.
            
            Time Complexity: O(n) where n = length of linked list. The linked list is being traversed twice.

            Space Complexity: O(n) where n = the number of elements inside of the linked list. 2 new arrays
                            are created to hold the smallest and largest elements inside of the linked list
                            compared to the pivot.
        """

        # If headNode is none or by itself, return it
        if headNode == None or headNode.next == None:
            return headNode
        
        # Create 2 lists to hold small and large elements
        smallerElems = list()
        biggerElems = list()

        # Traverse matrix and add element's value to appropriate list
        curNode = headNode
        while curNode != None:

            # If curNode.val is bigger or equal to pivot, add it to biggerElems list. If not, add it to smallerElems
            if curNode.val >= pivot:
                biggerElems.append(curNode.val)
            else:
                smallerElems.append(curNode.val)

            # Move to next node
            curNode = curNode.next

        # Traverse matrix again and add update all node's values from lists
        curNode = headNode
        while curNode != None:

            # Add all elements from smallerElems to list, then biggerElems
            if len(smallerElems) > 0:
                curNode.val = smallerElems.pop()
            else:
                curNode.val = biggerElems.pop()

            # Move node
            curNode = curNode.next

def main():

    # Create a linked list
    ll = SinglyLinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)

    # Initialize solution class
    sol = Solution()
    sol.solOne(ll.getHead(), 5)
    ll.printList()

main()