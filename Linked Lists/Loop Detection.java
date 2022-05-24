// Cracking the Coding Interview - pp. 95 - q 2.8
class Ans {

    /*
        OBJECTIVE: Create a class to hold multiple outputs from Solution.solOne()

        NOTE: Java doesn't allow function to return more than 1 value. So, I created a small class
            that will hold a node and a boolean variable representing whether or not a cycle exist.
    */

    Node node = null;
    boolean bool = false;

    Ans(Node node, boolean bool) {
        this.node = node;
        this.bool = bool;
    }
}

class Loop {

    public static Ans solOne(Node headNode) {

        /*
            OBJECTIVE: Check if there's a cycle inside the linked list using the tortoise and hare method
        
            NOTE: The tortoise and hare method uses 2 node pointers to traverse the linked list. The hare
                will move faster than the tortoise. Both will intersect each other inside the circular part of the linked list.
                From there, the hare will move back to the beginning of the linked list and move as the same rate as the tortoise.
                Both pointers will intersect again at the beginning of the cycle.

            Time Complexity: O(n) where n = length of linked list. The linked list is being traversed at most 2 times. The 1st
                            is to verify that the linked list has a cycle. The 2nd time is to find out where the cycle begins

            Space Complexity: O(1) because no dynamic data structures were created. Only 2 nodes were created and both occupy
                            constant space.
        */

        // If headNode is empty, then exit function
        if (headNode == null) {
            return new Ans(headNode, false);
        }

        // Create 2 node pointers
        Node hare = headNode;
        Node tortoise = headNode;

        // Iterate linked list
        boolean firstRun = true;
        while (hare != null && hare.next != null) {

            // Check if both node pointers overlap
            if (hare == tortoise) {

                // If this is the first loop, then continue
                if (firstRun == true) {
                    firstRun = false;
                }

                // If not, then exit loop
                else {
                    break;
                }
            }

            // Move both nodes
            hare = hare.next.next;
            tortoise = tortoise.next;
        }

        // If hare is at the tail or went pass it, then a cycle doesn't exist inside the linked list
        if (hare == null || hare.next == null) {
            return new Ans(headNode, false);
        }

        // Send hare back to the beginning
        hare = headNode;

        // Traverse list again with hare moving 1 node at a time. Hare and tortoise will overlap again at the beginning of the cycle
        while (hare != tortoise) {
            hare = hare.next;
            tortoise = tortoise.next;
        }

        return new Ans(hare, true);
    }

    public static void main(String[] args) {

        // Create a linked list
        Node nodeA = new Node(1);
        Node nodeB = new Node(2);
        Node nodeC = new Node(3);
        Node nodeD = new Node(4);

        nodeA.next = nodeB;
        nodeB.next = nodeC;
        nodeC.next = nodeD;
        // nodeD.next = null;
        nodeD.next = nodeB;

        Ans ans = solOne(nodeA);

        if (ans.bool == false) {
            System.out.println("Cycle undetected");
        }
        else {
            System.out.println("Cycle detected at " + ans.node.val);
        }
    }
}