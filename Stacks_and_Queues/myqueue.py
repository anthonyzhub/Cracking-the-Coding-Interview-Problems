# Cracking the Coding Interview - pp. 98 - q 3.4

class MyQueue:

    def __init__(self) -> None:
        
        # Create 2 stacks
        self.newestStack = list()
        self.oldestStack = list()

    def shiftStack(self):

        """
         * OBJECTIVE: Before executing a pop() or a peek(), move all elements from newestStack to oldestStack if oldestStack is empty
         * 
         * Time Complexity: O(n) where n = length of newestStack because all elements from newestStack is being passed on to oldestStack
         * 
         * Space Complexity: O(n) where n = length of newestStack. Although the number of elements aren't changing, oldestStack will still take the same
         *                  amount of space as newestStack.
        """

        if len(self.oldestStack) == 0:

            # Move all elements from newestStack to oldestStack
            while len(self.newestStack) != 0:
                self.oldestStack.append(self.newestStack.pop())

    def add(self, newVal):

        """
         *
         * OBJECTIVE: Add new value to stack
         * 
         * Time Complexity: O(1) because element is added at the top of the stack
         * 
         * Space Complexity: O(1) because stack takes up an additional, constant space element
         *
        """

        # OBJECTIVE: Add new value from stack
        self.newestStack.append(newVal)

    def pop(self):

        """
         *
         * OBJECTIVE: Remove and return last element from stack
         * 
         * Time Complexity: O(1) because only the head element is being removed
         * 
         * Space Complexity: O(1) because no additional space is being used. In reality, I'm giving back space to the computer
         *
        """

        # Update stack
        self.shiftStack()

        # If stack is empty, exit function
        if len(self.oldestStack) == 0:
            return

        # Pop oldest element
        return self.oldestStack.pop()

    def peek(self):

        """
         *
         * OBJECTIVE: Return value of oldest element from stack
         * 
         * Time Complexity: O(1) because I'm only checking the value of the head element
         * 
         * Space Complexity: O(1) because no additional space is being used
         *
        """
        
        # Update stack
        self.shiftStack()

        # If stack is empty, exit function
        if len(self.oldestStack) == 0:
            return

        # Return value of front element
        return self.oldestStack[0]

    def printQueue(self):

        """
         *
         * OBJECTIVE: Print queue
         * 
         * Time Complexity: O(n) where n = size of oldestStack. In the first while-loop, all the elements from oldestStack is printed then being transferred
         *                  to a temporary stack. The 2nd while-loop adds all the elements from tmp stack back to oldestStack
         * 
         * Space Complexity: O(1) because no additional space is being used
         *
        """

        # Update stack
        self.shiftStack()

        # If stack is empty, exit function
        if len(self.oldestStack) == 0:
            return

        # Create a temporarily stack
        tempStack = list()

        # Iterate oldestStack
        ans = ""
        while len(self.oldestStack) != 0:
            
            # Pop oldest element
            ans += "{} ".format(self.oldestStack[-1])
            tempStack.append(self.oldestStack.pop())

        # Print queue
        print(ans)

        # Add all elements from tempStack back to oldest stack
        while len(tempStack) != 0:
            self.oldestStack.append(tempStack.pop())

def main():

    # Initialize class
    queueClass = MyQueue()

    queueClass.add(1)
    queueClass.add(2)
    queueClass.add(3)
    queueClass.add(4)
    queueClass.add(5)
    queueClass.add(50)
    queueClass.add(51)

    queueClass.peek()
    queueClass.pop()
    queueClass.printQueue()

main()