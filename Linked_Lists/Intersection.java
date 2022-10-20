// Cracking the Coding Interview - pp. 94 - q 2.7

class Intersection {

    public static int linkedListSize(Node headNode) {

        // OBJECTIVE: Calculate linked list size

        // Iterate linked list
        int size = 0;
        while (headNode != null) {
            headNode = headNode.next;
            size++;
        }

        return size;
    }

    public static Node addPadding(Node headNode, int num) {
        
        // OBJECTIVE: Add nodes to the front of the linked list until num is 0

        // Create 2 nodes
        Node newHead = new Node(0);
        Node curNode = newHead;

        // Add nodes to the front
        while (num > 0) {

            // Create a new node
            newHead.next = new Node(0);
            newHead = newHead.next;

            // Decrement num
            num--;
        }

        // Connect newHead to headNode
        newHead.next = headNode;

        // Return new head node
        return curNode;
    }

    public static Node solOne(Node headA, Node headB) {

        /*
            OBJECTIVE: Find intersection point between both linked list. If one linked list is shorter than the other, add front padding to the shortest.

            Time Complexity: O(A + B + N) where A and B represents the size of each linked list. N = how long addPadding() will take to create new nodes
                            for the shortest linked list.
                            
                            Both lists are traversed at the beginning to determine its size, so that will take O(A + B) time where each variable represents
                            the length of their linked list.
                            
                            If one linked list is shorter than the other, new nodes will be added at the front of the shortest list. This will take O(N) where
                            N = the number of nodes that will be added for padding.

            Space Complexity: O(1) because neither new data structures that were created will change in size. A node object will always have the same size no matter what.

            IMPORTANT: I came up with this solution after reading one hint, so I will label this as a book solution
        */

        // If either linked list is empty, exit function
        if (headA == null || headB == null) {return null;}

        // Calculate size of both linked lists
        int sizeA = linkedListSize(headA);
        int sizeB = linkedListSize(headB);

        // Find out which linked list is the shortest in order to add padding
        Node nodeA = headA;
        Node nodeB = headB;
        if (sizeA > sizeB) {
            nodeB = addPadding(headB, sizeA - sizeB - 1);
        }
        else if (sizeB < sizeA) {
            nodeA = addPadding(headA, sizeB - sizeA - 1);
        }

        // Traverse both linked lists
        while (nodeA != null) {

            // If both nodes are the same, return intersection point
            if (nodeA == nodeB) {return nodeA;}

            // Move to next node
            nodeA = nodeA.next;
            nodeB = nodeB.next;
        }

        return null;
    }

    public static void main(String[] args) {

        // Create 2 linked lists
        Node headA = new Node(1);
        headA.next = new Node(2);
        headA.next.next = new Node(3);
        headA.next.next.next = new Node(4);
        headA.next.next.next.next = new Node(5);

        Node headB = new Node(1);
        headB.next = headA.next.next.next;
        headB.next = new Node(2);

        Node ans = solOne(headA, headB);
        if (ans == null) {
            System.out.println("No intersection detected");
        }
        else {
            System.out.println("Intersection at " + ans);
        }
    }
}