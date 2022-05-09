
public class LinkedList {

    Node headNode = new Node(0);
    Node tailNode = new Node(0);
    int size = 0;

    void append(int newVal) {

        // Create a new node
        Node newNode = new Node(newVal);

        // If linked list is empty, add newNode after head
        if (size == 0) {

            // Connect headNode and tailNode to newNode. Vice versa
            headNode.next = newNode;
            tailNode.prev = newNode;

            newNode.prev = headNode;
            newNode.next = tailNode;
        }
        else {

            // Get node before tailNode
            Node prevNode = tailNode.prev;

            // Connect prevNode to newNode. Vice versa
            prevNode.next = newNode;
            newNode.prev = prevNode;

            // Connect tailNode to newNode. Vice versa
            newNode.next = tailNode;
            tailNode.prev = newNode;
        }

        size++;
    }

    void delete(Node oldNode) {

        // OBJECTIVE: Delete oldNode from linked list

        // If oldNode is null, exit function
        if (oldNode == null) {return;}

        // Get neighboring nodes
        Node leftNode = oldNode.prev;
        Node rightNode = oldNode.next;

        // Connect neighboring nodes to each other
        leftNode.next = rightNode;
        rightNode.prev = leftNode;

        // Delete oldNode
        oldNode = null;
    }

    Node getHead() {

        // OBJECTIVE: Return node after headNode
        
        // If there's no node after headNode, exit function
        if (headNode.next == null) {return null;}

        return headNode.next;
    }

    int getSize() {

        // OBJECTIVE: Return linked list size
        return size;
    }

    void printList() {

        // OBJECTIVE: Print linked list

        // If linked list is empty, exit function
        if (headNode.next == null) {
            System.out.println("Linked list is empty!");
            return;
        }

        // Get headNode
        Node curNode = headNode.next;

        // Traverse linked list
        while (curNode.next != null) {
            System.out.print(curNode.val + " ");
            curNode = curNode.next;
        }
    }
}