import java.util.*;

public class BSTree {

    // Declare class variables
    int size;
    TreeNode root;
    List<String> children;

    BSTree() {
        this.size = 0;
        this.root = new TreeNode();
        this.children = new LinkedList<String>();
    }

    void inorder(TreeNode root) {
            
        if (root != null) {
            inorder(root.left);
            System.out.printf("%s ", root.val);
            inorder(root.right);
        }
    }

    void inorder() {

        // OBJECTIVE: Print tree in in-order
        inorder(root);
    }

    void insert(String newVal) {

        // OBJECTIVE: Create a new node and insert it to tree with newVal

        // If tree is empty, set newNode as root
        if (size == 0) {
            root = new TreeNode(newVal);
        }
        else {

            // Copy root node
            TreeNode curNode = root;

            // Traverse to the bottom of the tree
            while (true) {

                // If newValue already exist inside the tree, exit function
                if (curNode.val.compareTo(newVal) == 0) {
                    return;
                }

                // If newValue is less than curNode's value and curNode has a left child, go to left child
                if (newVal.compareTo(curNode.val) < 0 && curNode.left != null) {
                    curNode = curNode.left;
                }

                // If newValue is less than curNode's value and curNode doesn't have a left child, insert new node
                else if (newVal.compareTo(curNode.val) < 0) {
                    curNode.left = new TreeNode(newVal);
                    curNode.left.parent = curNode;
                    break;
                }

                // If newVal is greater than curNode's value and curNode has a right child, go to right child
                else if (newVal.compareTo(curNode.val) > 0 && curNode.right != null) {
                    curNode = curNode.right;
                }

                // If newVal is greater than curNode's value and curNode doesn't have a right child, insert new node
                else if (newVal.compareTo(curNode.val) > 0) {
                    curNode.right = new TreeNode(newVal);
                    curNode.right.parent = curNode;
                    break;
                }
            }
            children.add(newVal);
            size++;
        }
    }

    TreeNode find(String element) {

        // OBJECTIVE: Return node holding "element" as value

        // If tree is empty, exit function
        if (size == 0) {return null;}

        // Create a queue
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        // Iterate queue
        while (!queue.isEmpty()) {

            // Pop 1st element from queue
            TreeNode popped = queue.remove();

            // If popped node contains "element", return it
            if (popped.val.compareTo(element) == 0) {return popped;}

            // Add popped node's children to queue
            if (popped.left != null) {queue.add(popped.left);}
            if (popped.right != null) {queue.add(popped.right);}
        }

        return null;
    }

    void delete(String element) {

        // OBJECTIVE: Delete node holding "element" as value

        // If tree is empty, exit function
        if (size == 0) {return;}

        // Get node holding element
        TreeNode desiredNode = find(element);

        // If find() returned null, exit function
        if (desiredNode == null) {return;}

        // Get parent node of desiredNode
        TreeNode parentNode = desiredNode.parent;

        // If desiredNode is a leaf node, delete connection from parent
        if (desiredNode.left == null && desiredNode.right == null) {
            
            // Find out if desiredNode is a left or right child
            if (desiredNode.left == desiredNode) {parentNode.left = null;}
            else if (desiredNode.right == desiredNode) {parentNode.right = null;} 
        }

        // If desiredNode does have children, replace desiredNode for a child
        else {

            // If there's a right child, set it as new parent
            // NOTE: BST properties state that the right child will always be greater than the left. Left Child <= Root < Right Child
            if (desiredNode.right != null) {

                // Set desiredNode's right child as a direct child of desiredNode.parent
                if (parentNode.left == desiredNode) {

                    // Set right child as a direct child of parent
                    parentNode.left = desiredNode.right;

                    // Set desiredNode's left child as the left child of desiredNode.right
                    desiredNode.right.left = desiredNode.left;
                }
                else if (parentNode.right == desiredNode) {

                    // Set right child as a direct child of parent
                    parentNode.right = desiredNode.right;

                    // Set desiredNode's left child as the left child of desiredNode.right
                    desiredNode.right.left = desiredNode.left;
                }
            }

            // If a right child doesn't exist, but a left child does, set it as new parent
            else {
                
                // Set desiredNode's left child as a direct child of desiredNode.parent
                if (parentNode.left == desiredNode) {

                    // Set left child as a direct child of parent
                    parentNode.left = desiredNode.left;
                }
                else if (parentNode.right == desiredNode) {

                    // Set left child as a direct child of parent
                    parentNode.right = desiredNode.left;
                }
            }

            // Delete desired node and update tree's size and children list
            desiredNode = null;
            children.remove(element);
            size--;
        }
    }

    TreeNode getRandomNode() {

        // If tree is empty, exit function
        if (size == 0) {return null;}

        // Generate a random index and get element at index
        Random rand = new Random();
        int randIdx = rand.nextInt(size);

        // Return node containing element at "randIdx"
        return find(children.get(randIdx));
    }
}