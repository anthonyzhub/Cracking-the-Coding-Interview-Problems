import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Construct a binary search tree.
        // IMPORTANT: Make sure that ALL nodes have a reference to their parent node except for root
        TreeNode a = new TreeNode("A");
        TreeNode b = new TreeNode("B");
        TreeNode c = new TreeNode("C");

        a.left = b;
        a.right = c;

        
        // Initialize class
        BSTSequence seq = new BSTSequence();
        seq.sequence(a);
    }
}
