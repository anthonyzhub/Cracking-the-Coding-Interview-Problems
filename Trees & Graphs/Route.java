import java.util.*;

public class Route {
    
    boolean bfs(GraphNode sourceNode, GraphNode destNode) {

        /*
         * OBJECTIVE: Use breath-first search to determine if there's a route between source and destination node
         * 
         * Time Complexity: O(V + E) where V = # of vertices and E = # of edges inside of the graph. BFS involves inspecting a node and visiting its children.
         *                  bfs() is inspecting each node and its children in order to find the destination node.
         * 
         * Space Complexity: O(N) where N = length of queue and visited data structures. queue is a list of nodes that need to be visited and visited holds
         *                  all the nodes that I already checked. Queue's size will fluctuate overtime while visited will increase until all nodes are collected.
         */

        // If either node is null, return false
        if (sourceNode == null || destNode == null) {return false;}

        // If both nodes equal to each other, return true
        if (sourceNode == destNode) {return true;}

        // Create a queue and a visited set
        LinkedList<GraphNode> queue = new LinkedList<GraphNode>();
        HashSet<GraphNode> visited = new HashSet<GraphNode>();

        // Add sourceNode to queue
        queue.add(sourceNode);

        // Iterate queue
        while (queue.size() > 0) {

            // Pop head element from queue
            GraphNode curNode = queue.pop();
            visited.add(curNode);

            // Go through curNode's children
            for (GraphNode child: curNode.children) {

                // If child is destNode, return true
                if (child == destNode) {return true;}

                // If child isn't in visited, add it to queue
                if (!visited.contains(child)) {
                    queue.add(child);
                }
            }
        }
        return false;
    }

    boolean biSearch(GraphNode sourceNode, GraphNode destNode) {

        /*
         * OBJECTIVE: Use bidrectional search to determine if there's a route between source and destination nodes. Bidrectional search performs
         *          2 breath-first search simultaneously.
         * 
         * Time Complexity: O()
         */

        // If either node is null, exit function
        if (sourceNode == null || destNode == null) {return false;}

        // If both nodes are equal to each other, return true
        if (sourceNode == destNode) {return true;}

        // Create a two queues - one per node
        LinkedList<GraphNode> sourceQueue = new LinkedList<GraphNode>();
        LinkedList<GraphNode> destQueue = new LinkedList<GraphNode>();

        sourceQueue.add(sourceNode);
        destQueue.add(destNode);

        // Create a hashset for visited nodes
        HashSet<GraphNode> visitedSource = new HashSet<GraphNode>();
        HashSet<GraphNode> visitedDest = new HashSet<GraphNode>();

        // Iterate both queues
        while (sourceQueue.size() > 0 && destQueue.size() > 0) {

            // Both head nodes from both linked lists
            GraphNode curSource = sourceQueue.pop();
            GraphNode curDest = destQueue.pop();

            // Inspect curSource's children
            for (GraphNode child: curSource.children) {

                // If child is destNode, return true
                if (child == destNode) {return true;}

                // If child already exist in destQueue, then a route was found so return true
                if (visitedDest.contains(child)) {
                    return true;
                }

                // If child wasn't visited by sourceNode's or by destNode's path, add it to sourceQueue
                else if (!visitedSource.contains(child)) {
                    sourceQueue.add(child);
                }
            }

            // Inspect curDest's children
            for (GraphNode child: curDest.children) {

                // If child is sourceNode, return true
                if (child == sourceNode) {return true;}

                // If child already exist in destQueue, then a route was found so return true
                if (visitedSource.contains(child)) {
                    return true;
                }

                // If child wasn't visited by sourceNode's or by destNode's path, add it to sourceQueue
                else if (!visitedDest.contains(child)) {
                    destQueue.add(child);
                }
            }
        }

        // If sourceQueue isn't empty, but destQueue is, continue bfs on it until it's empty
        while (sourceQueue.size() > 0) {

            // Return true if popped node reaches to destNode
            if (bfs(sourceQueue.pop(), destNode) == true) {return true;}
        }

        // If destQueue isn't empty, but sourceQueue is, continue bfs on it until it's empty
        while (destQueue.size() > 0) {

            // Return true if popped node reaches to sourceNode
            if (bfs(destQueue.pop(), sourceNode) == true) {return true;}
        }

        return false;
    }
}
