from stack import Stack
from random import randint
import sys

class StackTest:

    def __init__(self) -> None:
        
        # Initialize stack class
        self.stack = Stack()
        self.minValues = list()

    def test_push(self):

        # OBJECTIVE: Populate stack with random integers

        numOfElems = 10
        for _ in range(numOfElems):

            # Generate random number
            ranNumber = randint(1, 100)

            # Add ranNumber to stack
            self.minValues.append(ranNumber)
            self.stack.push(ranNumber)

        # Check that stack was populated
        assert self.stack.regSize == numOfElems

    def test_removal(self):

        # OBJECTIVE: Remove head element from stack

        # Capture old head element to remove it from local minValues list
        oldHead = self.stack.peek()
        self.minValues.remove(oldHead)

        # Check that head element equals to what was popped 
        assert oldHead == self.stack.remove()

    def test_getMin(self):

        # OBJECTIVE: Get minimal value from stack
        assert self.stack.getMin() == min(self.minValues)
    
    def test_peek(self):

        # OBJECTIVE: Return head element from stack

        assert self.stack.peek() == self.minValues[-1]
    
if __name__ == "__main__":

    # Initialize test class
    test = StackTest()

    test.test_push()
    test.test_removal()
    test.test_getMin()
    test.test_peek()
    test.stack.printStack()