public class TreeNode {
    
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
        left = new TreeNode();
        right = new TreeNode();
    }
}
