# Cracking the Coding Interview - pp. 109 - q 4.3

from collections import deque
from ListNode import Node as ListNode
from TreeNode import Node as TreeNode

class Depths:

    def __init__(self) -> None:
        pass

    def printLists(self, listOfHeads):

        # Iterate list
        for head in listOfHeads:

            # Iterate linked list
            ans = ""
            while head != None:
                ans += "{} ".format(head.val)
                head = head.next
            
            # Print linked list
            print(ans)

    def bfs(self, root):

        """
        /*
         * OBJECTIVE: Create a linked list per level in Binary Tree. For example, if tree's height is 3 levels tall, then 
         *              there should be 3 separate linked lists where the nodes are from the same level.
         * 
         * Time Complexity: O(V + E) where V = # of vertices (nodes) and E = # of edges. Every node is pretty much visited and their kids are added to the queue
         *                  for future processing.
         * 
         * Space Complexity: O(L * N) where L = # of levels exist and N = # of nodes inside the queue. masterList is a LinkedList that will only hold the
         *                  head nodes of each level inside the tree. E.g., If a tree has 3 levels, then masterList will hold 3 heads TreeNodes. 
         * 
         *                  Queue exist to manage a queue of children nodes to inspect. Each child will be processed and dropped from the queue, but
         *                  if there are grandchildren, then they'll be added to the queue.
         */
         """

        # If root is empty, exit function
        if root is None:
            return
        
        # Create a queue
        queue = deque([root])
        listOfHeads = [ListNode(root.val)]

        # Traverse binary search tree
        while queue:

            # Pop queue
            poppedNode = queue.popleft()

            # Create linked list from node's children
            head = ListNode()
            if poppedNode.left and poppedNode.right:

                # Create linked list
                head.next = ListNode(poppedNode.left.val)
                head.next.next = ListNode(poppedNode.right.val)

                # Add children to queue
                queue.append(poppedNode.left)
                queue.append(poppedNode.right)
            
            # If left child is an only child
            elif poppedNode.left:

                # Create a linked list
                head.next = ListNode(poppedNode.left.val)

                # Add child to queue
                queue.append(poppedNode.left)

            # If right child is an only child
            elif poppedNode.right:
                
                # Create a linked list
                head.next = ListNode(poppedNode.right.val)

                # Add child to queue
                queue.append(poppedNode.right)
            
            # Add head of new linked list to a list
            if head.next:
                listOfHeads.append(head.next)

        self.printLists(listOfHeads)

def main():

    # Create a tree
    root = TreeNode(10)

    root.left = TreeNode(9)
    root.right = TreeNode(90)

    root.left.left = TreeNode(4)
    root.right.right = None

    root.right.left = None
    root.right.right = None

    # Initialize solution class
    depth = Depths()
    depth.bfs(root)

main()