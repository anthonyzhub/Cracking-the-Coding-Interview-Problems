# Cracking the Coding Interview - pp. 134 - q. 8.1

def stepHelper(nth: int, memo: list[int]) -> int:
    
    # OBJECTIVE: Calculate how many possible ways there are to reach the nth step

    # If steps is less than 0, return 0
    if nth < 0:
        return 0

    # If steps equals to 1, return 1
    elif nth == 0:
        return 1
    
    # If answer was already recorded, save it to list
    elif memo[nth] > -1:
        return memo[nth]

    else:
        # Make a recursive call and save output to list
        memo[nth] = stepHelper(nth - 1, memo) + stepHelper(nth - 2, memo) + stepHelper(nth - 3, memo)

        # NOTE: Will raise error of not able to add int with none
        return memo[nth]

def steps(steps: int):

    """
    OBJECTIVE: Calculate how many ways there are to reach n steps

    Time Complexity: O(1) because no looping was used in this algorithm

    Space Complexity: O(n) where n = steps because stepHelper() is making recursive calls, so each call adds on to
                        the memory stack. 

                        Also, if the execution was outlined as a tree, the tree's height is n levels tall.
    """

    # Create a list filled with -1's
    # NOTE: Each index will hold a value representing how many ways a person can get there
    res = [-1] * (steps + 1)

    # Calculate all possibilities
    stepHelper(steps, res)
    print(res[1:])

steps(5)