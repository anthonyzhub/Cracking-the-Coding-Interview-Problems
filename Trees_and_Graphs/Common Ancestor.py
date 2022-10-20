# Cracking the Coding Interview - pp. 110 - q 4.8

class ResultNode:

    def __init__(self, answerNode, isAncestor) -> None:
        self.answerNode = answerNode
        self.isAncestor = isAncestor

class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class CommonAncestor:

    def depth(self, root):

        # OBJECTIVE: Calculate root's depth inside of tree and return it

        # Create a depth counter
        depth = 0

        # Move up the tree
        while root != None:

            # Update root and depth counter
            root = root.parent
            depth += 1

        return depth

    def goUp(self, root, depthDiff):

        # OBJECTIVE: Move root node up the tree until depthDiff is 0

        # Continue while root isn't empty and depthDiff hasn't reached 0 yet
        while root is not None and depthDiff > 0:
            root = root.parent
            depthDiff -= 1

        # Return new node
        return root

    def commonAncestorWithLinkToParent(self, p, q):

        """
        * OBJECTIVE: Find common ancestor between node p and q with parent attribute
        * NOTE: Each node will have a pointer to its parent
        *
        * Time Complexity: O(d) where d = is the depth of deepNode. If the tree is 8 levels tall and deepNode is at 3, then the remaining 5 levels aren't
        *                   searched because shallowNode is higher than where deepNode is. The while-loop inside depth() only goes as far as deepNode's level.
        *
        *                   The loop inside goUp() executes "diff" times until shallowNode is at the same level as deepNode. From there, both nodes are moved
        *                   up the tree until they reach a common ancestor. The ancestor can be root or a child of root.
        *
        * Space Complexity: O(1) because no dynamic data structures were created and a recursive function isn't used.
        """

        # If either root is empty, exit function
        if p is None or q is None:
            return
        
        # Calculate difference in depth
        depthDiff = abs(self.depth(p) - self.depth(q))

        # Classify shallow and deeper node
        deepNode = q if depthDiff > 0 else p
        shallowNode = p if depthDiff > 0 else q

        # Move deepNode up until it reaches the same level (depth) as shallowNode
        deepNode = self.goUp(deepNode, depthDiff)

        # Move up the tree until an intersection or a None appears
        while deepNode != shallowNode and deepNode is not None and shallowNode is not None:
            deepNode = deepNode.parent
            shallowNode = shallowNode.parent

        # If either nodes are empty, exit function
        # NOTE: This means that both nodes weren't a part of the same tree
        if deepNode is None or shallowNode is None:
            return

        # Return either node since both are at ancestor node
        return deepNode

    def commonAncestorHelper(self, root, p, q):

        # OBJECTIVE: Continue to make recursive calls on a common ancestor has been found or p/q node becomes null

        # If root is empty, exit function
        if root is None:
            return ResultNode(root, False)
        
        # If both nodes equal to root, return root because root is the common ancestor
        if root == p and root == q:
            return root
        
        # Check if ancestor exist on the left subtree
        leftSubtree = self.commonAncestorHelper(root.left, p, q)
        if leftSubtree.isAncestor:
            return leftSubtree

        # Check if ancestor exist on the right subtree
        rightSubtree = self.commonAncestorHelper(root.right, p, q)
        if rightSubtree.isAncestor:
            return rightSubtree

        # If p and q exist on separate subtrees from current root, return root as common ancestor
        if leftSubtree.answerNode is not None and rightSubtree.answerNode is not None:
            return ResultNode(root, True)
        
        # If either subtree's root equals to root, return that subtree's root
        # I.e., If we're at p or q and one of those nodes is a subtree, then this root node is the common ancestor
        elif root == p or root == q:
            
            # Create a boolean variable
            isAncestor = (leftSubtree.answerNode is not None) or (rightSubtree.answerNode is not None)
            return ResultNode(root, isAncestor)

        # If either subtree nodes are empty, return the non-empty node as common ancestor
        else:
            
            # Capture the non-empty subtree node
            answerNode = leftSubtree.answerNode if leftSubtree.answerNode is not None else rightSubtree.answerNode
            return ResultNode(answerNode, False)

    def commonAncestorWithoutLinkToParent(self, root, p, q):

        """
        /*
         * OBJECTIVE: Find common ancestor between p and q nodes given the tree's root node
         * 
         * Time Complexity: O(n) where n = # of nodes that were visited in the traversal from commonAncestorHelper(). That function will check the root,
         *                  continue to go down the left subtree, then go through the right subtree. It won't stop until a common ancestor is found or
         *                  if one node reaches null.
         * 
         * Space Complexity: O(n) where n = # of recursive call made. A recursive call is made per node. The node's subtrees are traversed and it won't
         *                  stop until a common ancestor is found or if one node reachs null.
         */
        """

        # If either node is empty, exit function
        if p is None or q is None:
            return
        
        # Get common ancestor of both nodes
        result = self.commonAncestorHelper(root, p, q)

        # If resultNode contains the ancestor of p and q, return it. If not, return null
        if result.isAncestor == False:
            return result.answerNode

        return

def main():

    # Construct a binary search tree.
    # IMPORTANT: Make sure that ALL nodes have a reference to their parent node except for root
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")

    a.parent = None
    a.left = b
    a.right = c

    b.parent = a
    b.left = d
    b.right = e

    d.parent = b
    e.parent = b

    c.parent = a
    c.left = f
    c.right = h

    f.parent = c
    f.left = g

    h.parent = c

    g.parent = f

    # Initialize class
    sol = CommonAncestor()
    ans = sol.commonAncestorWithLinkToParent(h, g)
    # ans = sol.commonAncestorWithoutLinkToParent(a, b, c)

    if ans:
        print(ans.val)
    else:
        print(False)

main()