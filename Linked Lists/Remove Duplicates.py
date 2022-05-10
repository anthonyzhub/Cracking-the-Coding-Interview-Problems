# Cracking the Coding Interview - pp. 94 - q 2.1

from LinkedList import LinkedList

class RemoveDuplicates:

    def sortLinkedList(self, headNode):

        # OBJECTIVE: Sort linked list

        # Create a list
        buffer = list()

        # Traverse linked list
        curNode = headNode
        while curNode.next != None: # <= ".next" added since tail node is attached (it's still a node)

            # Add node's value to list
            buffer.append(curNode.val)

            # Move to next node
            curNode = curNode.next

        # Sort list
        buffer.sort()

        # Traverse linked list
        curNode = headNode
        while curNode.next != None: # <= ".next" added since tail node is attached (it's still a node)

            # Pop element from list and use it to update curNode's value
            curNode.val = buffer.pop(0)

            # Move to next node
            curNode = curNode.next

        return headNode

    def solOne(self, headNode):

        """
            OBJECTIVE: Sort unsorted linked list
            Time Complexity: O(n log n) where n = length of linked list.
            Space Complexity: O(n) where n = length of buffer[] list in sortLinkedList().
        """

        # If headNode is empty or by itself, exit function
        if headNode is None or headNode.next is None:
            return

        # Sort linked list
        self.sortLinkedList(headNode)

        # Get 2nd node from linked list
        curNode = headNode.next

        # Traverse linked list
        counter = 2
        while curNode.next != None:

            # Capture previous node
            prevNode = curNode.prev

            # If current and last node share same value, delete last node
            if prevNode.val == curNode.val:

                print(f"node #{counter-1} == node #{counter}")

                # Save node before curNode.prev
                nodeBefore = prevNode.prev

                # Connect last node's prev pointer to curNode
                nodeBefore.next = curNode
                curNode.prev = nodeBefore

                # Delete curNode's previous node
                # NOTE: "del curNode.prev" will cause an error, instead of "del prevNode"
                #       I think it's because I'm deleting ".prev" pointer instead of the actual node
                del prevNode

            # Move to next node
            curNode = curNode.next
            counter += 1
        
def main():

    # Initialize linked list
    ll = LinkedList()
    ll.append(0)
    ll.append(0)
    ll.append(21)
    ll.append(12)
    ll.append(0)
    ll.append(0)
    ll.append(0)

    # Initialize solution
    sol = RemoveDuplicates()
    sol.solOne(ll.getHead())
    ll.printList()

main()