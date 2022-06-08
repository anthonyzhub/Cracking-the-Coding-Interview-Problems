// Cracking the Coding Interview - pp. 98 - q 3.5

import java.util.*;

public class SortStack {

    // Create a stack
    Stack<Integer> stack;

    SortStack() {
        stack = new Stack<Integer>();
    }

    void push(int newVal) {

        // OBJECTIVE: Insert newVal to stack in correct order

        // If stack is empty, add newVal to stack and exit function
        if (stack.isEmpty()) {
            stack.push(newVal);
            return;
        }

        // If stack isn't empty, create a temporary stack and pop all elements from stack to it until finding a perfect place to add newVal
        Stack<Integer> tmp = new Stack<Integer>();

        // Iterate stack
        while (!stack.isEmpty()) {

            // Pop element from stack
            int curHead = stack.peek();

            // If curHead is smaller than newVal, pop it from stack
            if (curHead < newVal) {
                tmp.push(stack.pop());
            }
            else {
                break;
            }
        }

        // Add newVal to stack
        stack.push(newVal);

        // Iterate tmp and add all elements back to stack
        while (!tmp.isEmpty()) {
            stack.push(tmp.pop());
        }
    }

    int pop() {

        // OBJECTIVE: Pop and return head element from stack
        return stack.pop();
    }

    int peek() {
        
        // OBJECTIVE: Return value of head element from stack
        return stack.peek();
    }

    void printStack() {

        // OBJECTIVE: Print stack

        for (int elem: stack) {
            System.out.printf("%d ", elem);
        }
    }
}
