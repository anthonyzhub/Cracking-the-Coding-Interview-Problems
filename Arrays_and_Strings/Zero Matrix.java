// Cracking the Coding Interview - pp. 91 - q 1.8

import java.util.*;

class ZeroMatrix {

    public static void changeRow(int[][] matrix, int xPos) {

        // OBJECTIVE: Change every cell in row i to 0

        // Traverse matrix
        for (int j=0; j<matrix[0].length; j++) {
            matrix[xPos][j] = 0;
        }
    }

    public static void changeColumn(int[][] matrix, int yPos) {

        // OBJECTIVE: Change every cell in column j to 0

        // Traverse matrix
        for (int i=0; i<matrix.length; i++) {
            matrix[i][yPos] = 0;
        }
    }

    public static void solOne(int[][] matrix) {

        /*
            OBJECTIVE: If a row and a cell has a 0, change entire row and column to 0

            Time complexity: O((M + N) + MN + (M * # of elements inside of M) + (N * # of elements inside of n))
                (M + N) is the length and width of the matrix. After creating "rows" and "columns" array, Java goes through both arrays and fill each index with false.
                (MN) is the length and width of the matrix. I traverse the matrix to find any cells with a value of 0.
                (M * # of elements inside of M) is the length of "rows" and how many elements will need to be changed to 0. After traversing the matrix, I go through "rows" to find
                    index with "True" and then pass the work to changeRow(). In changeRow(), Java will go through every element in a 0-holding row.
                (N * # of elements inside of n) is similar to "M * # of elements inside of n", instead it focuses on columns

            Space complexity: O(M + N) where M = length of matrix and N = length of row inside the matrix. "rows" and "columns" gets initialized at the beginning
                and is based on matrix's size.
        */

        // If matrix is empty, exit function
        if (matrix.length == 0) {return;}

        // Create an array representing rows and columns
        Boolean[] rows = new Boolean[matrix.length];
        Boolean[] columns = new Boolean[matrix[0].length];

        Arrays.fill(rows, false);
        Arrays.fill(columns, false);

        // Traverse array and find a cell that has a 0
        for (int i=0; i<matrix.length; i++) {
            for (int j=0; j<matrix[0].length; j++) {

                // If cell has a 0, save i & j in rows and columns, respectively
                if (matrix[i][j] == 0) {
                    rows[i] = true;
                    columns[j] = true;
                }
            }
        }

        // Change all rows that 0s
        for (int i=0; i<rows.length; i++) {
            if (rows[i] == true) {
                changeRow(matrix, i);
            }
        }

        // Change all columns that 0s
        for (int j=0; j<columns.length; j++) {
            if (columns[j] == true) {
                changeColumn(matrix, j);
            }
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {0, 10, 11}
        };

        solOne(matrix);
        for (int[] row: matrix) {
            for (int elem: row) {
                System.out.print(elem + " ");
            }
            System.out.println();
        }
    }
}