public class Main {
    public static void main(String[] args) {

        // Initialize class
        Minimal minTree = new Minimal();
        int[] elems = {10, 23, 30, 41, 46, 47, 62, 63, 68, 82};
        minTree.createMinimalBST(elems);
    }
}
