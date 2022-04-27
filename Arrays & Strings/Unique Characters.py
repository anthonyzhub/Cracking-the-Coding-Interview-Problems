# Cracking the Coding Interview - pp. 90 - q 1.1

class UniqueCharacters:

    def solutionOne(self, str1):

        """
            OBJECTIVE: Use a dictionary to find out if str1 has unique characters
            Time complexity: O(n) where n = length of str1
            Space complexity: O(n) where n = number of keys
        """

        # Create a dictionary
        letters = dict()

        # Traverse string
        for c in str1:

            # If letter already exist inside of dictionary, return false because this is a repeating letter
            if c in letters.keys():
                print(False)
                return

            # Add letter to dictionary
            letters[c] = 1

        print(True)
    
    def solutionTwo(self, str1):

        """
            OBJECTIVE: Use a boolean list to help determine if str1 has unique characters
            Time complexity: O(n) where n = length of str1
            Space complexity: O(1) because list will have a set length of 128, where 128 represents length of ascii alphabet
        """

        # Create a list
        character_set = [False] * 128

        # Traverse string
        for c in str1:

            # Get ascii value of c
            ascii_val = ord(c)

            # If element at index is true, then return false because c is a repeating letter
            if character_set[ascii_val]:
                print(False)
                return

            # Change element to true
            character_set[ascii_val] = True

        print(True)

def main():

    ans = UniqueCharacters()

    # Solution one - My initial solution
    ans.solutionOne("abc")
    ans.solutionOne("hello")

    # Solution two - Book's solution
    ans.solutionTwo("abc")
    ans.solutionTwo("hello")

main()