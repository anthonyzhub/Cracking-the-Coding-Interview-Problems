// Cracking the Coding Interview - pp. 110 - q 4.6

public class Successor {
    
    TreeNode leftMostChild(TreeNode root) {

        // OBJECTIVE: Traverse to the bottom-left of the tree as much as possible

        // If root is empty, exit function
        if (root == null) {return null;}

        // Move to the bottom left of the tree starting from given node
        while (root.left != null) {
            root = root.left;
        }

        // Return left-most child
        return root;
    }

    TreeNode inorderSucc(TreeNode root) {

        /*
         * OBJECTIVE: Return the next node in in-order traversal
         * 
         * Time Complexity: O(n) where n = # of nodes needed to pass in order to reach the next left child. In
         *                  leftMostChild(), the tree is traversed starting from the given node until a the bottom-left
         *                  of the given (sub)tree is reached. 
         * 
         *                  In the while-loop inside inorderSucc(), the tree is traversed upwards until a left child node
         *                  is reached, or there's no more tree left to traverse
         * 
         * Space Complexity: O(1) because 1 or at-most 2 nodes will be created and they'll always take the same
         *                  constant space.
         */

        // If root is empty, exit function
        if (root == null) {return null;}

        // If there's a right child, find go to the left-most child node
        if (root.right != null) {return leftMostChild(root.right);}
        else {

            // Copy current node and get its parent
            TreeNode curRoot = root;
            TreeNode rootParent = curRoot.parent;

            // Go up the tree until we're on the left side, instead in the right
            while (rootParent != null && rootParent.left != curRoot) {

                // Move up the tree
                curRoot = rootParent;
                rootParent = rootParent.parent;
            }

            // Return parent node
            return rootParent;
        }
    }
}
