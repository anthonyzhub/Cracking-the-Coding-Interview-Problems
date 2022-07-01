# Cracking the Coding Interview - pp. 110 - q 4.7

from enum import Enum

class State(Enum):

    # OBJECTIVE: Create an enumerate class that represents state of a node

    COMPLETE = 1
    PARTIAL = 2
    BLANK = 3

class ProjectNode:

    # OBJECTIVE: Create a project class that is actually a node

    def __init__(self, name) -> None:

        # OBJECTIVE: Initialize new node with blank data and a blank state
        self.setState(State.BLANK)
        self.children = list()
        self.map = dict()
        self.name = name
        self.dependencies = 0

    def setState(self, newstate):

        # OBJECTIVE: Update node's state value (e.g., COMPLETE, PARTIAL, BLANK)
        self.state = newstate

    def getState(self):
        return self.state

    def getName(self):
        return self.name

    def getChildren(self):
        return self.children
    
    def getNumberOfDependencies(self):
        return self.dependencies

    def addNeighbor(self, adjacentNode):

        # OBJECTIVE: Connect adjacent node to this node as a neighbor

        # Check that adjacent node isn't already a neighbor
        if adjacentNode.getName() not in self.map:

            # Add adjacent node to list and dictionary
            self.children.append(adjacentNode)
            self.map[adjacentNode.getName()] = adjacentNode

            # Increment number of dependencies of this node
            adjacentNode.dependencies += 1

class Graph:

    def __init__(self) -> None:
        self.nodes = list()
        self.map = dict()

    def getOrCreateNode(self, name):

        # OBJECTIVE: Create or return a node from map

        # Check that node's name doesn't exist in map
        if name not in self.map:

            # Create a new project (node)
            node = ProjectNode(name)

            # Add project (node) to list and save it in dictionary
            self.nodes.append(node)
            self.map[name] = node

        # Return value at key
        return self.map[name]

    def addEdge(self, startName, endName):

        # OBJECTIVE: Connect start node to end node

        # Get nodes based on name. If node doesn't exist, create one
        start = self.getOrCreateNode(startName)
        end = self.getOrCreateNode(endName)

        # Connect start node to end node
        start.addNeighbor(end)

    def getNodes(self):
        # OBJECTIVE: Return all nodes that exist inside this graph
        return self.nodes

class Solution:

    def buildGraph(self, projects, dependencies):

        # Initialize graph class
        graph = Graph()

        # Create a node per project
        for project in projects:
            graph.getOrCreateNode(project)

        # Connect dependency node to dependent node
        # E.g., If project A relies on project B, then have project B point to project A
        for dependency in dependencies:

            # Parse data
            first = dependency[0]
            second = dependency[1]

            # Connect both nodes to each other
            graph.addEdge(first, second)
        
        return graph

    def doDFS(self, project, stack):

        # OBJECTIVE: Perform a dfs search on current project node

        # If node's state is already at PARTIAL (meaning it's in the process of a DFS), then return false
        # because a cycle has just been detected
        if project.getState() == State.PARTIAL:
            return False
        
        # If node's state is BLANK, then it hasn't been searched yet
        if project.getState() == State.BLANK:

            # Update node's state to PARTIAL meaning that it's being searched
            project.setState(State.PARTIAL)

            # Traverse project node's children
            children = project.getChildren()
            for child in children:

                # If function returns false, then a cycle was detected. 
                # Return false meaning that projects can't be completed
                if not self.doDFS(child, stack):
                    return False

            # If function is still continuing, set project node's status to COMPLETE.
            # This means that search was completed
            project.setState(State.COMPLETE)

            # Add node to stack (stack will be used as algorithm's output)
            stack.append(project.getName())

        return True

    def orderProjects(self, projects):

        # OBJECTIVE: Correct order of projects that need to be completed

        # Create a stack
        stack = list()

        # Iterate graph
        for project in projects:

            # Per node, if it's at a BLANK state, perform a dfs search on it
            if project.getState() == State.BLANK:

                # If dfs() returns false, then exit function because a cycle was detected
                if not self.doDFS(project, stack):
                    return None

        return stack

    def findBuildOrder(self, projects, dependencies):

        """
        * OBJECTIVE: Return a list of projects that need to be completed before the remaining projects
        *           E.g., 1st project must be completed before the remaining N - 1 projects
        *
        * Time Complexity: O(P + D) where P = # of projects and D = # of dependencies. The first step
        *                   was to take the input list and make a graph. 
        *
        * Space Complexity: O(P + D) where P = # of projects and D = # of dependencies because nodes and edges
        *                   were created to construct the graph
        """

        # Pass list and matrix to function and build a graph
        graph = self.buildGraph(projects, dependencies)

        # Return correct order of projects to complete
        return self.orderProjects(graph.getNodes())

def main():

    # Initialize class
    sol = Solution()

    # Create a list of projects and its dependencies
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [
        ["a", "d"],
        ["f", "b"],
        ["b", "d"],
        ["f", "a"],
        ["d", "c"]
    ]

    print(sol.findBuildOrder(projects, dependencies))

main()