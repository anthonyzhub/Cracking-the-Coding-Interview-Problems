// Cracking the Coding Interview - pp. 109 - q 4.1

import java.util.*;

public class Route {
    
    boolean bfs(GraphNode sourceNode, GraphNode destNode) {

        /*
         * OBJECTIVE: Use breath-first search to determine if there's a route between source and destination node
         * 
         * Time Complexity: O(K^d) where K = # of kids per node and d = # of levels (or depth) I go through. In each iteration, I inspect every node and its
         *                  children. As I go down, I will visit a child and it's children.
         * 
         * Space Complexity: O(N) where N = length of queue and set data structures. In the worst case scenario, all nodes are visited and added to the queue
         *                   and set. The queue's size will fluctuate based on how many nodes haven't been visited yet. The set's size will increase after 
         *                   every iteration because I need to remember which nodes I visited to avoid a repetition.
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
         * Time Complexity: O(K^(d/2)) where K = # of kids per node and d = # of levels (or depth) after every iteration. Bidirectional search involves
         *                  using bfs for both source and destination nodes, simultaneously. Since both are happening at the same time, I will only
         *                  need to go down d/2 times. 
         * 
         * Space Complexity: O(N) where N = total # of nodes inside the graph. Worst case scenario involves adding all nodes to their appropriate sets. The
         *                   queues' size will fluctuate and 
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
