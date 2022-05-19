from SinglyLinkedList import SinglyLinkedList

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
    print(sol.recursiveSol(listA.getHead(), listB.getHead()))

main()