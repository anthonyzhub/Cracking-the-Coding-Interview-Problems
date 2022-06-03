// Cracking the Coding Interview - pp. 98 - q 3.2

import java.util.*;

class stack {

    Stack<Integer> regStack;
    int regSize;
    Stack<Integer> minStack;

    public stack() {
        this.regStack = new Stack<Integer>();
        this.regSize = 0;
        this.minStack = new Stack<Integer>();
    }

    private void pushToMinStack(int newVal) {

        // OBJECTIVE: Add a new element to stack in sorted order (ascending order)

        // If head of minStack is bigger than newVal, add newVal to minStack and exit function
        if (minStack.peek() >= newVal) {
            minStack.push(newVal);
            return;
        }

        // Create a temporary stack
        Stack<Integer> tmp = new Stack<Integer>();

        // Continue to pop elements from minValues stack until a larger head is reached
        while (minStack.size() > 0 && minStack.peek() < newVal) {

            // Pop head from minValues and add it to tmp
            tmp.push(minStack.pop());
        }

        // Add newVal to stack
        minStack.push(newVal);

        // Add all elements from tmp stack back to minValue
        while (tmp.size() > 0) {
            minStack.push(tmp.pop());
        }
    }

    private void removeFromMinStack(int oldVal) {

        // OBJECTIVE: Remove oldVal from minStack

        // If head element of minStack equals to oldVal, remove it and exit function
        if (minStack.peek() == oldVal) {
            minStack.pop();
            return;
        }

        // Create a temporary stack
        Stack<Integer> tmp = new Stack<Integer>();

        // Pop an element until oldVal is found in minStack
        while (minStack.size() > 0 && minStack.peek() != oldVal) {
            tmp.push(minStack.pop());
        }

        // Remove head element from stack since it equals to oldVal
        // NOTE: remove() will pop head element from regStack, so we're popping an element that we know it exists inside of minStack
        minStack.pop();

        // Add all elements from tmp stack back to minStack
        while (tmp.size() > 0) {
            minStack.push(tmp.pop());
        }
    }

    public int getMin() {

        // OBJECTIVE: Return smallest value (head element) from stack
        return minStack.peek();
    }

    public void push(int newVal) {

        // OBJECTIVE: Add newVal to the top of the stack
        
        // Add new value to stack
        regStack.add(newVal);
        regSize++;

        // Add new value to array list and sort it
        pushToMinStack(newVal);
    }

    public int remove() {
        
        // OBJECTIVE: Remove the head element of stack and return its value

        // If stack is empty, exit function
        if (regSize == 0) {return -1;}

        // Capture last element
        int lastVal = regStack.pop();
        regSize--;

        // Update minStack
        removeFromMinStack(lastVal);

        return lastVal;
    }

    public int peek() {

        // OBJECTIVE: Return value of head element without removing it

        // If stack is empty, exit function
        if (regSize == 0) {return -1;}

        return regStack.peek();
    }

    public boolean isEmpty() {

        // OBJECTIVE: Return a boolean value representing whether or not stack is empty
        return regSize == 0;
    }
}