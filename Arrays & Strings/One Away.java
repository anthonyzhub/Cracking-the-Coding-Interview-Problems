class OneAway {

    public static boolean replaceOneLetter(String str1, String str2) {

        // OBJECTIVE: Traverse strings and flag when one edit is made

        // Change both strings into a char array
        char[] str1_array = str1.toCharArray();
        char[] str2_array = str2.toCharArray();

        // Traverse array
        boolean madeAnEdit = false;
        for (int i=0; i<str1_array.length; i++) {

            // If both letters don't match
            if (str1_array[i] != str2_array[i]) {

                // If an edit has already been made, return false
                // NOTE: At most 1 edit can be made
                if (madeAnEdit) {
                    return false;
                }

                // If not, set variable to true
                madeAnEdit = true;
            }
        }

        // If for-loop ended, return true
        return true;
    }

    public static boolean deleteOrAdd(String smallStr, String bigStr) {

        // OBJECTIVE: Traverse both strings and flag when a letter needs to be added or deleted from either strings

        // Change both strings to an array
        char[] smallArray = smallStr.toCharArray();
        char[] bigArray = bigStr.toCharArray();

        // Traverse both arrays
        int smallIdx = 0;
        int bigIdx = 0;
        boolean madeAnEdit = false;

        while (smallIdx < smallArray.length && bigIdx < bigArray.length) {

            // If both letters don't match
            if (smallArray[smallIdx] != bigArray[bigIdx]) {

                // If an edit has already been made, return false
                if (madeAnEdit) {return false;}

                // If not, move bigIdx by 1 and update boolean variable
                // E.g., ple & pale
                bigIdx++;
                madeAnEdit = true;

                continue;
            }

            // Update pointers
            smallIdx++;
            bigIdx++;
        }

        // If while-loop ended, return true
        return true;
    }

    public static boolean solOne(String str1, String str2) {
        
        /*
            OBJECTIVE: Check if both strings are the same with at-most 1 edit permitted (replace, drop, or insert a letter)
            
            Time complexity: O(n) where n = length of either string if replaceOneLetter() is executed. If deleteOrAdd() is
                            executed instead, then O(b) where b = length of bigger string because bigIdx can move 1 index more
                            than smallIdx if a mismatched letter is found
            
            Space complexity: O(n) where n = length of either string if replaceOneLetter() is executed because 2 new lists are
                            created. In deleteOrAdd(), it will be O(S + B) where S = length of small string and B = length of
                            big string because 2 new lists are created for each string.
        */

        // If both strings are different in length by 2, return false
        if (Math.abs(str1.length() - str2.length()) >= 2) {
            return false;
        }

        // If both strings share the same length, check if 1 letter needs to be changed
        if (str1.length() == str2.length()) {
            return replaceOneLetter(str1, str2);
        }

        // If str1 is bigger by 1 character
        else if (str1.length() > str2.length()) {
            return deleteOrAdd(str2, str1);
        }

        // If str1 is smaller by 1 character
        else {
            return deleteOrAdd(str1, str2);
        }
    }

    public static void main(String args[]) {

        System.out.println(solOne("pale", "ple"));
        System.out.println(solOne("pales", "pale"));
        System.out.println(solOne("pale", "bale"));
        System.out.println(solOne("pale", "bake"));
    }
}