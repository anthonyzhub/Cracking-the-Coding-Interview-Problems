
public class SinglyLinkedList {

    Node headNode = null;
    int size = 0;

    void append(int newVal) {

        // OBJECTIVE: Add a new node to the end of the list

        // Create a new node
        Node newNode = new Node(newVal);

        // If linked list is empty, add newNode as head
        if (headNode == null) {
            headNode = newNode;
        }
        else {

            // Traverse linked list
            Node curNode = headNode;
            while (curNode.next != null) {
                curNode = curNode.next;
            }

            // Connect last node to newNode
            curNode.next = newNode;
        }

        size++;
    }

    Node getHead() {

        // OBJECTIVE: Return node after headNode
        
        // If there's no node after headNode, exit function
        if (headNode == null) {return null;}

        return headNode;
    }

    Node getMiddle() {

        // OBJECTIVE: Return middle node from linked list

        // If linked list is empty, exit function
        if (headNode == null) {return null;}

        // Create a temporary node
        Node tmpNode = headNode;

        // Move to node until midpoint
        for (int i=0; i<size/2; i++) {
            tmpNode = tmpNode.next;
        }

        return tmpNode;
    }

    int getSize() {

        // OBJECTIVE: Return linked list size
        return size;
    }

    void printList() {

        // OBJECTIVE: Print linked list

        // If linked list is empty, exit function
        if (headNode == null) {
            System.out.println("Linked list is empty!");
            return;
        }

        // Get headNode
        Node curNode = headNode;

        // Traverse linked list
        while (curNode != null) {
            System.out.print(curNode.val + " ");
            curNode = curNode.next;
        }
    }
}