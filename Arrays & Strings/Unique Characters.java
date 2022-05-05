// Cracking the Coding Interview - pp. 90 - q 1.1

import java.util.HashMap;

class UniqueCharacters {

    public static void solutionOne(String str) {

        /*
            OBJECTIVE: Use a hash map to count frequnecy of characters
            Time complexity: O(n) where n = string length
            Space complexity: O(k) where k = number of keys
        */

        // If str is longer than 128-alphabet, then they are repeat characters
        // NOTE: We're assuming that str has ascii characters which there is a total of 128
        if (str.length() > 128) {
            System.out.println(false);
            return;
        }

        // Create a hash map
        HashMap<Character, Integer> letters = new HashMap<Character, Integer>();

        // Traverse string
        for (int i=0; i<str.length(); i++) {

            // If key exists, return false
            if (letters.containsKey(str.charAt(i))) {
                System.out.println(false);
                return;
            }

            // Add new letter to hash map
            letters.put(str.charAt(i), 1);
        }

        System.out.println(true);
    }

    public static void solutionTwo(String str) {

        /*
            OBJECTIVE: Use a boolean array to find out if str has unique characters
            Time complexity: O(n) where n = length of string
            Space complexity: O(1) because arrays that are being used have a definite size
        */

        // Create a boolean array
        boolean[] character_set = new boolean[128];

        // Traverse string
        for (int i=0; i<str.length(); i++) {

            // Get ascii value of character
            // NOTE: charAt() returns a character, but ascii_val is an integer type, so character will change to integer
            int ascii_val = str.charAt(i);

            // If index has an element, return false because this is a repeating character
            if (character_set[ascii_val]) {
                System.out.println(false);
                return;
            }

            // Add "true" to index in array
            character_set[ascii_val] = true;
        }

        System.out.println(true);
    }

    public static void main(String[] args) {
        
        // Solution one - hash map && my first solution
        solutionOne("abc");
        solutionOne("hello");

        // Solution two - boolean array && book's first solution
        solutionTwo("abc");
        solutionTwo("hello");
    }
}