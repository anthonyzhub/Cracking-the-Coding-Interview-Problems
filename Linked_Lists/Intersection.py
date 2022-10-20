# Cracking the Coding Interview - pp. 94 - q 2.7

from Node import Node

class Solution:

    def addPadding(self, headNode, num):

        # OBJECTIVE: Add extra nodes before headNode

        # Create a new head node
        newNode = Node()
        curHead = newNode # <= Hold reference to first newNode

        # Create additional nodes
        while num > 0:

            # Create another new node and chain it to current node
            newNode.next = Node()
            newNode = newNode.next

            # Decrement num
            num -= 1

        # Connect newNode to headNode
        newNode.next = headNode

        # Return head of extended linked list
        return curHead

    def bookSol(self, headA, headB):

        """
            OBJECTIVE: Find intersection point between both linked list. If one linked list is shorter than the other, add front padding to the shortest.

            Time Complexity: O(A + B + N) where A and B represents the size of each linked list. N = how long addPadding() will take to create new nodes
                            for the shortest linked list.
                            
                            Both lists are traversed at the beginning to determine its size, so that will take O(A + B) time where each variable represents
                            the length of their linked list.
                            
                            If one linked list is shorter than the other, new nodes will be added at the front of the shortest list. This will take O(N) where
                            N = the number of nodes that will be added for padding.

            Space Complexity: O(1) because neither new data structures that were created will change in size. A node object will always have the same size no matter what.

            IMPORTANT: I came up with this solution after reading one hint, so I will label this as a book solution
        """

        def linkedListLength(headNode):
            
            # OBJECTIVE: Calculate linked list's length.
            # NOTE: This didn't have to be a helper method

            # Copy headNode
            curNode = headNode

            # Iterate linked list
            size = 0
            while curNode != None:
                curNode = curNode.next
                size += 1

            return size

        # If either linked list is empty, return none because there's no intersection
        if headA == None or headB == None:
            return None

        # Find out which linked list is the longest
        sizeA = linkedListLength(headA)
        sizeB = linkedListLength(headB)

        # Add padding to shortest linked list (if there exist one)
        nodeA = headA
        nodeB = headB
        if sizeA == sizeB:
            pass
        elif sizeA > sizeB:
            nodeB = self.addPadding(headB, sizeA - sizeB - 1)
        else:
            nodeA = self.addPadding(headA, sizeB - sizeA - 1)

        # Iterate both linked list
        while nodeA != None:

            # If both share the same node, return the intersecting point
            if nodeA == nodeB:
                return nodeA

            # Move to next node
            nodeA = nodeA.next
            nodeB = nodeB.next

        return None

    def solOne(self, headA, headB):

        """
            OBJECTIVE: Find intersection point between both linked list. If one linked list is shorter than the other, add front padding to the shortest.

            Time Complexity: O(A + B) where A and B represents the size of each linked list. Both linked lists are traversed to figure out which node is
                            the intersection. 2 additional while-loops were add to traverse the longest linked list because the 1st while-loop would have
                            ended when the shorted linked list was done being traversed through.

            Space Complexity: O(A + B) because nodes from both linked lists were added to the set. In the worst case, an intersection never existed between
                            both linked lists. If there was an intersection point, the set's size would have varied because the intersection could have
                            been at the beginning or at the end of both linked lists.
        """

        # If either head is empty, return None
        if headA == None or headB == None:
            return None
        
        # Create a set to hold nodes from both linked list
        nodesLog = set()

        # Traverse both linked list
        curNodeA = headA
        curNodeB = headB

        while curNodeA != None and curNodeB != None:

            # Add curNodeA if it isn't inside set
            if curNodeA not in nodesLog:
                nodesLog.add(curNodeA)
            else:
                return curNodeA

            # After adding curNodeA, add curNodeB if it's not inside the set
            if curNodeB not in nodesLog:
                nodesLog.add(curNodeB)
            else:
                return curNodeB

            # Move nodes
            curNodeA = curNodeA.next
            curNodeB = curNodeB.next

        # Traverse headA's linked list
        # NOTE: headB could have reached end of linked list before curNodeA
        while curNodeA != None:
            
            # Add curNodeA if it isn't inside set
            if curNodeA not in nodesLog:
                nodesLog.add(curNodeA)
            else:
                return curNodeA
            
            # Move node
            curNodeA = curNodeA.next

        # Traverse headB's linked list
        # NOTE: headA could have reached end of linked list before curNodeB
        while curNodeB != None:
            
            # Add curNodeB if it isn't inside set
            if curNodeB not in nodesLog:
                nodesLog.add(curNodeB)
            else:
                return curNodeB
            
            # Move node
            curNodeB = curNodeB.next

        return None

def main():

    # Initialize linked list
    nodeA = Node(1)
    nodeA.next = Node(2)
    nodeA.next.next = Node(3)
    nodeA.next.next.next = Node(4)
    nodeA.next.next.next.next = Node(5)

    nodeB = Node(1)
    nodeB.next = nodeA.next.next.next
    # nodeB.next = Node(2)
    # nodeB.next.next = Node(3)

    # Initialize solution class
    sol = Solution()
    # ans = sol.solOne(nodeA, nodeB)
    ans = sol.bookSol(nodeA, nodeB)

    if ans != None:
        print("Intersecting node: " + str(ans))
    else:
        print("Intersection doesn't exist")

main()