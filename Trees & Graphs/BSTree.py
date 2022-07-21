# Cracking the Coding Interview - pp. 111 - q 4.11

from collections import deque
from TreeNode import Node
from random import choice, randint

class BookNode:

    def __init__(self, val) -> None:

        # Hold value and this node's children
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

        # Hold number of children (including all descendants) this node has
        self.size = 1

    def inorder(self):

        # OBJECTIVE: Print tree in in-order

        if self.val:

            self.left.inorder()
            print(self.val, end=" ")
            self.right.inorder()

    def getIthNode(self, i):
        
        # OBJECTIVE: Return ith node from root

        # Get size of left subtree
        if self.left == None:
            leftSize = 0
        else:
            leftSize = self.left.size
        
        # If i is less than left subtree's size, move to left child
        if i < leftSize:
            return self.left.getIthNode(i)

        # If this node is the ith node, return it
        elif i == leftSize:
            return self

        else:
            return self.right.getIthNode(i - (leftSize + 1))

    def insertInOrder(self, value):

        # OBJECTIVE: Create a new node with designated value on the tree in the proper order (this is a BST)

        # If value is less than or equal to this node's value, go to the left subtree
        if value <= self.val:
            
            # If a left child doesn't exist, create one now
            if self.left == None:
                self.left = BookNode(value)
                self.left.parent = self
            else:
                self.left.insertInOrder(value)

        else:

            # If a right child doesn't exist, create one now
            if self.right == None:
                self.right = BookNode(value)
                self.right.parent = self
            else:
                self.right.insertInOrder(value)

        # Increment this node's size counter
        size += 1

    def delete(self, value):

        # OBJECTIVE: Delete node with matching value

        # Find node with matching value
        suspect = self.find(value)

        # Get suspect's parent node
        parent = suspect.parent

        # Remove suspect
        if parent.left == suspect:

            # If suspect has a right child, set it as new parent and link left child as child of right sibling
            if suspect.right:

                parent.left = suspect.right

                if suspect.left:
                    suspect.right.left = suspect.left

            # If suspect only has a left child, set it as new parent
            else:
                parent.left = suspect.left

        elif parent.right == suspect:

            # If suspect has a right child, set it as new parent and link left child as child of right sibling
            if suspect.right:

                parent.right = suspect.right

                if suspect.left:
                    suspect.right.left = suspect.left

            # If suspect only has a left child, set it as new parent
            else:
                parent.right = suspect.left

        del suspect

    def find(self, value):

        # OBJECTIVE: Return node that has matching value

        # Compare input value against node's value
        if value == self.val:
            return self

        # Go to appropriate child
        elif value < self.val:
            return self.left.find(value)

        elif value > self.val:
            return self.right.find(value)

        # If function is still continuing, return None because value doesn't exist inside tree
        return None

class BookTree:

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def inorder(self):

        # OBJECTIVE: Print tree in in-order

        if self.root:
            self.root.inorder()

    def getRandomNode(self):

        """
        * OBJECTIVE: Return a random node from the tree
        *
        * Time Complexity: O(d) where d = depth of the tree. getRandomNode() generates a random number from 0 to self.size.
        *                   From there, it will traverse the entire until the ith node is found. This all depends on how
        *                   big the tree is. Remember, the root node will have the total number of nodes listed under its
        *                   subtrees. The children of the root will hold the size of their subtrees minus root.
        *
        * Space Complexity: O(log n) where n = number of nodes inside the tree. Since this is a BST, you can either return
        *                   the current node, or visit the left/right child. If a child will be visited, a recursive call
        *                   will be made and the call will be saved on the memory stack.
        """

        # If tree is empty, exit function
        if self.root == None:
            return
        
        # Generate a random number
        i = randint(self.size)

        # Get ith node from tree
        return self.root.getIthNode(i)

    def insertInOrder(self, value):

        # OBJECTIVE: Create a new node with dedicated value and insert it to tree in proper order (this is a BST)

        # If tree is empty, set new node as root
        if self.root == None:
            self.root = BookNode(value)

        # If tree isn't empty, add value to dedicated spot in tree
        else:
            self.root.insertInOrder(value)

class MyTree:

    def __init__(self) -> None:
        self.size = 0
        self.root = None
        self.lastNode = None
        self.children = list()

    def inorder(self):

        # OBJECTIVE: Print tree in inorder traversale

        def helper(root, path):

            if root:

                helper(root.left, path)
                print(root.val, end=" ")
                helper(root.right, path)

        # If tree is empty, exit function
        if self.size == 0:
            return

        helper(self.root, "")

    def insert(self, newVal):

        # OBJECTIVE: Create a new node and insert to tree with newVal

        # Create a new node
        newNode = Node(newVal)

        # If tree is empty, set newNode as root
        if self.size == 0:
            self.root = newNode
            self.lastNode = newNode

        else:

            # Copy root node
            curNode = self.root

            # Traverse to the bottom of the tree
            while True:

                # If newNode's value already exist inside of tree, delete newNode and exit function
                if curNode.val == newNode.val:
                    del newNode
                    return

                # If newNode's value is less than curNode, go to left child
                if newNode.val < curNode.val and curNode.left != None:
                    curNode = curNode.left

                # If newNode's value is less than curNode and curNode doesn't have a left child, set newNode as left child
                elif newNode.val < curNode.val:
                    curNode.left = newNode
                    newNode.parent = curNode
                    break

                # If newNode's value is greater than curNode, go to right child
                elif newNode.val > curNode.val and curNode.right != None:
                    curNode = curNode.right

                # If newNode's value is greater than curNode and curNode doesn't have a right child, set newNode as right child
                elif newNode.val > curNode.val:
                    curNode.right = newNode
                    newNode.parent = curNode
                    break

        self.children.append(newVal)
        self.size += 1

    def find(self, element):

        # OBJECTIVE: Return node holding "element" as value

        # If tree is empty, exit function
        if self.size == 0:
            return

        # Create a queue
        queue = deque([self.root])

        # Iterate queue
        while queue:

            # Pop 1st element from queue
            popped = queue.popleft()

            # If popped node contains "element", return it
            if popped.val == element:
                return popped

            # Add popped node's children to queue
            if popped.left:
                queue.append(popped.left)

            if popped.right:
                queue.append(popped.right)

    def delete(self, element):

        # OBJECTIVE: Delete node holding "element" as value

        # If tree is empty, exit function
        if self.size == 0:
            return
        
        # Get node holding element
        desiredNode = self.find(element)

        # If find() returned none, exit function
        if desiredNode == None:
            return

        # Get parent node of desiredNode
        parentNode = desiredNode.parent

        # If desiredNode is a leaf node, delete connection from parent and return node
        if desiredNode.left == None and desiredNode.right == None:
            
            # Find out if desiredNode is a left or right child
            if parentNode.left == desiredNode:
                parentNode.left = None
            
            elif parentNode.right == desiredNode:
                parentNode.right = None
        
        # If desiredNode does have children, replace desiredNode for a child
        else:

            # If there's a right child, set it as new parent
            # NOTE: BST properties state that the right child will always be greater than the left. Left Child <= Root < Right Child
            if desiredNode.right:

                # Set desiredNode's right child as a direct child of desiredNode.parent
                if parentNode.left == desiredNode:

                    # Set right child as a direct child of parent
                    parentNode.left = desiredNode.right

                    # Set desiredNode's left child as the left child of desiredNode.right
                    desiredNode.right.left = desiredNode.left
            
                elif parentNode.right == desiredNode:
                    
                    # Set right child as a direct child of parent
                    parentNode.right = desiredNode.right

                    # Set desiredNode's left child as the left child of desiredNode.right
                    desiredNode.right.left = desiredNode.left

            # If a right child doesn't exist, but a left child does, set it as new parent
            else:

                # Set desiredNode's left child as a direct child of desiredNode.parent
                if parentNode.left == desiredNode:

                    # Set left child as a direct child of parent
                    parentNode.left = desiredNode.left
            
                elif parentNode.right == desiredNode:
                    
                    # Set left child as a direct child of parent
                    parentNode.right = desiredNode.left

        del desiredNode
        self.children.remove(element)
        self.size -= 1
        
    def getRandomNode(self):
        
        """
        * OBJECTIVE: Return a random node from tree
        *
        * Time Complexity: O(n) where n = # of nodes inside the tree. This approach has 2 data structures: a list and
        *                   a tree. The list only holds the values of every node that exist inside the tree and the 
        *                   tree holds the actual nodes.
        *
        *                   choice() randomly select a value from the list. This can take at most n-times because the
        *                   function will iterate the list and might return the last element.
        *
        *                   find() is based off of breadth-first search. The time complexity for that will be O(n)
        *                   because each node will be searched for until randElem is found
        *
        * Space Complexity: O(n) where n = # of nodes inside the queue and list. The queue will continuously add nodes
        *                   to itself until randElem is found. The list holds all the elements inside the tree for 
        *                   convenience.
        """
        
        # If tree is empty, exit function
        if self.size == 0:
            return
        
        # Generate a random index and get element at index
        randElem = choice(self.children)
        return self.find(randElem)

def main():

    # Initialize class
    """bstree = MyTree()
    bstree.insert("A")
    bstree.insert("B")
    bstree.insert("C")
    bstree.insert("D")
    bstree.insert("E")
    bstree.insert("F")
    bstree.insert("G")
    bstree.insert("H")
    bstree.insert("I")
    bstree.insert("J")"""

    bookTree = BookTree()
    bookTree.insertInOrder("A")
    bookTree.insertInOrder("B")
    bookTree.insertInOrder("C")
    bookTree.insertInOrder("D")
    bookTree.insertInOrder("E")
    bookTree.insertInOrder("F")
    bookTree.insertInOrder("G")
    bookTree.insertInOrder("H")
    bookTree.insertInOrder("I")
    bookTree.insertInOrder("J")

    # Print random node
    elemToDelete = bookTree.getRandomNode().val
    print(elemToDelete)
    bookTree.find("F")
    bookTree.inorder(); print()
    bookTree.delete(elemToDelete)
    bookTree.inorder()

main()