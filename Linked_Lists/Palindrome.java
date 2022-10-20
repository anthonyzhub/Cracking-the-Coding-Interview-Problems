// Cracking the Coding Interview - pp. 94 - q 2.6 

import java.util.*;

class Palindrome {
    
    public static boolean solOne(Node headNode) {

        /*
            OBJECTIVE: Check if a linked list is a palindrome

            Time Complexity: O(n) where n = length of linked list because linked list will be traversed twice, even though it's only reaching the halfway point.
                            Also, the return statement involves reversing a list and that list has n elements.

            Space Complexity: O(n) where n = length of linked list. In the 2nd while-loop, the left-half and right-half elements are added to their appropriate list.
        */

        // If headNode is null or by itself, return true
        if (headNode == null || headNode.next == null) {return true;}

        // Create tortoise and hare pointer nodes
        Node tortoise = headNode;
        Node hare = headNode;

        // Traverse linked list
        while (hare != null && hare.next != null) {

            // Move tortoise 1 node at a time and hare 2 nodes at a time
            tortoise = tortoise.next;
            hare = hare.next.next;
        }

        // Move hare back to the front of the linked list since it went out-of-bounds
        hare = headNode;

        // Traverse linked list
        ArrayList<Integer> tortoiseList = new ArrayList<Integer>();
        Stack<Integer> hareList = new Stack<Integer>();
        while (tortoise != null) {

            // Add node's value to appropriate array
            tortoiseList.add(tortoise.val);
            hareList.push(hare.val);

            // Move to next node
            tortoise = tortoise.next;
            hare = hare.next;
        }

        for (int i=0; i<tortoiseList.size(); i++) {
            if (tortoiseList.get(i) != hareList.pop()) {return false;}
        }

        return true;
    }

    public static void main(String[] args) {

        // Initialize linked list
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.append(2);
        ll.append(1);
        ll.append(1);
        ll.append(3);

        System.out.println(solOne(ll.getHead()));
    }
}
