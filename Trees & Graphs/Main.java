public class Main {
    public static void main(String[] args) {

        // Create a tree
        TreeNode root = new TreeNode(8);

        root.left = new TreeNode(4);
        root.right = new TreeNode(10);

        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(0);

        root.right.right = new TreeNode(20);

        // Check if tree is a BST
        CheckBST sol = new CheckBST();
        boolean ans = sol.checkBST(root);
        System.out.println(ans);
    }
}
