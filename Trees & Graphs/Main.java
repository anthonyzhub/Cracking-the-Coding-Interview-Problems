public class Main {
    public static void main(String[] args) {

        // Create nodes
        GraphNode nodeA = new GraphNode();
        GraphNode nodeB = new GraphNode();
        GraphNode nodeC = new GraphNode();
        GraphNode nodeD = new GraphNode();

        nodeA.children.add(nodeB);
        nodeB.children.add(nodeC);
        nodeC.children.add(nodeD);
        // nodeD.children.add(nodeA);

        // Initialize class
        Route route = new Route();
        // boolean ans = route.bfs(nodeA, nodeB);
        boolean ans = route.biSearch(nodeD, nodeA);
        System.out.println(ans);
    }    
}
