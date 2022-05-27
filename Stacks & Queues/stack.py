class Stack:

    def __init__(self) -> None:

        # Create a regular stack
        self.regStack = list()
        self.regSize = 0

        # Create a min stack
        self.minStack = list()

    def pushToMinStack(self, newVal):

        # OBJECTIVE: Add newVal to minStack in ascending order

        # If head element in minStack is bigger than newVal, add it and exit function
        if len(self.minStack) > 0 and self.minStack[-1] >= newVal:
            self.minStack.append(newVal)
            return

        # Create a temporary stack
        tmp = list()

        # Pop head element from minStack until head is bigger than newVal
        while (len(self.minStack) > 0 and self.minStack[-1] < newVal):
            tmp.append(self.minStack.pop())

        # Add newVal to minStack
        self.minStack.append(newVal)

        # Add all elements from tmp stack back to minStack
        while (len(tmp) > 0):
            self.minStack.append(tmp.pop())

    def removeFromMinStack(self, oldVal):

        # OBJECTIVE: Remove oldVal from minStack

        # If head element in minStack is equals to oldVal, remove it and exit function
        if len(self.minStack) > 0 and self.minStack[-1] == oldVal:
            self.minStack.pop()
            return

        # Create a temporary stack
        tmp = list()

        # Pop head element from minStack until oldVal is found
        while (len(self.minStack) > 0 and self.minStack[-1] != oldVal):
            tmp.append(self.minStack.pop())

        # Remove oldVal from minStack
        self.minStack.pop()

        # Add all elements from tmp stack back to minStack
        while (len(tmp) > 0):
            self.minStack.append(tmp.pop())

    def getMin(self):

        # OBJECTIVE: Return minimum value from stack
        return self.minStack[-1]

    def push(self, newVal):

        # OBJECTIVE: Add newVal to top of the stack

        # Add newVal to regular stack
        self.regStack.append(newVal)
        self.regSize += 1

        # Add newVal to minStack and sort it
        self.pushToMinStack(newVal)

    def remove(self):

        # OBJECTIVE: Remove head of stack

        # If stack is empty, exit function
        if self.regSize == 0:
            return None

        # Pop last element
        lastVal = self.regStack.pop()
        self.regSize -= 1

        # Remove element from minStack
        self.removeFromMinStack(lastVal)

        return lastVal

    def peek(self):

        # OBJECTIVE: Return value of top element without removing it from the stack

        # If stack is empty, exit function
        if self.regSize == 0:
            return None

        return self.regStack[-1]

    def isEmpty(self):

        # OBJECTIVE: Return boolean variable representing if stack is empty or not
        return self.regSize == 0

    def printStack(self):

        # OBJECTIVE: Print all elements inside stack from top to bottom

        # NOTE: Since a list is being used with stack operations, I can cycle through the list. Python doesn't have a built-in stack data structure
        ans = ""
        for elem in reversed(self.regStack):
            ans += "{} ".format(elem)

        print(ans)