// Cracking the Coding Interview - pp. 94 - q 2.2

class KElement {

    public static int solOne(Node headNode, int k) {

        /*
            OBJECTIVE: Find last kth element from linked list
            Time Complexity: O(n) where n = length of linked list. Linked list is only being traversed once.
            Space Complexity: O(1) because only 2 new nodes were created and its space is constant.
        */

        // If headNode is empty, exit function
        if (headNode == null) {
            return -1;
        }

        // If headNode is by itself, return it
        if (headNode.next == null) {return headNode.val;}

        // Create 2 pointers
        Node firstPtr = headNode;
        Node secondPtr = headNode;

        // Traverse linked list
        int pos = 0;
        while (firstPtr != null) {

            // If pos is greater than k, move secondPtr
            if (pos > k - 1) {
                secondPtr = secondPtr.next;
            }

            // Move firstPtr and update pos
            firstPtr = firstPtr.next;
            pos++;
        }

        // Return secondPtr's value
        // return secondPtr.val;

        /*
            NOTE: A little more advanced. 
            If K can be greater than linked list's length, then a few changes will need to be made. (1) Edge case of
                linked list only have one element needs to be deleted. What happens if k = 10 and linked list only has
                1 node. (2) Uncomment the below if-condition to compare secondPtr against headNode. If both share the
                same memory address, then K is greater than linked list's length because secondPtr never moved from
                starting position.
        */
        if (secondPtr == headNode) {
            return -1;
        }
        else {
            return secondPtr.val;
        }
    }

    public static void main(String[] args) {

        // Initialize linked list
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.append(1);
        ll.append(10);
        ll.append(100);
        ll.append(1000);

        int ans = solOne(ll.getHead(), 2);
        System.out.println(ans);
    }
}