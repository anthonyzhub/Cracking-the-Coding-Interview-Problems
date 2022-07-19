// Cracking the Coding Interview - pp. 111 - q 4.10

import java.util.*;

class CheckSubtree {

    boolean matchTree(TreeNode t1, TreeNode t2) {

        // OBJECTIVE: Compre t1 and t2 trees node by node

        // If both roots are empty, return true
        if (t1 == null && t2 == null) {
            return true;
        }

        // If only 1 root is empty, return false since a discrepancy was found
        else if (t1 == null || t2 == null) {
            return false;
        }
        
        // If both roots don't share the same value, then return false
        else if (t1.val != t2.val) {
            return false;
        }

        // If function is still continuing, check both of their children to see if the tree still matches
        else {
            return matchTree(t1.left, t2.left) && matchTree(t1.right, t2.right);
        }
    }

    boolean subtree(TreeNode t1, TreeNode t2) {

        // OBJECTIVE: Traverse tree until both root nodes share the same value. That'll be the starting point to see
        //              if t2 is a subtree of t1

        // If t1 is empty, return false because t2 can't be a subtree of an empty tree
        if (t1 == null) {
            return false;
        }

        // If both roots share teh same value and t2 was found inside of t1, then return true
        else if (t1.val == t2.val && matchTree(t1, t2)) {
            return true;
        }
        
        // Make a recursive call on t1's children to see if t2 can be found
        else {
            return subtree(t1.left, t2) || subtree(t1.right, t2);
        }
    }

    boolean containsTree(TreeNode t1, TreeNode t2) {

        // If t2 is empty, return tree because an empty tree is always a subtree
        if (t2 == null) {return true;}

        return subtree(t1, t2);
    }

    /*
     * ^ Book's solution ^
     * 
     * v My solution v
    */

    boolean inspect(TreeNode t1, TreeNode t2) {

        // OBJECTIVE: Compare t1, t2, and their children against each other. If they're a match, continue with the traversal. If not, return false

        // If both nodes are empty, return true
        if (t1 == null && t2 == null) {
            return true;
        }

        // If only node is empty, return false
        else if (t1 == null || t2 == null) {
            return false;
        }

        // If both roots don't share the same value, return false
        else if (t1.val != t2.val) {
            return false;
        }

        // If function is still continuing, compare their children
        return inspect(t1.left, t2.left) && inspect(t1.right, t2.right);
    }

    boolean bfs(TreeNode t1, TreeNode t2) {

        // OBJECTIVE: Perform a breadth-first search to find t2 inside of t1

        // Create a queue
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(t1);

        // Iterate queue
        while (!queue.isEmpty()) {

            // Pop 1st element from queue
            TreeNode poppedNode = queue.remove();

            // Check if popped node equals to t2
            if (poppedNode.val == t2.val) {

                // If true, then t2 was found inside of t1. Return true to end algorithm
                if (inspect(poppedNode, t2) == true) {return true;}
            }

            // Add its children to the queue
            if (poppedNode.left != null) {queue.add(poppedNode.left);}
            if (poppedNode.right != null) {queue.add(poppedNode.right);}
        }

        // Return false if t2 couldn't be found inside of t1
        return false;
    }

    boolean check(TreeNode t1, TreeNode t2) {

        /*
         * OBJECTIVE: Check if t2 is a subtree of t1 by using breadth-first search and recursive calls
         *
         * Time Complexity: O(K^d + cr*t2) where K = the maximum number of kids a node can have, d = how far deep bfs()
         *                   goes through, cr = # of common root found in t1 of t2's root, t2 = # of nodes in t2
         *
         *                   bfs() takes O(K^d) time because the function is looking for a node that shares the same
         *                   value as t2's root node. bfs() will continue until a matching node is found and if t2
         *                   does exist inside of t1.
         *
         *                   inspect() takes O(cr * t2) time because for every common root that is found in t1, inspect()
         *                   will be called and it will traverse the t2 tree. All t2 nodes will be traversed and compared
         *                   against the incoming nodes t1. If a discrepancy is found, inspect() will stop and won't
         *                   continue until another common root is found in bfs().
         *
         * Space Complexity: O(n * cr * t2) where n = # of nodes inside queue, cr = # of common roots found in t1 of t2's
         *                   root, and t2 = # of nodes inside of t2.
         * 
         *                   bfs() features a queue where it will hold t1's nodes. The queue size changes on every loop
         *                   because an element will be popped and its children will be added to the queue.
         *
         *                   inspect() takes O(cr * t2) time because for every common root that is found in t1, inspect()
         *                   will be called and it will traverse the t2 tree. All t2 nodes will be traversed and compared
         *                   against the incoming nodes t1. If a discrepancy is found, inspect() will stop and won't
         *                   continue until another common root is found in bfs().
        */

        // If hosting tree is empty, return false because t2 can't be a subtree of an empty tree
        if (t1 == null) {return false;}

        // Perform a breadth-first search and determine if t2 is a subtree of t1
        return bfs(t1, t2);
    }
}