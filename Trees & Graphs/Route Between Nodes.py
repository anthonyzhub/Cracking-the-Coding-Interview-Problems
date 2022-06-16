# Cracking the Coding Interview - pp. 109 - q 4.1

from GraphNode import Node
from collections import deque

class Route:

    def __init__(self) -> None:
        pass

    def bfs(self, sourceNode, destNode):

        """
         *
         * OBJECTIVE: Use breath-first search to determine if there's a route between source and destination node
         * 
         * Time Complexity: O(K^d) where K = # of kids per node and d = # of levels (or depth) I go through. In each iteration, I inspect every node and its
         *                  children. As I go down, I will visit a child and it's children.
         * 
         * Space Complexity: O(N) where N = length of queue and set data structures. In the worst case scenario, all nodes are visited and added to the queue
         *                   and set. The queue's size will fluctuate based on how many nodes haven't been visited yet. The set's size will increase after 
         *                   every iteration because I need to remember which nodes I visited to avoid a repetition.
         *
        """

        # If either nodes is null, return false
        if sourceNode is None or destNode is None:
            return False
        
        # If both are the same nodes, return true
        if sourceNode == destNode:
            return True
        
        # Create a queue to hold all the nodes and a set to hold visited nodes
        queue = deque([sourceNode])
        visited = set()

        # Iterate queue
        while queue:

            # Pop 1st element from queue
            curNode = queue.popleft()

            # Add curNode to visited set
            visited.add(curNode)
            
            # Add curNode's children to queue
            for child in curNode.children:

                # If child is destNode, return true
                if child == destNode:
                    return True

                # If child node isn't a node that I already visited, add it to queue
                if child not in visited:
                    queue.append(child)
        
        return False

    def biSearch(self, sourceNode, destNode):

        # OBJECTIVE: Use bidirectional search to check if there's a route between source and destination nodes

        # If either nodes are empty, exit function
        if sourceNode is None or destNode is None:
            return False
        
        # If both nodes are the same, return true
        if sourceNode == destNode:
            return True

        # Create a queue and a visited set
        sourceQueue = deque([sourceNode])
        destQueue = deque([destNode])

        visitedSource = set()
        visitedDest = set()

        # Iterate queue
        while sourceQueue and destQueue:

            # Pop elements from source and destination queues
            curSourceNode = sourceQueue.popleft()
            curDestNode = destQueue.popleft()

            # Add both to visited set
            visitedSource.add(curSourceNode)
            visitedDest.add(curDestNode)

            # Iteration curSourceNode's children
            for child in curSourceNode.children:
                
                if child == destNode:
                    return True

                if child in visitedDest:
                    return True

                elif child not in visitedSource:
                    sourceQueue.append(child)

            # Iteration curDestNode's children
            for child in curDestNode.children:

                if child == sourceNode:
                    return True

                if child in visitedSource:
                    return True
                
                elif child not in visitedDest:
                    destQueue.append(child)

        # Iterate visitedSource queue
        while sourceQueue:

            if self.bfs(sourceQueue.popleft(), destNode) == True:
                return True

        # Iterate visitedDest queue
        while destQueue:

            if self.bfs(destQueue.popleft(), sourceNode) == True:
                return True

        return False

def main():

    # Create a directed graph
    nodeA = Node()
    nodeB = Node()
    nodeC = Node()
    nodeD = Node()

    nodeA.children.append(nodeB)
    nodeB.children.append(nodeC)
    nodeC.children.append(nodeA)
    nodeD.children.append(nodeA)

    # Initialize solution
    route = Route()
    # ans = route.bfs(nodeA, nodeC)
    ans = route.biSearch(nodeA, nodeD)
    print(ans)

main()