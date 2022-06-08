# Cracking the Coding Interview - pp. 98 - q 3.5

from stack import Stack

class SortStack:

    def __init__(self) -> None:

        # Initialize stack class
        self.stack = Stack()

    def push(self, newVal):

        # OBJECTIVE: Add new value to stack in ascending order

        # If stack is empty, add newVal to stack and exit function
        if self.stack.isEmpty():
            self.stack.push(newVal)
            return

        # If stack isn't empty, pop every element from stack until newVal is added in correct order
        tmp = Stack()

        # Iterate stack
        while not self.stack.isEmpty():
            
            # Pop element from stack
            curHead = self.stack.peek()

            # If popped is smaller than 
            if curHead < newVal:
                tmp.push(self.stack.pop())
            else:
                break

        # Add newVal to stack
        self.stack.push(newVal)

        # Add all elements from tmp back to stack
        while not tmp.isEmpty():
            self.stack.push(tmp.pop())

    def pop(self):

        # OBJECTIVE: Remove head element from stack and return it
        return self.stack.pop()

    def peek(self):

        # OBJECTIVE: Return value of head element from stack
        return self.stack.peek()

    def isEmpty(self):

        # OBJECTIVE: Return true/false if stack is empty
        return self.stack.isEmpty()

    def printStack(self):

        # OBJECTIVE: Print stack
        self.stack.printStack()

def main():

    # Initialize class
    sortedStack = SortStack()
    sortedStack.push(1)
    sortedStack.push(21)
    sortedStack.push(153)
    sortedStack.push(1123)
    sortedStack.push(0)

    sortedStack.printStack()

    sortedStack.pop()
    sortedStack.printStack()

main()