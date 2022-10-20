# Cracking the Coding Interview - pp. 109 - q 4.2

from TreeNode import Node

class Minimal:

    def __init__(self) -> None:
        
        # Create root node
        self.root = None

    def add(self, newVal):

        """
        /*
         * OBJECTIVE: Add a new node to tree
         * 
         * Time Complexity: O(n log n ) where n = # of nodes that exist inside of the tree. Each call involves traversing
         *                  the tree starting from the root. After each call, a new node will be added to the tree.
         * 
         * Space Complexity: O(h) where h = height of tree. addNode() makes a recursive call until it reaches the bottom
         *                  of the tree. Each recursive call is saved on a memory stack.
         */
         """

        def addNode(root, newNode):

            # OBJECTIVE: Move down the tree to find a perfect spot to add newNode

            # If root is empty, exit function
            if root is None:
                return
            
            # If newNode.val is less than root's, go to the left
            if root.val <= newNode.val:

                # If root doesn't have a left child, set newNode as root's left child.
                if root.left is None:
                    root.left = newNode

                # If not, continue traversing tree
                else:
                    addNode(root.left, newNode)

            # If newNode.val is greater than root's, go to the right
            else:

                # If root doesn't have a right child, set newNode as root's right child
                if root.right is None:
                    root.right = newNode

                # If not, continue traversing tree from right child
                else:
                    addNode(root.right, newNode)

        # If root is None, then add newVal to it since this is the first node of the tree
        if self.root is None:
            self.root = Node(newVal)
            return
        
        # Create a new node and add it to BST
        addNode(self.root, Node(newVal))

    def createMinimalBST(self, elems, startPtr, endPtr):
        
        """
        /*
         * OBJECTIVE: Continuosly add a new node to the tree from the array
         * 
         * Time Complexity: O(n) where n = # of elements inside of the array. Each element inside of elems[] will
         *                  have its own node that will be a part of the tree.
         * 
         * Space Complexity: O(n) where n = # of nodes inside the tree. Although nodes will take up constant space,
         *                  multiple nodes will be created based on the length of elems[]
         */
         """

        # If startPtr and endPtr overlaps, exit function
        if startPtr > endPtr:
            return
        
        # Create a new node from middle element
        midPtr = (startPtr + endPtr) // 2
        newNode = Node(elems[midPtr])

        # Add remaining elements to newNode as its children
        newNode.left = self.createMinimalBST(elems, startPtr, midPtr - 1)
        newNode.right = self.createMinimalBST(elems, midPtr + 1, endPtr)

        return newNode

    def preorder(self, root):

        # OBJECTIVE: Print nodes inside of tree in pre-order traversal

        # If root is None, exit function
        if root is None:
            return

        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def main():

    # Initialize class
    tree = Minimal()

    # Solution 1: Add each element from list to tree. This method is slower, even without the for-loop, because
    #              I'm always traversing the tree starting from its root per call
    elems = sorted([68, 41, 10, 46, 47, 82, 30, 23, 62, 63])
    for i in elems:
        tree.add(i)

    # Solution 2: Create a new node and its children per call. This is faster because traversing the tree
    #               won't always start at the root. Instead, root is created immediately with its children
    #               and those children will have their own family created instantly
    elems = sorted([68, 41, 10, 46, 47, 82, 30, 23, 62, 63])
    tree.createMinimalBST(elems, 0, len(elems) - 1)

main()