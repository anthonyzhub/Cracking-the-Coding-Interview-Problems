# Cracking the Coding Interview - pp. 135 - q. 8.4

def make(arr: list[int], startPtr: int, cur: list[int], res: list[list[int]]):

    # If pointers go out-of-bounds, exit function
    if startPtr >= len(arr):
        if cur not in res:
            res.append(list(cur))
        return
    
    # If cur isn't in res and isn't empty, add it
    if cur not in res and cur != []:
        res.append(list(cur))

    # Iterate arr
    for i in range(startPtr, len(arr)):

        # Add element to cur
        cur.append(arr[i])

        # Make a recursive call
        make(arr, i + 1, cur, res)

        # Drop recently added element
        cur.pop(-1)

def powerSubsets(arr: list[int]) -> None:

    """
    OBJECTIVE: Create a list of all possible sets from arr
    
    Time Complexity: O(n * 2^n) where n = length of arr. There is expected to be a total of 2^n subsets that can be made
                    from arr because each element has 2 options. Each element can either be in curList or not.

                    Now, the best case time comes from the summation of all subsets' length. If there are n elements and each
                    element will be listed in half of all subsets, then the final time/space complexity is O(n * 2^n)

    Space Complexity: O(n * 2^n) where n = length of arr. The reasoning is the same as time complexity
    """

    # If list's length is 1 or less, return it
    if len(arr) <= 1:
        return arr
    
    # Create a return list
    res = list()

    # Create all possible subsets
    make(arr, 0, [], res)

    print(res)

powerSubsets([1, 2, 3])