// Cracking the Coding Interview - pp. 91 - q 1.6

public class StringCompression {
    
    public static String solOne(String str) {
    
        /*
            OBJECTIVE: Return a compressed string
            Time complexity: O(n) where n = length of str because algorithm traverses the string
            Space complexity: O(a + n) where a = length of ans and n = length of str. It doesn't matter whether "ans" is smaller (compressed)
                                than "str", "ans" will always be created and the string will be converted to a char array.
        */

        // If str only has one character, return it
        if (str.length() <= 1) {return str;}

        // Create a variable to hold answer and letter frequency
        StringBuilder ans = new StringBuilder();
        int freq = 1;

        // Traverse string
        char[] str_array = str.toCharArray();
        for (int i=1; i<str_array.length; i++) {

            // If current letter is different from previous, update ans string
            if (str_array[i] != str_array[i - 1]) {

                // Update ans and counter
                ans.append(str_array[i - 1]);
                ans.append(Integer.toString(freq));

                freq = 1;
            }
            else {
                freq++;
            }
        }

        // Add stopped recording to ans
        // NOTE: Recording could be stopped when for-loop ends
        ans.append(str_array[str_array.length - 1]);
        ans.append(Integer.toString(freq));

        // Return shortest string
        if (str.length() > ans.length()) {return ans.toString();}

        return str;
    }    

    public static void main(String[] args) {

        System.out.println(solOne("aabcccccaaa"));
        System.out.println(solOne("abcdeffffffff"));
        System.out.println(solOne("abc"));
    }

}
