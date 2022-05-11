// Cracking the Coding Interview - pp. 94 - q 2.3

public class DeleteMiddleNode {
    
    public static void solOne(Node midNode) {

        /*
            OBJECTIVE: Given a middle node, delete it while still keeping the linked list connected as one.
            Time Complexity: O(n/2) where n = length of linked list. The function is given the middle node of
                            a linked list. I only need to traverse the right-half of the linked list, instead
                            of the entire list.
            Space Complexity: O(1) because all 3 pointers take constant space. No large data structures were
                            created.
        */

        // Create 3 pointers
        Node prevNode = midNode;
        Node curNode = midNode;
        Node nextNode = curNode.next;

        // Swap values between curNode and nextNode
        boolean movePrevNode = false;
        while (nextNode != null) {

            // Swap values
            int tmpVal = curNode.val;
            curNode.val = nextNode.val;
            nextNode.val = tmpVal;

            // Move nodes
            curNode = curNode.next;
            nextNode = nextNode.next;

            // After one loop, move prevNode
            if (movePrevNode == false) {
                movePrevNode = true;
            }
            else {
                prevNode = prevNode.next;
            }
        }

        // Disconnect prevNode from curNode
        prevNode.next = null;

        // Delete curNode and nextNode
        curNode = null;
        nextNode = null;
    }

    public static void main(String[] args) {

        // Initialize linked list class
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.append(1);
        ll.append(2);
        ll.append(3);
        ll.append(4);
        ll.append(5);
        ll.append(6);
        ll.printList();
        System.out.println();

        // Call function
        solOne(ll.getMiddle());
        ll.printList();
    }
}
