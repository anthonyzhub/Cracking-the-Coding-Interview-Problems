import java.util.*;

public class Main {
    public static void main(String[] args) {

        BSTree bstree = new BSTree();
        bstree.insert("A");
        bstree.insert("B");
        bstree.insert("C");
        bstree.insert("D");
        bstree.insert("E");
        bstree.insert("F");
        bstree.insert("G");
        bstree.insert("H");
        bstree.insert("I");
        bstree.insert("J");

        // Print random node
        String elemToDelete = bstree.getRandomNode().val;
        System.out.println(elemToDelete);
        bstree.find("F");
        bstree.inorder();
        System.out.println();
        bstree.delete(elemToDelete);
        bstree.inorder();
    }
}
