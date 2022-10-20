// Cracking the Coding Interview - pp. 135 - q. 8.2

import java.util.*;

public class Robot {

    public static boolean traverseMatrix(int[][] grid, int m, int n, ArrayList<Integer> res, HashSet<Integer> visited, int xPos, int yPos) {

        // Stop from going out of bounds
        if (xPos < 0 || xPos >= m || yPos < 0 || yPos >= n) {return false;}

        // If cell cannot be visited (-1), exit function
        if (grid[xPos][yPos] == -1) {return false;}

        // If cell was previously visited, exit function
        if (visited.contains(grid[xPos][yPos])) {
            return false;
        }
        else {
            visited.add(grid[xPos][yPos]);
        }

        // Add visiting cell to list in case it is part of path to route. If not, it will be deleted later
        res.add(grid[xPos][yPos]);

        // If cell is the destination cell, return true and exit function
        if (xPos == m - 1 && yPos == n - 1) {
            return true;
        }

        // If robot can go to the right and reach its destination, return true
        if (traverseMatrix(grid, m, n, res, visited, xPos, yPos + 1)) {
            return true;
        }

        // If robot can go down and reach its destinatino, return true
        else if (traverseMatrix(grid, m, n, res, visited, xPos + 1, yPos)) {
            return true;
        }

        // If robot couldn't go right or down, pop cell from list and return false
        res.remove(res.size() - 1);
        return false;
    }

    public static void travel(int[][] grid) {

        /*
         * OBJECTIVE: Return boolean variable indicating robot can reach the bottom-right corner from the top-left corner
         * 
         * Time Complexity: O(mn) where m and n are the dimensions of grid. In traverseMatrix(), each cell is being visted
         *                  and repeated visited are being prevented with a set.
         * 
         * Space Complexity: O(P) where P = length of res list. The list holds all the cells that forms a path from starting
         *                  cell to ending cell.
         */

        // If grid is empty, exit function
        if (grid.length == 0) {return;}

        // Get length of matrix
        int m = grid.length;
        int n = grid[0].length;

        // Create an array to hold path taken
        ArrayList<Integer> res = new ArrayList<>();

        // Create a set of all visited cells
        HashSet<Integer> visited = new HashSet<>();

        // Traverse matrix
        traverseMatrix(grid, m, n, res, visited, 0, 0);
        
        for (int i: res) {
            System.out.printf("%d ", i);
        }
    }

    public static void main(String[] args) {
        
        // Create a grid
        int[][] grid = {
            {1, 2, -1},
            {-1, 5, 6},
            {-1, -1, 9}
        };

        // Traverse grid
        travel(grid);
    }
}