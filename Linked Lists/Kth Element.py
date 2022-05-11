# Cracking the Coding Interview - pp. 94 - q 2.2

from SinglyLinkedList import SinglyLinkedList

class KElement:

    def solOne(self, headNode, k):

        """
            OBJECTIVE: Create 2 pointers to find the kth element inside of linked list. Assume k is at most length of linked list.
            Time Complexity: O(n) where n = length of linked list. List is being traversed once.
            Space Complexity: O(1) because only 2 new nodes were created and its space is constant.
        """

        # If headNode is empty, exit function
        if headNode is None:
            return

        # If headNode is by itself, return its value
        elif headNode.next is None:
            return headNode.val

        # If k == 1, return headNode's value
        if k == 1:
            return headNode.val

        # Create 2 pointers
        firstPtr = headNode
        secondPtr = headNode

        # Traverse linked list
        pos = 0
        while firstPtr != None:

            # Check if Kth element has been reached
            if pos > k - 1:
                secondPtr = secondPtr.next

            # Move firstPtr and update pos
            firstPtr = firstPtr.next
            pos += 1

        # Return value of Kth element
        return secondPtr.val

        """
        # NOTE: A little more advanced. 
        # If K can be greater than linked list's length, then a few changes will need to be made. (1) Edge case of
        #    linked list only have one element needs to be deleted. What happens if k = 10 and linked list only has
        #    1 node. (2) Uncomment the below if-condition to compare secondPtr against headNode. If both share the
        #    same memory address, then K is greater than linked list's length because secondPtr never moved from
        #    starting position.
        if secondPtr == headNode:
            return -1
        else:
            return secondPtr.val
        """

def main():

    # Initialize linked list
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(10)
    ll.append(100)
    ll.append(1000)

    # Initialize solution class
    sol = KElement()
    ans = sol.solOne(ll.getHead(), ll.size)

    print(ans)

main()