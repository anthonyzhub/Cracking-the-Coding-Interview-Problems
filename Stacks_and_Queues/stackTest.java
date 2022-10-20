// Cracking the Coding Interview - pp. 98 - q 3.2

import java.util.*;

public class stackTest {

    static void test_push(stack stackClass, ArrayList<Integer> minValues) {

        // OBJECTIVE: Populate stack with random integers

        // Initialize Random class
        Random rand = new Random();

        // Populate stack
        int numOfElems = 10;
        for (int i=0; i<numOfElems; i++) {

            // Generate a random number
            int ranNumber = rand.nextInt(100);

            // Add ranNumber to stack
            minValues.add(ranNumber);
            stackClass.push(ranNumber);
        }

        assert stackClass.regSize == numOfElems;
    }

    static void test_removal(stack stackClass, ArrayList<Integer> minValues) {

        // OBJECTIVE: Remove head element from stack

        // Capture old head element to remove it from local minValues array
        int oldHead = stackClass.peek();
        minValues.remove(oldHead);

        // Check that head element equals to what was popped
        assert oldHead == stackClass.pop();
    }

    static void test_getMin(stack stackClass, ArrayList<Integer> minValues) {
        
        // OBJECTIVE: Get minimal value from stack

        Collections.sort(minValues);
        assert stackClass.getMin() == minValues.get(0);
    }

    static void test_peek(stack stackClass, ArrayList<Integer> minValues) {

        // OBJECTIVE: Return head element from stack
        assert stackClass.peek() == minValues.get(-1);
    }

    public static void main(String[] args) {

        // Initialize stack class
        stack stackClass = new stack();
        ArrayList<Integer> minValues = new ArrayList<Integer>();

        test_push(stackClass, minValues);
        test_removal(stackClass, minValues);
        test_getMin(stackClass, minValues);
        test_peek(stackClass, minValues);
    }
}
