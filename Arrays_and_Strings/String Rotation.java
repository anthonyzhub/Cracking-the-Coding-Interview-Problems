// Cracking the Coding Interview - pp. 91 - q 1.9

import java.util.ArrayList;

class StringRotation {

    public static ArrayList<Character> toArrayList(String str1) {
        
        // OBJECTIVE: Convert a string to an ArrayList

        // Create a new array
        ArrayList<Character> ans = new ArrayList<Character>();

        // Traverse string
        for (int i=0; i<str1.length(); i++) {
            ans.add(str1.charAt(i));
        }

        return ans;
    }
    
    public static boolean solOne(String str1, String str2) {

        /*
            OBJECTIVE: Rotate either string until both matches (e.g., erbottlewat == waterbottle).
                        This is a permutation problem.

            Time complexity: O(n) where n = length of either string since they both are the same. 

            Space complexity: O(n) where n = the size of the array lists.
        */

        // If both strings aren't equal in length, return false
        if (str1.length() != str2.length()) {return false;}

        // Turn both strings into lists
        ArrayList<Character> str1_list = toArrayList(str1);
        ArrayList<Character> str2_list = toArrayList(str2);

        // Traverse both strings
        for (int i=0; i<str1_list.size(); i++) {

            // If both letters don't match, pop element from str1_array and append it
            if (str1_list.get(0) != str2_list.get(0)) {

                // Pop element and add it again
                char tmp = str1_list.remove(0);
                str1_list.add(tmp);
            }
        }

        // Compare both lists
        return str1_list.equals(str2_list);
    }

    public static void main(String[] args) {
        System.out.println(solOne("erbottlewat", "waterbottle"));
    }
}
