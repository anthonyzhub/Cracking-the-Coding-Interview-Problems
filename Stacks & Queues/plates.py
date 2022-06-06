from stack import Stack
from random import randint

class SetOfStacks:

    def __init__(self) -> None:
        
        # Create a list to hold stacks
        self.stackList = list()
        self.stackLimit = 10

    def push(self, newVal):

        # OBJECTIVE: Add newVal to list of stacks.

        # For first entry, create a new stack and add it to stackList
        if len(self.stackList) == 0:

            # Create a new instance of Stack class
            newStack = Stack()
            newStack.push(newVal)

            # Add new instance to stackList
            self.stackList.append(newStack)

        # For other entries, check if current stack will fall from having too many plates
        else:

            # Get last stack from stackList
            lastStack = self.stackList[-1]

            # If lastStack has already reached its limit, create a new instance of stack
            if lastStack.getSize() == self.stackLimit:

                # Create a new instance of Stack class
                newStack = Stack()
                newStack.push(newVal)

                # Add newStack to stackList
                self.stackList.append(newStack)

            # If not, add newVal to last stack
            else:

                lastStack.push(newVal)

    def getSize(self):

        # OBJECTIVE: Return number of elements that exist inside of linked list
        
        # If stackList is empty, exit function
        if len(self.stackList) == 0:
            return 0

        """
        # Calculate how many elements there are
        totalElems = len(self.stackList) * self.stackLimit

        # If last stack is partially full, subtract difference from totalElems
        if self.stackList[-1].getSize() != 10:
            totalElems -= 10 - self.stackList[-1].getSize()

        return totalElems"""

        totalSize = 0
        for curStack in self.stackList:
            totalSize += curStack.getSize()

        return totalSize

    def pop(self):

        # OBJECTIVE: Remove top element from last stack

        # If stackList is empty, exit function
        if len(self.stackList) == 0:
            return

        # Get last stack from stackList
        lastStack = self.stackList[-1]
        deletedVal = lastStack.remove()
        
        # If lastStack is now empty, remove it from stackList
        if lastStack.getSize() == 0:
            self.stackList.pop()

        return deletedVal

    def popAt(self, index):

        # OBJECTIVE: Remove element at specific index

        # If stackList is empty, exit function
        if len(self.stackList) == 0:
            print("There are no stacks")
            return

        # If index surpasses totalElems, exit function
        totalElems = self.getSize()
        if index > totalElems:
            print("Index will go out of bounds in stacks")
            return

        # Divide totalElems by stackLimit
        stackNum = 0
        while totalElems > self.stackLimit == 0:
            totalElems -= self.stackLimit
            stackNum += 1

        return self.stackList[stackNum].popAt(totalElems)

    def printStacks(self):

        for curStack in self.stackList[::-1]:
            curStack.printStack()
        
        print()

def main():

    # Initialize class
    stacks = SetOfStacks()

    # Populate stack
    print("Populate stack")
    for _ in range(randint(10, 30)):
        stacks.push(randint(1, 10))
    stacks.printStacks()

    # Pop stack
    print("Pop stack")
    stacks.pop()
    stacks.printStacks()

    print("Stacks size: {}\n".format(stacks.getSize()))

    # Pop element at index
    # popAtIndex = randint(1, stacks.getSize())
    popAtIndex = 1
    print("Pop at index {}".format(popAtIndex - 1))
    print("Popped {}".format(stacks.popAt(popAtIndex - 1)))
    stacks.printStacks()

main()