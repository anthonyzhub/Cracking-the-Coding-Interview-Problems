class Solution:

    def replaceOneLetter(self, str1, str2):

        # OBJECTIVE: Traverse strings and flag when one edit is made

        # Change string to a list
        str1_list = list(str1)
        str2_list = list(str2)

        # Traverse string
        madeAnEdit = False
        for idx in range(len(str1_list)):

            # If both letters don't match
            if str1_list[idx] != str2_list[idx]:

                # If an edit has already been made, return False
                if madeAnEdit:
                    return False

                # If not, update boolean variable
                madeAnEdit = True

        # If the for-loop ended, then both strings are only different by 1 edit
        return True

    def deleteOrAdd(self, smallStr, bigStr):

        # OBJECTIVE: Traverse both strings and flag when a letter needs to be added or deleted from either strings

        # Change string to a list
        smallStr_List = list(smallStr)
        bigStr_List = list(bigStr)

        # Traverse both lists
        smallIdx = 0
        bigIdx = 0
        madeAnEdit = False
        while smallIdx < len(smallStr_List) and bigIdx < len(bigStr_List):

            # If both letters don't match
            if smallStr_List[smallIdx] != bigStr_List[bigIdx]:

                # If a change has already been made, then return false
                if madeAnEdit:
                    return False

                # If this is the first edit, move bigIdx by 1 and update boolean variable
                # E.g., ple & pale
                bigIdx += 1
                madeAnEdit = True

                continue

            smallIdx += 1
            bigIdx += 1

        return True

    def solOne(self, str1, str2):
        
        # If both strings are different in length by 2, then return false
        # E.g., bake & bakery
        if abs(len(str1) - len(str2)) >= 2: # <= Add abs() because wasn't sure which stirng is bigger
            return False

        # If both strings share the same length, check if one letter needs to be change in either strings
        if len(str1) == len(str2):
            return self.replaceOneLetter(str1, str2)

        # If str1 is bigger by 1 character
        elif len(str1) > len(str2):
            return self.deleteOrAdd(str2, str1)

        # If str2 is shorter by 1 character
        elif len(str1) < len(str2):
            return self.deleteOrAdd(str1, str2)

sol = Solution()
print(sol.solOne("pale", "ple"))
print(sol.solOne("pales", "pale"))
print(sol.solOne("pale", "bale"))
print(sol.solOne("pale", "bake"))