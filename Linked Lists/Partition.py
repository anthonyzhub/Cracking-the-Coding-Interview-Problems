from SinglyLinkedList import SinglyLinkedList
from Node import Node

class Solution:

    def summation(self, headNode, exp):

        # OBJECTIVE: Make a recursive call for the remaining nodes before computing sum

        # If headNode is empty, return 0
        if headNode == None:
            return 0

        return (headNode.val * 10**exp) + self.summation(headNode.next, exp + 1)

    def recursiveSol(self, headA, headB):

        """
            OBJECTIVE: Find sum of number in linked list using a recursive solution
                        Linked list is storing a number with its digits in reverse order. E.g., 7 - 1 - 6 is 617.

            Time Complexity: O(A + B) where A and B represents each linked list's size. Each linked list
                            is being traversed through to calculate the sum.
            Space Complexity: O(A + B) where A and B represents each linked list's size. A recursive call
                            takes up with memory because of stacking.
        """

        # If both linked list are empty, exit function
        if headA == None and headB == None:
            return 0

        # If either linked list is empty, let the non-empty list continue
        if headA == None:
            return self.summation(headA, 0)
        elif headB == None:
            return self.summation(headB, 0)

        # If both lists are non-empty, compute sum of each one
        return self.summation(headA, 0) + self.summation(headB, 0)

    def bookSol(self, headA, headB, carryOver):

        # If both lists are empty and there's nothing to carry over, exit function
        if headA == None and headB == None and carryOver == 0:
            return

        # Create a new linked list node
        newNode = Node()

        # Copy carry over value
        newVal = carryOver

        # If either linked list are non-empty, add its value to newVal
        if headA is not None:
            newVal += headA.val
        
        if headB is not None:
            newVal += headB.val

        # Divide newNval by 10 and add it to newNode
        newNode.val = newVal % 10

        # Make a recursive call for either non-empty linked list
        if headA is not None or headB is not None:

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
    listB.append(9)

    # Initialize solution class
    sol = Solution()
    print(sol.recursiveSol(listA.getHead(), listB.getHead())



main()