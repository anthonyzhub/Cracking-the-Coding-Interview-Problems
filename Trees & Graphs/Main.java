import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Create a tree
        TreeNode a = new TreeNode("A");
        TreeNode b = new TreeNode("B");
        TreeNode c = new TreeNode("C");
        TreeNode d = new TreeNode("D");
        TreeNode e = new TreeNode("E");
        TreeNode f = new TreeNode("F");
        TreeNode g = new TreeNode("G");
        TreeNode h = new TreeNode("H");
        TreeNode i = new TreeNode("I");
        TreeNode j = new TreeNode("J");

        a.left = b;
        a.right = c;

        b.left = d;
        b.right = e;

        d.left = f;
        d.right = h;

        c.left = g;
        c.right = i;

        g.left = j;

        // Initialize class
        CheckSubtree sol = new CheckSubtree();
        System.out.println(sol.containsTree(a, j));
    }
}
