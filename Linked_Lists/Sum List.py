# Cracking the Coding Interview - pp. 94 - q 2.5

from SinglyLinkedList import SinglyLinkedList
from Node import Node

class Solution:

    def summation(self, headNode, exp):

        # OBJECTIVE: Go to last node of linked list and convert digits into 1 big number
        # E.g., Input: 7 => 1 => 6 Output: 617

        # If headNode is empty, return 0
        if headNode == None:
            return 0

        # Make a recursive call on remaining nodes
        # NOTE: 10**exp is used to turn digit into appropriate number
        # E.g, 6 in 7 => 1 => 6 is 600, so calculate 6 * 10^2
        return (headNode.val * 10**exp) + self.summation(headNode.next, exp + 1)

    def recursiveSol(self, headA, headB):

        """
            OBJECTIVE: Find sum of number in linked list using a recursive solution
                        Linked list is storing a number with its digits in reverse order. E.g., 7 - 1 - 6 is 617.

            Time Complexity: O(1) because loops weren't used in the algorithm

            Space Complexity: O(n) where n = length of linked list (assuming both linked lists are the same size). A recursive call
                            takes up with memory because of stacking.

            IMPORTANT: I misread the problem and solved another one. I'll keep this here since it's still useful. =)
        """

        # If both linked list are empty, exit function
        if headA == None and headB == None:
            return 0

        # Compute sum of both linked lists
        return self.summation(headA, 0) + self.summation(headB, 0)

    def bookSol(self, headA, headB, carryOver):

        """
            OBJECTIVE: Write a function that adds 2 new numbers and returns the sum as a linked list

            Time Complexity: O(1) because loops weren't used in the algorithm

            Space Complexity: O(n) where n = length of the sum's linked list. headA and headB will be added together to create a new number. That new number will
                            have its digit stored in a new linked list where each digit will have its own node. Each node will be made per recursive call and a
                            recursive call takes up with memory because of stacking.
        """

        # If both lists are empty and there's nothing to carry over, exit function
        if headA == None and headB == None and carryOver == 0:
            return

        # Create a new linked list node
        newNode = Node()

        # Compute newNode's potential value (depending if total exceeds 9)
        newVal = carryOver + headA.val + headB.val

        # Divide newVal by 10 and add it to newNode
        newNode.val = newVal % 10

        # Create a new node
        rightNodes = self.bookSol(headA.next, headB.next, 1 if newVal >= 10 else 0)
        newNode.next = rightNodes

        return newNode

def main():

    # Create 2 linked lists
    listA = SinglyLinkedList()
    listB = SinglyLinkedList()

    listA.append(7)
    listA.append(1)
    listA.append(6)

    listB.append(5)
    listB.append(9)
    listB.append(2)

    # Initialize solution class
    sol = Solution()
    # print(sol.recursiveSol(listA.getHead(), listB.getHead()))

    headNode = sol.bookSol(listA.getHead(), listB.getHead(), 0)
    while headNode != None:
        print(headNode.val)
        headNode = headNode.next

main()