// Cracking the Coding Interview - pp. 110 - q 4.9
import java.util.*;

public class BSTSequence {

    void weaveLists(LinkedList<String> first, LinkedList<String> second, ArrayList<LinkedList<String>> results,
            LinkedList<String> prefix) {

        // OBJECTIVE: Merge elements from first and second list to an array list of linked list.
        
        // If either linked lists are empty, merge the non-empty list to results
        if (first.isEmpty() || second.isEmpty()) {

            // Clone prefix
            LinkedList<String> prefixCopy = (LinkedList<String>) prefix.clone();

            // Add elements from first and second linked list to results
            prefixCopy.addAll(first);
            prefixCopy.addAll(second);

            // Add cloned linked list to the end of results
            results.add(prefixCopy);

            return;
        }

        // Pop head from first linked list
        String popped = first.remove();
        prefix.add(popped);

        // Continue to weave first and second list
        weaveLists(first, second, results, prefix);

        // Add popped element back to first linked list
        prefix.removeLast();
        first.addFirst(popped); // <= It was popped from the front and re-added to the front

        // Repeat same steps above for second linked list
        popped = second.remove();
        prefix.add(popped);
        weaveLists(first, second, results, prefix);
        prefix.removeLast();
        second.addFirst(popped);
    }

    ArrayList<LinkedList<String>> allSequences(TreeNode node) {

        /*
         * OBJECTIVE: Return a list of all possible combinations of how input tree could have been constructed
         * 
         * Time Complexity: O(n + L*R*(L + R)) where n = # of nodes inside the tree, L = # of nodes on the left subtrees,
         *                  R = # of nodes on the right subtrees. O(n) is for pre-order traversal that is done in allSequences().
         *                  O(L * R) is from the double nested for-loops inside allSequences(). Within the for-loops, weaveLists()
         *                  is called which performs a recursive call.
         * 
         *                  The recursive calls is to continue weaving the remaining elements from the first and second list.
         *                  If there's only 1 non-empty list, it will be iterated in order to add all the remaining elements
         *                  from that list to results.
         * 
         *                  For the record, I labelled L and R left and right subtrees, respecitvely, because there might be
         *                  more nodes on the left than on the right, or vice versa. It depends on the tree.
         * 
         * Space Complexity: O(Re + (L+R)) where Re = length of result, L = length of leftSequence and R = length of rightSequence.
         *                  The output list, result, will be the largest data structure in this algorithm because it contains the list of
         *                  all possible combinations on how the given tree was constructed.
         * 
         *                  (L+R) comes from weaveList(). At the bottom of weaveList(), a recursive call is made per node in each list.
         *                  This will continue until either list becomes empty because the if-condition will add the remaining nodes from
         *                  the non-empty list to result. Then, the function will stop and revert the already-made recursive calls.
        */
        
        // Create an array list of linked lists
        ArrayList<LinkedList<String>> result = new ArrayList<LinkedList<String>>();

        // If node is empty, exit function
        if (node == null) {

            // Add a blank linked list to the array list
            result.add(new LinkedList<String>());

            return result;
        }

        // Create a linked list
        LinkedList<String> prefix = new LinkedList<String>();
        prefix.add(node.val);

        // Recurse on left and right subtrees
        ArrayList<LinkedList<String>> leftSequence = allSequences(node.left);
        ArrayList<LinkedList<String>> rightSequence = allSequences(node.right);

        // Weave (merge) each list from the left and right side
        for (LinkedList<String> leftElem : leftSequence) {
            for (LinkedList<String> rightElem : rightSequence) {

                // Create a new linked list to hold left and right elements
                ArrayList<LinkedList<String>> weaved = new ArrayList<LinkedList<String>>();

                // Go through left and right sequences
                weaveLists(leftElem, rightElem, weaved, prefix);

                // Add all possible combinations to result list
                result.addAll(weaved);
            }
        }

        return result;
    }
}
