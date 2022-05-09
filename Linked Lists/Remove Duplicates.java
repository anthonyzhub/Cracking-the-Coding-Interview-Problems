// Cracking the Coding Interview - pp. 94 - q 2.1

import java.util.ArrayList;
import java.util.Collections;

class Duplicates {

    public static void solOne(Node headNode) {

        /*
            OBJECTIVE: Sort unsorted linked list
            Time complexity: O(n log n) where n = length of linked list.
            Space complexity: O(n) where n = length of buffer[] list in sortLinkedList().
        */
        
        // If headNode is null or by itself, exit function
        if (headNode == null || headNode.next == null) {return;}

        // Create an array list
        ArrayList<Integer> buffer = new ArrayList<Integer>();

        // Traverse linked list and save elements to list
        Node curNode = headNode;
        while (curNode.next != null) {
            buffer.add(curNode.val);
            curNode = curNode.next;
        }

        // Sort ArrayList
        Collections.sort(buffer);

        // Traverse linked list again and update node's values
        curNode = headNode;
        for (int elem: buffer) {
            curNode.val = elem;
            curNode = curNode.next;
        }

        // Traverse linked list again and delete nodes with duplicate values
        curNode = headNode.next;
        while (curNode.next != null) {
            
            // Get previous node
            Node prevNode = curNode.prev;

            // If prevNode and curNode shares the same value, delete curNode
            if (prevNode.val == curNode.val) {
                
                // Connect neighboring nodes
                prevNode.next = curNode.next;
                curNode.next.prev = prevNode;
            }

            curNode = curNode.next;
        }
    }

    public static void main(String[] args) {

        // Create a linked list
        LinkedList ll = new LinkedList();
        ll.append(0);
        ll.append(0);
        ll.append(21);
        ll.append(12);
        ll.append(0);
        ll.append(0);
        ll.append(0);

        solOne(ll.getHead());
        ll.printList();
    }
}