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