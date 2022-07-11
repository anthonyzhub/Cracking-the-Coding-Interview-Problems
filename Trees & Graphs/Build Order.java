// Cracking the Coding Interview - pp. 110 - q 4.7

import java.util.*;

class ProjectNode {

    // OBJECTIVE: Create a project class that is actually a node

    // Create an enum that represents a node's state
    enum State {
        COMPLETE,
        PARTIAL,
        BLANK
    };

    // Create class variables
    private State state = State.BLANK;
    private ArrayList<ProjectNode> children = new ArrayList<ProjectNode>();
    private HashMap<String, ProjectNode> map = new HashMap<String, ProjectNode>();
    private String name;
    private int dependencies = 0;

    public ProjectNode(String name) {this.name = name;}

    public void setState(State newState) {
        // OBJECTIVE: Update node's state value (e.g., COMPLETE, PARTIAL, BLANK)
        state = newState;
    }

    public State getState() {return state;}

    public String getName() {return name;}

    public ArrayList<ProjectNode> getChildren() {return children;}

    public int getNumberOfDependes() {return dependencies;}

    public void addNeighbor(ProjectNode adjacentNode) {

        // OBJECTIVE: Connect adjacent node to this node as a neighbor

        // Check that adjacent node doesn't exist inside map
        if (!map.containsKey(adjacentNode.getName())) {

            // Add adjacent node as a neighbor and update map
            children.add(adjacentNode);
            map.put(adjacentNode.getName(), adjacentNode);

            // Increment number of dependencies of this node
            adjacentNode.dependencies++;
        }
    }
}

class Graph {

    // Create class variables
    ArrayList<ProjectNode> nodes = new ArrayList<ProjectNode>();
    HashMap<String, ProjectNode> map = new HashMap<String, ProjectNode>();

    public ProjectNode getOrCreateNode(String name) {

        // OBJECTIVE: Create or return a node from map

        // Check that node's name doesn't exist in map
        if (!map.containsKey(name)) {

            // Create a new project (node)
            ProjectNode newNode = new ProjectNode(name);

            // Add node to list and save it in map
            nodes.add(newNode);
            map.put(name, newNode);
        }

        return map.get(name);
    }

    public void addEdge(String startName, String endName) {

        // OBJECTIVE: Connect start node to end node

        // Get nodes based on name. If node doesn't exist, create it
        ProjectNode start = getOrCreateNode(startName);
        ProjectNode end = getOrCreateNode(endName);

        // Connect start node to end node
        start.addNeighbor(end);
    }

    public ArrayList<ProjectNode> getNodes() {
        return nodes;
    }
}

public class BuildOrder {

    Graph buildGraph(String[] projects, String[][] dependencies) {

        // Initialize graph class
        Graph graph = new Graph();

        // Create a node per project
        for (String project: projects) {
            graph.getOrCreateNode(project);
        }

        // Connect dependency node to dependent node
        // E.g., If project A relies on project B, then have project B point to project A
        for (String[] dependency: dependencies) {

            // Parse data
            String first = dependency[0];
            String second = dependency[1];

            // Connect both nodes to each other
            graph.addEdge(first, second);
        }

        return graph;
    }

    boolean doDFS(ProjectNode project, Stack<ProjectNode> nodesStack) {

        // OBJECTIVE: Perform a dfs search on current project node

        // If node's state is already at PARTIAL (meaning it's in the process of a DFS), then return false
        // because a cycle has just been detected
        if (project.getState() == ProjectNode.State.PARTIAL) {return false;}

        // If node's state is BLANK, then it hasn't been searched yet
        if (project.getState() == ProjectNode.State.BLANK) {

            // Update node's state to PARTIAl MEANING THAT IT'S BEING SEARCHED
            project.setState(ProjectNode.State.PARTIAL);

            // Traverse project node's children
            for (ProjectNode child: project.getChildren()) {

                // If function returns false, then a cycle was detected
                // Return false meaning that projects can't be completed
                if (!doDFS(child, nodesStack)) {return false;}

                // If function is still continuing, set project node's status to COMPLETE
                // This means that search was completed
                project.setState(ProjectNode.State.COMPLETE);

                // Add node to stack (stack will be used as algorithm's output)
                nodesStack.push(project);
            }
        }
        return true;
    }

    Stack<ProjectNode> orderProjects(List<ProjectNode> projects) {

        // OBJECTIVE: Correct order of projects that need to be completed

        // Create a stack
        Stack<ProjectNode> ans = new Stack<ProjectNode>();

        // Iterate graph
        for (ProjectNode project: projects) {

            // Per node, if it's at a BLANK state, perform a dfs search on it
            if (project.getState() == ProjectNode.State.BLANK) {

                // If dfs() returns false, then exit function because a cycle was detected
                if (!doDFS(project, ans)) {
                    return null;
                }
            }
        }
        return ans;
    }

    Stack<ProjectNode> findBuildOrder(String[] projects, String[][] dependencies) {

        /*
         * OBJECTIVE: Return a list of projects that need to be completed before the remaining projects
         *           E.g., 1st project must be completed before the remaining N - 1 projects
         *
         * Time Complexity: O(P + D) where P = # of projects and D = # of dependencies. The first step
         *                   was to take the input list and make a graph. 
         *
         * Space Complexity: O(P + D) where P = # of projects and D = # of dependencies because nodes and edges
         *                   were created to construct the graph
        */

        // Pass array and matrix to function and build a graph
        Graph graph = buildGraph(projects, dependencies);

        // Return correct order of projects to complete
        return orderProjects(graph.getNodes());
    }
}