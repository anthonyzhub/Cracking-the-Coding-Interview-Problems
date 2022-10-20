# Cracking the Coding Interview - pp. 135 - q. 8.2

def traverseMatrix(grid: list[list[int]], m: int, n: int, res: list[int], visited: set, xPos: int, yPos: int):

    # OBJECTIVE: Traverse matrix

    # Exit function if going out of bounds
    if xPos < 0 or xPos >= m or yPos < 0 or yPos >= n:
        return False
    
    # If cell doesn't allow visits (-1), then exit function
    if grid[xPos][yPos] == -1:
        return False

    # If cell was previously visited, exit function
    if grid[xPos][yPos] in visited:
        return False
    else:
        visited.add(grid[xPos][yPos])

    # Add visiting cell to list in case it is part of path to route. If not, it will be deleted later
    res.append(grid[xPos][yPos])

    # If xPos and yPos is at the bottom-right cell, return true
    if xPos == m - 1 and yPos == n - 1:
        return True

    # If robot can go right and reach its destination, add cell to list and exit function
    if traverseMatrix(grid, m, n, res, visited, xPos, yPos + 1):
        return True

    # If robot can go down and reach its destination, exit function
    elif traverseMatrix(grid, m, n, res, visited, xPos + 1, yPos) and (xPos + 1, yPos) not in visited:
        return True

    # If robot couldn't go right or down, pop cell from list and return false
    res.pop(-1)
    return False

def robot(grid: list[list[int]]) -> bool:

    """
    OBJECTIVE: Return boolean variable indicating robot can reach the bottom-right corner from the top-left corner
    
    Time Complexity: O(mn) where m and n are the dimensions of grid. In traverseMatrix(), each cell is being visted
                    and repeated visited are being prevented with a set.
    
    Space Complexity: O(P) where P = length of res list. The list holds all the cells that forms a path from starting
                        cell to ending cell.
    """

    # If matrix is empty, exit function
    if len(grid) <= 0:
        return False
    
    # Get matrix's size
    m = len(grid)
    n = len(grid[0])

    # Create a list to hold path that was taken
    res = list()

    # Create a set to hold visited cells
    visited = set()

    # Traverse matrix
    ans = traverseMatrix(grid, m, n, res, visited, 0, 0)

    print(res) if ans else print("Impossible!")

grid = [
    [1, 2, -1],
    [-1, 5, 6],
    [-1, -1, 9]
]

robot(grid)