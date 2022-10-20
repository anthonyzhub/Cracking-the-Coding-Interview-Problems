# Cracking the Coding Interview - pp. 110 - q 4.4

from TreeNode import Node

class Balanced:

    def __init__(self) -> None:
        pass

    def getHeight(self, root, level):

        # OBJECTIVE: Traverse subtree and return max height

        # If root is None, return level
        if root is None:
            return level
        
        # Calculate height of left and right subtree
        leftSubTree = self.getHeight(root.left, level + 1)
        rightSubTree = self.getHeight(root.right, level + 1)

        # Return maximum height between the subtrees
        return max(leftSubTree, rightSubTree)

    def check(self, root):

        """
        /*
         * OBJECTIVE: Determine if given binary tree is balanced. A balanced tree has 2 subtrees with heights that don't differ by more than 1 level.
         * 
         * Time Complexity: O(V + E) where V = # of vertices (nodes) and E = # of edges (lines between nodes). check() traverses the left and right
         *                  subtree with getHeight(). getHeight() visits every nodes, increments level, and returns maximum height between subtrees.
         * 
         * Space Complexity: O(V) where V = # of vertices (nodes) inside of the tree because a recursive call is made per vertex. After visiting a vertex,
         *                  a recursive call is made to visit the vertex's children. Each call is saved on the memory stack.
         */
        """

        # If root is None, return true
        if root is None:
            return True
        
        # Calculate height of left and right subtree
        leftSubTree = self.getHeight(root.left, 1)
        rightSubTree = self.getHeight(root.right, 1)

        # Calculate height difference between both subtrees
        diff = abs(leftSubTree - rightSubTree)

        # If height difference is at most 1 level, return true. If not, return false.
        if diff <= 1:
            return True
        
        return False

def main():

    # Create a tree
    root = Node()
    root.left = Node()
    root.right = Node()

    root.left.left = Node()
    root.left.left.left = Node()

    # Initialize solution
    sol = Balanced()
    print(sol.check(root))

main()