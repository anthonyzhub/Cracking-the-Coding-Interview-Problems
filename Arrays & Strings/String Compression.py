# Cracking the Coding Interview - pp. 91 - q 1.6

class Solution:

    def solOne(self, str1):

        """
            OBJECTIVE: Return a compressed string
            Time complexity: O(n) where n = length of str because algorithm traverses the string
            Space complexity: O(a + n) where a = length of ans and n = length of str. It doesn't matter whether "ans" is smaller (compressed)
                                than "str", "ans" will always be created and the string will be converted to a char array.
        """

        # Base case: If str1 only has 1 character, return itself
        if len(str1) <= 1:
            return str1

        # Create a new string
        ans = ""
        freq = 1

        # Traverse string
        str1_list = list(str1)
        for i in range(1, len(str1_list)):
            
            # If current letter and previous letter is different, update ans string
            if str1_list[i] != str1_list[i - 1]:

                # Add last recording to ans string
                ans += str1_list[i - 1] + str(freq)

                # Update frequency
                freq = 1

            else:

                freq += 1

        # Add last recording
        # NOTE: Recording can stop if for-loop ended
        ans += str1_list[-1] + str(freq)

        # Return shortes string
        if len(str1) > len(ans):
            return ans

        return str1

if __name__ == "__main__":

    sol = Solution()
    print(sol.solOne("aabcccccaaa"))
    print(sol.solOne("abcdeffffffff"))
    print(sol.solOne("abc"))