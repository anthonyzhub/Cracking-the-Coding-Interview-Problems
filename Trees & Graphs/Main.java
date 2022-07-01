import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Initialize class
        BuildOrder sol = new BuildOrder();

        // Create a array and matrix
        String[] projects = {"a", "b", "c", "d", "e", "f"};
        String[][] dependencies = {
            {"a", "d"},
            {"f", "b"},
            {"b", "d"},
            {"f", "a"},
            {"d", "c"}
        };

        Stack<ProjectNode> ans = sol.findBuildOrder(projects, dependencies);
        Stack<ProjectNode> tmp = new Stack<ProjectNode>();
        while (!ans.empty()) {
            System.out.printf("%s ", ans.peek().getName());
            tmp.push(ans.pop());
        }

        while (!tmp.empty()) {
            ans.push(tmp.pop());
        }
    }
}
