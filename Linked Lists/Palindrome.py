# Cracking the Coding Interview - pp. 94 - q 2.6 

from SinglyLinkedList import SinglyLinkedList

class Solution:

    def solOne(self, headNode):
        
        """
            OBJECTIVE: Check if a linked list is a palindrome

            Time Complexity: O(n) where n = length of linked list because linked list will be traversed twice, even though it's only reaching the halfway point.
                            Also, the return statement involves reversing a list and that list has n elements.

            Space Complexity: O(n) where n = length of linked list. In the 2nd while-loop, the left-half and right-half elements are added to their appropriate list.
        """

        # If headNode is empty or by itself, return true
        if headNode == None or headNode.next == None:
            return True
        
        # Create tortoise and hare node pointers
        tortoise = headNode
        hare = headNode

        # Traverse linked list
        # IMPORTANT: "hare.next" is added because "hare.next.next" will throw an error if "hare.next" is empty
        while hare != None and hare.next != None:

            # Move hare 2 nodes at a time and tortoise one node at a time
            hare = hare.next.next
            tortoise = tortoise.next

        # Move hare back to the beginning
        hare = headNode

        # Move both pointers and compare node's value
        # IMPORTANT: At this point, tortoise is already at the middle of the linked list and hare is sent back to the front for going out-of-bounds
        hareList = list()
        tortoiseList = list()
        while tortoise != None:

            # If both don't share the same value, then linked list isn't a palindrome
            # if tortoise.val != hare.val:
            #     return False

            hareList.append(hare.val)
            tortoiseList.append(tortoise.val)

            # Move both pointers one node at a time
            tortoise = tortoise.next
            hare = hare.next

        return hareList == tortoiseList[::-1]

def main():

    # Initialize linked list
    ll = SinglyLinkedList()
    ll.append("M")
    ll.append("O")
    ll.append("E")
    ll.append("M")

    # Initialize solution class
    sol = Solution()
    print(sol.solOne(ll.getHead()))

main()