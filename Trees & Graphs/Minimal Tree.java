// Cracking the Coding Interview - pp. 109 - q 4.2

public class Minimal {
    
    TreeNode createMinimalBST(int[] elems, int startPtr, int endPtr) {

        /*
         * OBJECTIVE: Continuosly add a new node to the tree from the array
         * 
         * Time Complexity: O(N) where N = # of elements inside of the array. Each element inside of elems[] will have its own node that will be a part of 
         *                  the tree.
         * 
         * Space Complexity: O(n) where n = # of nodes inside the tree. Although nodes will take up constant space,
         *                  multiple nodes will be created based on the length of elems[]
         */

        // If start and end pointers overlap, exit function
        if (startPtr > endPtr) {return null;}

        // Create a new node
        int midPtr = (startPtr + endPtr) / 2;
        TreeNode newNode = new TreeNode(elems[midPtr]);

        // Create newNode's children
        newNode.left = createMinimalBST(elems, startPtr, midPtr - 1);
        newNode.right = createMinimalBST(elems, midPtr + 1, endPtr);

        return newNode;
    }

    TreeNode createMinimalBST(int[] elems) {
        return createMinimalBST(elems, 0, elems.length - 1);
    }
}
