class SumList {

    public static Node bookSol(Node headA, Node headB, int carryOver) {

        // If both linked lists are empty and there's no carry over value, exit function
        if (headA == null && headB == null && carryOver == 0) {return null;}

        // Compute potential value of future new node(depending if total exceeds 9)
        int newVal = carryOver + headA.val + headB.val;
        
        // Create a new node
        Node newNode = new Node(newVal % 10);

        // Create the remaining right-side nodes
        Node rightNodes = bookSol(headA.next, headB.next, newVal >= 10 ? 1 : 0);
        newNode.next = rightNodes;

        // Return head node of new linked list
        return newNode;
    }

    public static void main(String[] args) {

        // Create 2 linked lists
        SinglyLinkedList listA = new SinglyLinkedList();
        SinglyLinkedList listB = new SinglyLinkedList();

        listA.append(7);
        listA.append(1);
        listA.append(6);

        listB.append(5);
        listB.append(9);
        listB.append(2);

        // Call solution function
        Node headNode = bookSol(listA.getHead(), listB.getHead(), 0);
        while (headNode != null) {
            System.out.print(headNode.val + " ");
            headNode = headNode.next;
        }
    }
}