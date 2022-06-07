// Cracking the Coding Interview - pp. 98 - q 3.4

import java.util.*;

public class myqueue {
    
    // Create 2 stacks
    Stack<Integer> newestStack;
    Stack<Integer> oldestStack;

    myqueue() {

        // OBJECTIVE: Create a queue class that uses 2 stacks to keep track of elements.

        newestStack = new Stack<Integer>();
        oldestStack = new Stack<Integer>();
    }

    void add(int newVal) {

        /*
         * OBJECTIVE: Add new value to stack
         * 
         * Time Complexity: O(1) because element is added at the top of the stack
         * 
         * Space Complexity: O(1) because stack takes up an additional, constant space element
         */
        newestStack.push(newVal);
    }

    void shiftStack() {

        /*
         * OBJECTIVE: Before executing a pop() or a peek(), move all elements from newestStack to oldestStack if oldestStack is empty
         * 
         * Time Complexity: O(n) where n = length of newestStack because all elements from newestStack is being passed on to oldestStack
         * 
         * Space Complexity: O(n) where n = length of newestStack. Although the number of elements aren't changing, oldestStack will still take the same
         *                  amount of space as newestStack.
         */
        
        if (oldestStack.isEmpty()) {
            while (!newestStack.isEmpty()) {

                // Add newest elements from newestStack to oldestStack
                oldestStack.push(newestStack.pop());
            }
        }
    }

    int pop() {

        /*
         * OBJECTIVE: Remove and return last element from stack
         * 
         * Time Complexity: O(1) because only the head element is being removed
         * 
         * Space Complexity: O(1) because no additional space is being used. In reality, I'm giving back space to the computer
         */
        
        // Update stack
        shiftStack();

        // If stack is empty, exit function
        if (oldestStack.isEmpty()) {return -1;}

        // Pop and return oldest element
        return oldestStack.pop();
    }

    int peek() {

        /*
         * OBJECTIVE: Return value of oldest element from stack
         * 
         * Time Complexity: O(1) because I'm only checking the value of the head element
         * 
         * Space Complexity: O(1) because no additional space is being used
         */

        // Update stack
        shiftStack();

        // If stack is empty, exit function
        if (oldestStack.isEmpty()) {return -1;}

        // Return value of oldest element
        return oldestStack.peek();
    }

    void printQueue() {


        /*
         * OBJECTIVE: Print queue
         * 
         * Time Complexity: O(n) where n = size of oldestStack. In the first while-loop, all the elements from oldestStack is printed then being transferred
         *                  to a temporary stack. The 2nd while-loop adds all the elements from tmp stack back to oldestStack
         * 
         * Space Complexity: O(1) because no additional space is being used
         */

        // Update stack
        shiftStack();

        // If stack is empty, exit function
        if (oldestStack.isEmpty()) {return;}

        // Create a temporary stack
        Stack<Integer> tmp = new Stack<Integer>();

        // Iterate oldestStack
        while (!oldestStack.isEmpty()) {
            
            // Capture popped element
            int popped = oldestStack.pop();
            tmp.push(popped);

            // Print value
            System.out.printf("%d ", popped);
        }

        // Add all elements from tmp back to oldestStack
        while (!tmp.isEmpty()) {
            oldestStack.push(tmp.pop());
        }
    }
}