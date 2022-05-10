// Cracking the Coding Interview - pp. 94 - q 2.1

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

class Duplicates {

    public static void hashSet(Node curNode) {

        /*
            OBJECTIVE: Answer solution with a hash set
            Time Complexity: O(n) where n = length of linked list
            Space Complexity: O(n) where n = length of hash set
        */

        // Create a hash set
        HashSet<Integer> set = new HashSet<Integer>();

        // Traverse linked list
        Node prevNode = curNode;
        while (curNode.next != null) {

            // If value already exist, have prevNode skip curNode for curNode.next
            if (set.contains(curNode.val)) {
                prevNode.next = curNode.next;
            }
            else {

                // If curNode's value is not in set, add it to set and update prevNode
                set.add(curNode.val);
                prevNode = curNode;
            }

            // Move to next node
            curNode = curNode.next;
        }
    }

    public static void tortoiseAndHare(Node headNode) {

        /*
            OBJECTIVE: Remove duplicate nodes from linked list
            Time Complexity: O(n^2) where n = length of linked list. This algorithm involves create 2 pointers (tortoise and hare). For each node, the linked
                                list is traversed from tortoise node to the end.
            Space Complexity: O(1) because no large datasets were created. Only 2 new nodes were created, but they are constant.
        */

        // Create a tortoise node (slow node)
        Node tortoise = headNode;

        // Move tortoise
        while (tortoise.next != null) {

            // Create a hare node
            Node hare = tortoise;

            // Move hare and remove nodes with same value
            while (hare.next.next != null) {

                // If both nodes share the same value, move (hop) 2 nodes to the right
                if (hare.next.val == tortoise.val) {
                    hare.next = hare.next.next;
                } 
                else {
                    // If not, move to next node
                    hare = hare.next;
                }
            }

            tortoise = tortoise.next;
        }
    }

    public static void solOne(Node headNode) {

        /*
            OBJECTIVE: Sort unsorted linked list
            Time Complexity: O(n log n) where n = length of linked list.
            Space Complexity: O(n) where n = length of buffer[] list in sortLinkedList().
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

        // solOne(ll.getHead());
        // hashSet(ll.getHead());
        tortoiseAndHare(ll.getHead());
        ll.printList();
    }
}