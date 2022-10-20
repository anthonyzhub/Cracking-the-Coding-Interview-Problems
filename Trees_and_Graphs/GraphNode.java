import java.util.*;

public class GraphNode {

    int val;
    LinkedList<GraphNode> children = new LinkedList<GraphNode>();

    GraphNode(){}
    GraphNode(int val) {this.val = val;}
}