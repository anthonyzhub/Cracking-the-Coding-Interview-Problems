// Cracking the Coding Interview - pp. 90 - q 1.3

public class URLify {
    
    public static String solOne(String str) {

        // OBJECTIVE: Replace all whitespace with "%20" and return string

        // Remove duplicate whitespaces with replaceAll()
        // Then, remove leading and trailing whitespaces with trim()
        String trimmed = str.replaceAll("\\s+", " ").trim();

        // Traverse string
        StringBuilder ans = new StringBuilder();
        for (char c: trimmed.toCharArray()) {

            // Replace whitespace with "%20"
            if (c == ' ') {
                ans.append("%20");
            }
            else {
                ans.append(c);
            }
        }

        // Return StringBuilder as a string
        return ans.toString();
    }

    public static void main(String args[]) {
        System.out.println(solOne("   John Smith   "));
    }
}
