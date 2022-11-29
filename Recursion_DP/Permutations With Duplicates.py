# Cracking the Coding Interview - pp. 135 - q. 8.8

from collections import Counter

def getPermutations(lettersDict: dict, prefixStr: str, remaining: int, res: set):

    # If remaining spaces left to construct permutation string is 0, add prefixStr to set
    if remaining == 0:
        res.add(prefixStr)
    
    # Iterate dictionary
    for curLetter, freq in lettersDict.items():

        # Check if letter's count is greater than 0
        if freq > 0:

            # Reduce frequency, create permutation from new string, then reset frequency
            lettersDict[curLetter] -= 1
            getPermutations(lettersDict, prefixStr + curLetter, remaining - 1, res)
            lettersDict[curLetter] += 1

def perm(s1: str):

    """
    OBJECTIVE: Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have
                duplicates

    Time Complexity: O(n!) where n = length of s1. The permutation formula is n!/(n - r)! where n = total elements and r = number of elements being used. In
                    this case, we'll be using all elements. Counter() is being used to execute the algorithm faster. Imagine if the algorithm in "Permutations
                    Without Duplicates.py" would have behaved with "AAAAAAAAAAAAA". A 13-letter string would have 6 billion permutations. Counter() will
                    list unique letters as keys and values as their frequency in the string.

                    This algorithm is faster than the one being used in the other challenge.

    Space Complexity: O(K + P!) where K = # of keys in dictionary and P! = the number of permutations that can be made from string. A dictionary has to be
                    used for this problem. The dictionary will only hold letters as keys and their number of occurrences as values.

                    P! comes from the permutation formula. Since all letters will be used the denominoator will equal to 1. Anyway, the getPermutations()
                    makes a recursive call per letter in string.
    """

    # If s1 only has 1 letter, return it
    if len(s1) <= 1:
        return set([s1])

    # Only keep unique characters from string
    lettersDict = Counter(s1)
    
    # Create a set to hold output
    res = set()

    # Create all possible permutations
    getPermutations(lettersDict, "", len(s1), res)

    for elem in res:
        print(elem)

perm("aaaaaaab")