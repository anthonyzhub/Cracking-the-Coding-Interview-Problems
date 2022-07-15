import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Construct a binary search tree.
        // IMPORTANT: Make sure that ALL nodes have a reference to their parent node except for root
        TreeNode a = new TreeNode("1");
        TreeNode b = new TreeNode("2");
        TreeNode c = new TreeNode("3");

        // a.left = b;
        // a.right = c;
        b.left = a;
        b.right = c;

        // Initialize class
        BSTSequence seq = new BSTSequence();
        for (LinkedList<String> output: seq.allSequences(b)) {
            System.out.println(output);
        }
    }
}
