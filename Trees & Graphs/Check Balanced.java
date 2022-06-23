// Cracking the Coding Interview - pp. 110 - q 4.4

public class CheckBalanced {

    int getHeight(TreeNode root, int level) {

        // OBJECTIVE: Calculate and return maximum height between subtrees

        // If root is null, return level
        if (root == null) {return level;}

        // Calculate height of left and right subtree
        int leftSubTree = getHeight(root.left, level + 1);
        int rightSubTree = getHeight(root.right, level + 1);

        return Math.max(leftSubTree, rightSubTree);
    }
    
    boolean check(TreeNode root) {

        /*
         * OBJECTIVE: Determine if given binary tree is balanced. A balanced tree has 2 subtrees with heights that don't differ by more than 1 level.
         * 
         * Time Complexity: O(V + E) where V = # of vertices (nodes) and E = # of edges (lines between nodes). check() traverses the left and right
         *                  subtree with getHeight(). getHeight() visits every nodes, increments level, and returns maximum height between subtrees.
         * 
         * Space Complexity: O(V) where V = # of vertices (nodes) inside of the tree because a recursive call is made per vertex. After visiting a vertex,
         *                  a recursive call is made to visit the vertex's children. Each call is saved on the memory stack.
         */

        // If root is null, return true
        if (root == null) {return true;}

        // Calculate height of left and right subtree
        int leftSubTree = getHeight(root.left, 1);
        int rightSubTree = getHeight(root.right, 1);

        // Calculate height difference
        int diff = Math.abs(leftSubTree - rightSubTree);

        // If height difference is at most 1, return true. If not, return false
        if (diff <= 1) {return true;}
        return false;
    }
}
