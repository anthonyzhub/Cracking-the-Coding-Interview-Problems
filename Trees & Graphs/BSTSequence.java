import java.util.*;

public class BSTSequence {
    
    void inorder(TreeNode root, ArrayList<String> path) {

        // OBJECTIVE: Print tree in inorder traversal

        // If root is empty, exit function
        if (root == null) {return;}

        // Visit left child, root, then right child
        inorder(root.left, path);
        path.add(root.val);
        inorder(root.right, path);
    }

    void postorder(TreeNode root, ArrayList<String> path) {

        // OBJECTIVE: Print tree in postorder traversal

        // If root is empty, exit function
        if (root == null) {return;}

        // Visit root, left child, then right child
        path.add(root.val);
        postorder(root.left, path);
        postorder(root.right, path);
    }

    void preorder(TreeNode root, ArrayList<String> path) {

        // OBJECTIVE: Print tree in preorder traversal
        
        // if root is empty, exit function
        if (root == null) {return;}

        // Visit left child, right child, then root
        preorder(root.left, path);
        preorder(root.right, path);
        path.add(root.val);
    }

    void printList(ArrayList<String> path) {

        // OBJECTIVE: Print elements inside array list

        for (String elem: path) {
            System.out.printf("%s ", elem);
        }

        System.out.println();
    }

    void sequence(TreeNode root) {

        // OBJECTIVE: Print tree in all possible orders as an array

        // If root is empty, exit function
        if (root == null) {return;}

        // Create 3 new ArrayLists
        ArrayList<String> inorderArrayList = new ArrayList<String>();
        ArrayList<String> postorderArrayList = new ArrayList<String>();
        ArrayList<String> preorderArrayList = new ArrayList<String>();
        
        // Call all 3 traversal functions
        inorder(root, inorderArrayList);
        postorder(root, postorderArrayList);
        preorder(root, preorderArrayList);

        printList(inorderArrayList);
        printList(postorderArrayList);
        printList(preorderArrayList);
    }
}
