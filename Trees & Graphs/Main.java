public class Main {
    public static void main(String[] args) {

        // Create a tree
        TreeNode root = new TreeNode(10);

        root.left = new TreeNode(9);
        root.right = new TreeNode(90);

        root.left.left = new TreeNode(4);

        // Initialize solution class
        CheckBalanced balanced = new CheckBalanced();
        boolean ans = balanced.check(root);
        System.out.println(ans);
    }
}
