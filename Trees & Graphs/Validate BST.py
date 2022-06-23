# Cracking the Coding Interview - pp. 110 - q 4.5

from TreeNode import Node

class CheckClass:

    def dfs(self, root: Node, children: list):

        # OBJECTIVE: Traverse down tree and add children to appropriate list. Return true/false if BST condition is met

        # If root is empty, exit function
        if root is None:
            return

        # Add root to list
        children.append(root)
        
        # Visit children
        self.dfs(root.left, children)
        self.dfs(root.right, children)

    def isTreeBST(self, root: Node, leftChildren: list, rightChildren: list):

        # OBJECTIVE: Check that all nodes in leftChildren are less than or equal to root.val and all nodes in the rightChildren are greater than root.val

        # Iterate leftChildren
        # IMPORTANT: All nodes on the left side MUST be less than or equal to root.val
        for node in leftChildren:
            if node.val > root.val:
                return False
        
        # Iterate rightChildren
        # IMPORTANT: All nodes on the right side MUST be greater than root.val
        for node in rightChildren:
            if node.val <= root.val:
                return False

        return True

    def checkBST(self, root: Node):

        """
        /*
         * OBJECTIVE: Given the root of a binary tree, check if binary tree is a valid Binary Search Tree (BST). The root of a BST is greater than or 
         *              equal to ALL the nodes on left side. While on the right side, ALL the nodes are greater than the root.
         * 
         * Time Complexity: O(N) where N = # of nodes inside the tree. All of the nodes are visited, even if dfs() is called on left and right side 
         *                  separately. On top of that, isTreeBST() invovles iterating through both lists with a total time complexity of O(N). So,
         *                  O(N) from dfs() plus O(N) from isTreeBST() equals to a total time complexity of O(N).
         * 
         * Space Complexity: O(N) where N = # of nodes inside of the tree. All nodes, except for the root, are added to their appropriate lists. 
         */
         """
        
        # Create a list for left and right children
        leftChildren = list()
        rightChildren = list()

        # Traverse tree
        self.dfs(root.left, leftChildren)
        self.dfs(root.right, rightChildren)

        return self.isTreeBST(root, leftChildren, rightChildren)

def main():

    # Create a tree
    root = Node(8)

    root.left = Node(4)
    root.right = Node(10)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.right = Node(20)

    # Check if tree is a BST
    sol = CheckClass()
    ans = sol.checkBST(root)
    print(ans)

main()