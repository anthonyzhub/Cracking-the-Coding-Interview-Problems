// Cracking the Coding Interview - pp. 109 - q 4.3

import java.util.*;

public class Depth {

    void printLists(ArrayList<ListNode> masterList) {

        // Iterate array list
        for (ListNode head: masterList) {

            // Iterate linked list
            while (head != null) {
                System.out.printf("%d ", head.val);
                head = head.next;
            }
            System.out.println();
        }
    }

    void bfs(TreeNode root) {

        /*
         * OBJECTIVE: Create a linked list per level in Binary Tree. For example, if tree's height is 3 levels tall, then 
         *              there should be 3 separate linked lists where the nodes are from the same level.
         * 
         * Time Complexity: O(V + E) where V = # of vertices (nodes) and E = # of edges. Every node is pretty much visited and their kids are added to the queue
         *                  for future processing.
         * 
         * Space Complexity: O(L * N) where L = # of levels exist and N = # of nodes inside the queue. masterList is a LinkedList that will only hold the
         *                  head nodes of each level inside the tree. E.g., If a tree has 3 levels, then masterList will hold 3 heads TreeNodes. 
         * 
         *                  Queue exist to manage a queue of children nodes to inspect. Each child will be processed and dropped from the queue, but
         *                  if there are grandchildren, then they'll be added to the queue.
         */

        // If root is null, exit function
        if (root == null) {return;}

        // Create an array list to hold head nodes of each level
        ArrayList<ListNode> masterList = new ArrayList<ListNode>();
        masterList.add(new ListNode(root.val));

        // Create a queue
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        // Iterate queue
        while (queue.size() > 0) {

            // Pop element from queue
            TreeNode poppedNode = queue.pop();

            // Create a new node
            ListNode head = new ListNode();

            // Add poppedNode's children to linked list
            if (poppedNode.left != null && poppedNode.right != null) {

                // Created linked list
                head.next = new ListNode(poppedNode.left.val);
                head.next.next = new ListNode(poppedNode.right.val);

                // Add children to queue
                queue.add(poppedNode.left);
                queue.add(poppedNode.right);
            }

            else if (poppedNode.left != null) {
                head.next = new ListNode(poppedNode.left.val);
                queue.add(poppedNode.left);
            }

            else if (poppedNode.right != null) {
                head.next = new ListNode(poppedNode.right.val);
                queue.add(poppedNode.right);
            }

            // If linked list isn't empty, add it to listOfHeads
            if (head.next != null) {
                masterList.add(head.next);
            }
        }
        printLists(masterList);
    }
}