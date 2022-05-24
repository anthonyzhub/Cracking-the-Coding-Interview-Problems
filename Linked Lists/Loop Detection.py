# Cracking the Coding Interview - pp. 95 - q 2.8

from Node import Node

class Ans:

    """
        OBJECTIVE: Create a class to hold multiple outputs from Solution.solOne()
        
        NOTE: Python allows functions to return more than 1 output. I chose this approach since it's more organized 
            and other languages (C++ & Java) don't allow functions to return more than 1 output.
    """
    def __init__(self, node, boolean) -> None:
        self.node = node
        self.boolean = boolean

class Solution:

    def solOne(self, headNode):

        """
            OBJECTIVE: Check if there's a cycle inside the linked list using the tortoise and hare method
        
            NOTE: The tortoise and hare method uses 2 node pointers to traverse the linked list. The hare
                will move faster than the tortoise. Both will intersect each other inside the circular part of the linked list.
                From there, the hare will move back to the beginning of the linked list and move as the same rate as the tortoise.
                Both pointers will intersect again at the beginning of the cycle.

            Time Complexity: O(n) where n = length of linked list. The linked list is being traversed at most 2 times. The 1st
                            is to verify that the linked list has a cycle. The 2nd time is to find out where the cycle begins

            Space Complexity: O(1) because no dynamic data structures were created. Only 2 nodes were created and both occupy
                            constant space.
        """

        # If headNode is empty, exit function
        if headNode == None:
            return Ans(headNode, False)

        # Create 2 pointers
        tortoise = headNode
        hare = headNode

        # Iterate list. If linked list doesn't have a cycle, then hare will go out-of-bounds. 
        firstRun = True
        while (hare != None and hare.next != None):

            # Check if tortoise and hare overlap
            if hare == tortoise:

                # If firstRun is false, then exit while-loop because both pointers overlapped pass the starting line
                if firstRun == False:
                    break

                # Set variable to false during the first loop
                else:
                    firstRun = False
            
            # Move to next node
            hare = hare.next.next
            tortoise = tortoise.next

        # If hare or hare.next is none, then a tail node exist and a cycle doesn't exist
        if hare == None or hare.next == None:
            return Ans(headNode, False)

        # Set hare node back to the front
        hare = headNode

        # Re-iterate linked list with hare moving 1 node per loop (same rate as tortoise)
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next

        return Ans(hare, True)

def main():

    # Initialize linked list
    nodeA = Node(1)
    nodeB = Node(2)
    nodeC = Node(3)
    nodeD = Node(4)

    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    # nodeD.next = None
    nodeD.next = nodeB

    # Initialize solution class
    sol = Solution()
    ans = sol.solOne(nodeA)
    
    if ans.boolean == False:
        print("Cycle undetected")
    else:
        print("Cycle detected at {}".format(ans.node.val))

main()