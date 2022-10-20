// Cracking the Coding Interview - pp. 110 - q 4.8

class ResultNode {

    // Create a node and boolean variable
    public TreeNode answerNode;
    public boolean isAncestor;

    ResultNode(TreeNode answerNode, boolean isAncestor) {
        this.answerNode = answerNode;
        this.isAncestor = isAncestor;
    }
}

public class CommonAncestor {

    int depth(TreeNode root) {

        // OBJECTIVE: Return depth of root node

        // Create a depth counter
        int depth = 0;

        // Move up the tree with "parent" pointer
        while (root != null) {

            // Update node and counter
            root = root.parent;
            depth++;
        }

        return depth;
    }

    TreeNode goUp(TreeNode root, int depthDiff) {

        // OBJECTIVE: Move root node up until depthDiff is 0

        while (depthDiff > 0 && root != null) {
            root = root.parent;
            depthDiff--;
        }

        return root;
    }

    TreeNode commonAncestorWithLinkToParent(TreeNode p, TreeNode q) {

        /*
         * OBJECTIVE: Find common ancestor between node p and q with parent attribute
         * NOTE: Each node will have a pointer to its parent
         *
         * Time Complexity: O(d) where d = is the depth of deepNode. If the tree is 8 levels tall and deepNode is at 3, then the remaining 5 levels aren't
         *                   searched because shallowNode is higher than where deepNode is. The while-loop inside depth() only goes as far as deepNode's level.
         *
         *                   The loop inside goUp() executes "diff" times until shallowNode is at the same level as deepNode. From there, both nodes are moved
         *                   up the tree until they reach a common ancestor. The ancestor can be root or a child of root.
         *
         * Space Complexity: O(1) because no dynamic data structures were created and a recursive function isn't used.
        */

        // If either nodes are empty, exit function
        if (p == null || q == null) {return null;}

        // Calculate difference in depth
        int depthDiff = Math.abs(depth(p) - depth(q));

        // Classify shallow and deep node
        TreeNode deepNode = depthDiff > 0 ? q : p;
        TreeNode shallowNode = depthDiff > 0 ? p : q;

        // Move deepNode up the tree until it reaches the same level as shallowNode
        deepNode = goUp(deepNode, depthDiff);

        // Move both nodes up the tree until an intersection occurs or one of them becomes a null
        while (deepNode != shallowNode && deepNode != null && shallowNode != null) {

            // Move both nodes up
            deepNode = deepNode.parent;
            shallowNode = shallowNode.parent;
        }

        // If either nodes are empty, exit function
        // This means that both nodes weren't a part of the same tree
        if (deepNode == null || shallowNode == null) {return null;}

        // Return either node since both are at ancestor node
        return deepNode;
    }
    
    ResultNode commonAncestorHelper(TreeNode root, TreeNode p, TreeNode q) {

        // OBJECTIVE: Continue to make recursive calls on a common ancestor has been found or p/q node becomes null

        // If root is empty, exit function
        if (root == null) {return null;}

        // If both nodes equal to root, return root because it's the common ancestor
        if (p == q) {return new ResultNode(root, true);}

        // Check if ancestor exists on the left subtree
        ResultNode leftSubtree = commonAncestorHelper(root.left, p, q);
        if (leftSubtree.isAncestor) {return leftSubtree;}

        // Check if ancestor exists on the right subtree
        ResultNode rightSubtree = commonAncestorHelper(root.right, p, q);
        if (rightSubtree.isAncestor) {return rightSubtree;}

        // If p and q exist on separate subtrees from current root, return root as common ancestor
        if (leftSubtree.answerNode != null && rightSubtree.answerNode != null) {
            return new ResultNode(root, true);
        }

        // If either subtree's root equals to root, return that subtree's root
        // I.e., If we're at p or q and one of those nodes is a subtree, then this root node is the common ancestor
        else if (root == p || root == q) {

            // Create a boolean variable
            boolean isAncestor = (leftSubtree.answerNode != null || rightSubtree.answerNode != null);
            return new ResultNode(root, isAncestor);
        }

        // If either subtree nodes are empty, return the non-empty node as common ancestor
        else {

            // Capture the non-empty subtree node
            TreeNode answerNode = leftSubtree.answerNode != null ? leftSubtree.answerNode : rightSubtree.answerNode;
            return new ResultNode(answerNode, false);
        }
    }

    TreeNode commonAncestorWithoutLinkToParent(TreeNode root, TreeNode p, TreeNode q) {

        /*
         * OBJECTIVE: Find common ancestor between p and q nodes given the tree's root node
         * 
         * Time Complexity: O(n) where n = # of nodes that were visited in the traversal from commonAncestorHelper(). That function will check the root,
         *                  continue to go down the left subtree, then go through the right subtree. It won't stop until a common ancestor is found or
         *                  if one node reaches null.
         * 
         * Space Complexity: O(n) where n = # of recursive call made. A recursive call is made per node. The node's subtrees are traversed and it won't
         *                  stop until a common ancestor is found or if one node reachs null.
         */

        // If either nodes are empty, exit function
        if (p == null || q == null) {return null;}

        // Get common ancestor of both nodes
        ResultNode resultNode = commonAncestorHelper(root, p, q);

        // If resultNode contains the ancestor of p and q, return it. If not, return null
        if (resultNode.isAncestor == false) {return resultNode.answerNode;}

        return null;
    }
}