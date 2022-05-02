# Cracking the Coding Interview - pp. 90 - q 1.3

class URLify:

    def solOne(self, str1):

        """
            OBJECTIVE: Replace all whitespace with "%20" and return string
            Time complexity: O(2n) where n = length of string. String is traversed twice in replace() and by my for-loop
            Space complexity: O(2n) where n = length of string. String is converted to a list for the for-loop and traversed again to
                                convert back to a string.
        """

        # Replace all duplicate whitespace with a singular one
        str1 = str1.replace("  ", " ")

        # Remove leading and trailing whitespaces
        str1 = str1.strip()

        # Convert string to a list
        str1 = list(str1)

        # Traverse string
        for i in range(len(str1)):

            if str1[i] == " ":
                str1[i] = "%20"

        # Return list as string
        return "".join(i for i in str1)

def main():

    ans = URLify()
    print(ans.solOne("  John Smith  "))

main()