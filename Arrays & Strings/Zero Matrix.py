# Cracking the Coding Interview - pp. 91 - q 1.8

class Solution:

    def changeColumn(self, matrix, yPos):

        # OBJECTIVE: Change every cell's value in column to 0

        # Traverse column
        for x in range(len(matrix)):
            matrix[x][yPos] = 0

    def changeRow(self, matrix, xPos):

        # OBJECTIVE: Change every cell's value in row to 0

        # Traverse row
        for y in range(len(matrix[0])):
            matrix[xPos][y] = 0

    def solOne(self, matrix):

        """
            OBJECTIVE: If a row and a cell has a 0, change entire row and column to 0

            Time complexity: O((M + N) + MN + (M * # of elements inside of M) + (N * # of elements inside of n))
                (M + N) is the length and width of the matrix. After creating "rows" and "columns" array, Java goes through both arrays and fill each index with false.
                (MN) is the length and width of the matrix. I traverse the matrix to find any cells with a value of 0.
                (M * # of elements inside of M) is the length of "rows" and how many elements will need to be changed to 0. After traversing the matrix, I go through "rows" to find
                    index with "True" and then pass the work to changeRow(). In changeRow(), Java will go through every element in a 0-holding row.
                (N * # of elements inside of n) is similar to "M * # of elements inside of n", instead it focuses on columns

            Space complexity: O(M + N) where M = length of matrix and N = length of row inside the matrix. "rows" and "columns" gets initialized at the beginning
                and is based on matrix's size.
        """

        # If matrix is empty, exit function
        if len(matrix) == 0:
            return

        # Columns and rows to avoid
        column = [False] * len(matrix[0])
        row = [False] * len(matrix)
        
        # Traverse matrix
        for xPos in range(len(matrix)):
            for yPos in range(len(matrix[0])):

                # Check if cell is a 0
                if matrix[xPos][yPos] == 0:
                    column[yPos] = True
                    row[xPos] = True

        # Traverse column list and change entire column to 0 if applicable
        for x in range(len(column)):

            if column[x] == True:
                self.changeColumn(matrix, x)

        for y in range(len(row)):

            if row[y] == True:
                self.changeRow(matrix, y)

def main():

    sol = Solution()
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #     [0, 10, 11]
    # ]

    matrix = [
        [0, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    sol.solOne(matrix)
    print(matrix)

main()