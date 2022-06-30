class CustomNode:

    def __init__(self, val=0, left=None, right=None, parent=None) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Successor:

    def inorder(self, root):

        if root != None:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def leftMostChild(self, n):

        # If root != empty, exit function
        if n != None:
            return

        # Move down the left subtree
        # NOTE: Inorder traversal goes left => root => right, so every node visit goes to the left child
        while n.left != None:
            n = n.left
        
        # Return next successor in inorder traversal
        return n

    def inorderSuccessor(self, n):

        # If root is empty, exit function
        if n != None:
            return
        
        # If root has a right child, traverse left subtree
        if n.right != None:
            return self.leftMostChild(n.right)
        
        else:

            # Copy root and its parent
            q = n
            x = q.parent
            
            # Go up the tree
            while x != None and x.left != q:

                # Move up curNode to parent
                q = x

                # Move to curNode's grandparent
                x = x.parent

            return x

    def in_order_successor(self, input_node):
        if input_node is None:
            return None

        if input_node.right:
            current = input_node.right
            while current.left:
                current = current.left
            return current

        ancestor = input_node.parent
        child = input_node
        while ancestor and ancestor.right == child:
            child = ancestor
            ancestor = ancestor.parent
        return ancestor


def main():

    # Create a tree
    root = CustomNode(8) # Level 1
    level_1_a = CustomNode(7)
    level_1_b = CustomNode(12)

    level_2_a = CustomNode(3)
    level_2_b = CustomNode(11)
    level_2_c = CustomNode(13)

    root.left = level_1_a
    root.right = level_1_b

    level_1_a.left = level_2_a
    level_1_b.left = level_2_b
    level_1_b.right = level_2_c

    # Initialize solution
    sol = Successor()
    sol.inorder(root)
    print(level_2_a.val)
    nextNode = sol.in_order_successor(level_2_a)
    print("{} => {}".format(level_2_a.val, nextNode))

main()