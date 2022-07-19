# Cracking the Coding Interview - pp. 111 - q 4.10

from collections import deque
from TreeNode import Node

class Inspector:

    def matchTree(self, t1, t2):

        # OBJECTIVE: Compare t1 and t2 trees node by node

        # If both roots are empty, return true
        if t1 == None and t2 == None:
            return True

        # If only 1 root is empty, return false since a discrepancy was found
        elif t1 == None or t2 == None:
            return False

        # If both roots don't share teh same value, then return false
        elif t1.val != t2.val:
            return False

        # If function is still continuing, check both of their children to see if the tree still matches
        else:
            return self.matchTree(t1.left, t2.left) and self.matchTree(t1.right, t2.right)

    def subtree(self, t1, t2):

        # OBJECTIVE: Traverse tree until both root nodes share the same value. That'll be the starting point to see
        #            if t2 is a subtree of t1

        # If t1 is empty, return false because t2 can't be a subtree of an empty tree
        if t1 == None:
            return False

        # If both roots share the same value and t2 was found inside of t1, then return true
        elif (t1.val == t2.val) and (self.matchTree(t1, t2)):
            return True

        # Make a recursive call on both of their children to find out if t2 is a part of t1
        else:
            return self.subtree(t1.left, t2.left) or self.subtree(t1.right, t2.right)

    def containsTree(self, t1, t2):

        """
        * OBJECTIVE: Check if t2 is a subtree of t1 by using breadth-first search and recursive calls
        *
        * Time Complexity: O(t1 * t2) where t1 and t2 represents the number of nodes that exist in each tree. 
        *
        * Space Complexity: O(log(t1) + log(t2)) where t1 and t2 represents the number of nodes that exist in each tree.
        """

        # If t2 is empty, return tree because an empty tree is always a subtree
        if t2 == None:
            return True
        
        return self.subtree(t1, t2)

    """
    ^ Book's solution ^

    v My Solution v
    """

    def inspect(self, t1, t2):
        
        # OBJECTIVE: Compare t1 and t2 and their children. If they're a match, continue with traversal. If not, return false

        # If either node is empty, return false
        if (t1 == None and t2 != None) or (t1 != None and t2 == None):
            return False

        elif (t1 == None and t2 == None):
            return True
        
        # If both roots don't share the same value, return false
        if t1.val != t2.val:
            return False
        
        # Check if both have children
        return self.inspect(t1.left, t2.left) and self.inspect(t1.right, t2.right)
        
    def bfs(self, t1, t2):

        # OBJECTIVE: Perform a breadth-first search to find t2 inside of t1

        # Create a queue
        queue = deque()
        queue.append(t1)

        # Iterate queue
        while queue:

            # Pop 1st element from queue
            poppedNode = queue.popleft()

            # Check if popped node equals to t2
            if poppedNode.val == t2.val:

                # If true, then t2 was found inside of t1. Return true to end algorithm
                if self.inspect(poppedNode, t2) == True:
                    return True

            # Add its children to queue
            if poppedNode.left:
                queue.append(poppedNode.left)
            
            if poppedNode.right:
                queue.append(poppedNode.right)

        # Return false if couldn't find t2 inside t1
        return False

    def checkSubtree(self, t1, t2):

        """
        * OBJECTIVE: Check if t2 is a subtree of t1 by using breadth-first search and recursive calls
        *
        * Time Complexity: O(K^d + cr*t2) where K = the maximum number of kids a node can have, d = how far deep bfs()
        *                   goes through, cr = # of common root found in t1 of t2's root, t2 = # of nodes in t2
        *
        *                   bfs() takes O(K^d) time because the function is looking for a node that shares the same
        *                   value as t2's root node. bfs() will continue until a matching node is found and if t2
        *                   does exist inside of t1.
        *
        *                   inspect() takes O(cr * t2) time because for every common root that is found in t1, inspect()
        *                   will be called and it will traverse the t2 tree. All t2 nodes will be traversed and compared
        *                   against the incoming nodes t1. If a discrepancy is found, inspect() will stop and won't
        *                   continue until another common root is found in bfs().
        *
        * Space Complexity: O(n * cr * t2) where n = # of nodes inside queue, cr = # of common roots found in t1 of t2's
        *                   root, and t2 = # of nodes inside of t2.
        * 
        *                   bfs() features a queue where it will hold t1's nodes. The queue size changes on every loop
        *                   because an element will be popped and its children will be added to the queue.
        *
        *                   inspect() takes O(cr * t2) time because for every common root that is found in t1, inspect()
        *                   will be called and it will traverse the t2 tree. All t2 nodes will be traversed and compared
        *                   against the incoming nodes t1. If a discrepancy is found, inspect() will stop and won't
        *                   continue until another common root is found in bfs().
        """

        # If either nodes are empty, return false
        if (t1 == None and t2 != None) or (t1 != None and t2 == None):
            return False
        
        # If both roots are equal to each other, return true
        if t1.val == t2.val:
            return True
        
        # Perform a breadth-first search and determine if t2 is a subtree of t1
        return self.bfs(t1, t2)

def main():

    # Create a tree
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    i = Node("I")
    j = Node("J")

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    d.left = f
    d.right = h

    c.left = g
    c.right = i

    g.left = j

    # Initialize class
    sol = Inspector()
    print(sol.checkSubtree(a, Node("A")))

main()