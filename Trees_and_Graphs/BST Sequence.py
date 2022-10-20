# Cracking the Coding Interview - pp. 110 - q 4.9

from copy import deepcopy

class BSTSequence:

    def weaveList(self, first, second, results, prefix):

        # OBJECTIVE: Merge elements from first and second list to a large list

        # If either list is empty, merge the non-empty list to results
        if len(first) == 0 or len(second) == 0:

            # Create a copy of prefix
            prefixCopy = deepcopy(prefix)

            # Add all elements from first and second list to prefixCopy
            for fElem in first: prefixCopy.append(fElem)
            for sElem in second: prefixCopy.append(sElem)

            # Add cloned list to results
            results.append(prefixCopy)
            return

        # Pop head from first list
        popped = first.pop(0)
        prefix.append(popped)

        # Continue to weave first and second list
        self.weaveList(first, second, results, prefix)

        # Add popped element back to first list
        prefix.pop(-1)
        first.insert(0, popped)

        # Repeat same steps above for second list
        popped = second.pop(0)
        prefix.append(popped)
        self.weaveList(first, second, results, prefix)
        prefix.pop(-1)
        second.insert(0, popped)

    def allSequences(self, node):

        """
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
        """

        # Create a return list
        result = list()

        # If input node is empty, exit function
        if node is None:
            return [[]]
        
        # Create a list to hold current combination
        prefix = list()
        prefix.append(node.val)

        # Recurse left and right subtree
        leftSequence = self.allSequences(node.left)
        rightSequence = self.allSequences(node.right)

        # Weave (merge) each list from the left and right subtree
        for leftElem in leftSequence:
            for rightElem in rightSequence:

                # Create a new linked list to hold left and right elements
                weaved = list()

                # Go through left and right sequences
                self.weaveList(leftElem, rightElem, weaved, prefix)

                # Add all possible combinations to result list
                for combo in weaved:
                    result.append(combo)

        # Return list of all possible combinations
        return result
