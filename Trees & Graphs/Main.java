import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Construct a binary search tree.
        // IMPORTANT: Make sure that ALL nodes have a reference to their parent node except for root
        TreeNode a = new TreeNode("A");
        TreeNode b = new TreeNode("B");
        TreeNode c = new TreeNode("C");
        TreeNode d = new TreeNode("D");
        TreeNode e = new TreeNode("E");
        TreeNode f = new TreeNode("F");
        TreeNode g = new TreeNode("G");
        TreeNode h = new TreeNode("H");

        a.parent = null;
        a.left = b;
        a.right = c;

        b.parent = a;
        b.left = d;
        b.right = e;

        d.parent = b;
        e.parent = b;

        c.parent = a;
        c.left = f;
        c.right = h;

        f.parent = c;
        f.left = g;

        h.parent = c;

        g.parent = f;

        // Initialize class
        CommonAncestor ancestorClass = new CommonAncestor();
        TreeNode ans = ancestorClass.commonAncestorWithLinkToParent(h, g);

        if (ans != null) {
            System.out.println(ans.val);
        }
        else {
            System.out.println(false);
        }
    }
}
