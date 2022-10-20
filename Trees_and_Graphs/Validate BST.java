// Cracking the Coding Interview - pp. 110 - q 4.5

import java.util.LinkedList;

public class CheckBST {

    public void dfs(TreeNode root, LinkedList<TreeNode> children) {

        // If root is null, exit function
        if (root == null) {return;}

        // Add root to linked list
        children.add(root);

        // Visit children
        dfs(root.left, children);
        dfs(root.right, children);
    }

    public boolean isTreeBST(TreeNode root, LinkedList<TreeNode> leftChildren, LinkedList<TreeNode> rightChildren) {

        // OBJECTIVE: Check that all left children are less than or equal to root and all right children are greater than root

        // Traverse leftChildren linked list
        // IMPORTANT: All nodes on the left side MUST be less than or equal to root.val
        for (TreeNode curNode: leftChildren) {
            if (curNode.val > root.val) {return false;}
        }
        
        // Traverse rightChildren linked list
        // IMPORTANT: All nodes on the right side MUST be greater than root.val
        for (TreeNode curNode: rightChildren) {
            if (curNode.val <= root.val) {return false;}
        }

        return true;
    }
    
    public boolean checkBST(TreeNode root) {

        /*
         * OBJECTIVE: Given the root of a binary tree, check if binary tree is a valid Binary Search Tree (BST). The root of a BST is greater than or 
         *              equal to ALL the nodes on left side. While on the right side, ALL the nodes are greater than the root.
         * 
         * Time Complexity: O(N) where N = # of nodes inside the tree. All of the nodes are visited, even if dfs() is called on left and right side 
         *                  separately. On top of that, isTreeBST() invovles iterating through both lists with a total time complexity of O(N). So,
         *                  O(N) from dfs() plus O(N) from isTreeBST() equals to a total time complexity of O(N).
         * 
         * Space Complexity: O(N) where N = # of nodes inside of the tree. All nodes, except for the root, are added to their appropriate LinkedList. 
         */

        // Create 2 lists
        LinkedList<TreeNode> leftChildren = new LinkedList<TreeNode>();
        LinkedList<TreeNode> rightChildren = new LinkedList<TreeNode>();

        // Traverse tree
        dfs(root.left, leftChildren);
        dfs(root.right, rightChildren);

        // Compare root against linked lists' elements and check that BST condition is met
        return isTreeBST(root, leftChildren, rightChildren);
    }
}
