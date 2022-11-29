# Cracking the Coding Interview - pp. 135 - q. 8.7

def getPermutations(prefixStr: str, remainderStr: str, res: list):

    # If input string is empty, add prefix string to list
    if len(remainderStr) == 0:
        res.append(prefixStr)
    
    # Iterate remainderStr
    for i in range(len(remainderStr)):

        # Split remainder string into 2 pieces: before and after i
        leftHalf = remainderStr[:i]
        rightHalf = remainderStr[i+1:]

        # Get ith letter from string
        curLetter = remainderStr[i]

        # Create remaining permutations on new input string with the left and right half
        getPermutations(prefixStr + curLetter, leftHalf + rightHalf, res)

def bookSolution(s1: str):

    """
    OBJECTIVE: Write a method to compute all permutations of a string of unique characters

    Time Complexity: O(n^2 * n!) where n = length of s1. In getPermutations(), the string is iterated and a recursive call is made. That is where n^2 comes
                    from. n! comes from the total number of permutations.
                    
                    The permutation formula is n!/(r-n)! where n = length of string and r = number of elements being used. In this scenario, all letters are
                    being used, so if "abc" was the input string and all 3 letters were being used, then the total number of permuations would be: 
                    3!/(3-3)! => 3!/0! => 6/1 => 6. *drops mic*
    
    Space Complexity: O(n!) where n = length of s1. A recursive call is made for every character in the string. n! comes from the permutation formula with
                    the same explanation as above.
    """

    # Create a list to hold output
    res = list()

    # Create all possible permutations and print them
    getPermutations("", s1, res)
    for permutation in sorted(res):
        print(permutation)

bookSolution("abc")