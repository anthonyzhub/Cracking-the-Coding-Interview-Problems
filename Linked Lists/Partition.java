// Cracking the Coding Interview - pp. 95 - q 2.4

import java.util.*;

class Partition {

    public static Node boolSol(Node node, int pivot) {

        /*

        OBJECTIVE: Partition linked list with any elements smaller than or equal to pivot appearing first,
                        then add remaining elements to the end of the list.

        NOTE: We're assuming that keeping the linked list in its original order doesn't matter.
        
        Time Complexity: O(n) where n = length of linked list. The linked list is being traversed twice.

        Space Complexity: O(1) because no dynamic data structures were created. The 2 nodes that were created
                        will always take up the same amount of space.

        */

        // Create 2 new nodes
        Node head = node;
        Node tail = node;

        // Traverse linked list
        while (node != null) {

            // Copy node's next pointer value
            Node next = node.next;

            // Compare node.val against pivot
            if (node.val < pivot) {

                // Insert curNode before newHead, then update newHead
                node.next = head;
                head = node;
            }
            else {

                // Insert newTail before curNode, then update newTail
                tail.next = node;
                tail = node;
            }

            // Move to next node
            node = next;
        }

        // Set tail node's next pointer to null
        tail.next = null;

        // Return newHead since original head has changed
        return head;
    }
    
    public static Node solOne(Node headNode, int pivot) {

        /*
            OBJECTIVE: Partition linked list with any elements smaller than or equal to pivot appearing first,
                        then add remaining elements to the end of the list.

            NOTE: We're assuming that keeping the linked list in its original order doesn't matter.
            
            Time Complexity: O(n) where n = length of linked list. The linked list is being traversed twice.

            Space Complexity: O(n) where n = the number of elements inside of the linked list. 2 new arrays
                            are created to hold the smallest and largest elements inside of the linked list
                            compared to the pivot.
        */

        // If headNode is empty or by itself, return it
        if (headNode == null || headNode.next == null) {return headNode;}

        // Create 2 new arrays
        ArrayList<Integer> smallest = new ArrayList<Integer>();
        ArrayList<Integer> largest = new ArrayList<Integer>();

        // Traverse linked list
        Node curNode = headNode;
        while (curNode != null) {

            // Add curNode.val to appropriate list
            if (curNode.val < pivot) {
                smallest.add(curNode.val);
            }
            else {
                largest.add(curNode.val);
            }

            // Move to next node
            curNode = curNode.next;
        }

        // Traverse linked list again and add smaller elements first
        curNode = headNode;
        while (curNode != null) {

            // Continue to add smaller elements first until array is empty
            if (smallest.size() > 0) {
                curNode.val = smallest.remove(0);
            }
            else {
                curNode.val = largest.remove(0);
            }

            // Move to next node
            curNode = curNode.next;
        }
        return headNode;
    }

    public static void main(String[] args) {

        // Create a linked list
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.append(3);
        ll.append(5);
        ll.append(8);
        ll.append(5);
        ll.append(10);

        // Partition array
        // solOne(ll.getHead(), 5);
        boolSol(ll.getHead(), 5);
        ll.printList();
    }
}
