# Cracking the Coding Interview - pp. 91 - q 1.9

class Solution:

    def solOne(self, str1, str2):

        # OBJECTIVE: Rotate either string until they both look the same (erbottlewat == waterbottle)
        # NOTE: This is a permutation problem:

        """
        bottlewater == ber                    rbottlewate
                            bottlewater
                            ottlewaterb
                            ttlewaterbo
                            tlewaterbot
                            lewaterbott
                            ewaterbottl
                            waterbottle
        """

        # If both strings aren't equal in length, exit function
        if len(str1) != len(str2):
            return False

        # Turn both strings into a list
        str1_list = list(str1)
        str2_list = list(str2)

        # Traverse str1
        for _ in range(len(str1_list)):

            # If both letters don't match, pop letter from str1 and append it
            if str1_list[0] != str2_list[0]:

                # Pop element and add it at the back
                tmp = str1_list.pop(0)
                str1_list.append(tmp)

        return str1_list == str2_list

def main():

    sol = Solution()
    print(sol.solOne("erbottlewat", "waterbottle"))

main()