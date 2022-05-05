// Cracking the Coding Interview - pp. 90 - q 1.2

class StringPermutations {

    public static void merge(char[] charArray, int leftPtr, int midPtr, int rightPtr) {

        // OBJECTIVE: Create 2 temporary arrays representing each half of the original array, 
        //              then slowly update element's value at index inside of original array

        // Create 2 new arrays
        int sizeA = midPtr - leftPtr + 1;
        int sizeB = rightPtr - midPtr;

        char[] leftHalf = new char[sizeA];
        char[] rightHalf = new char[sizeB];

        // Copy elements from charArray to charA and charB
        for (int i=0; i<leftHalf.length; i++) {
            leftHalf[i] = charArray[leftPtr + i];
        }

        for (int j=0; j<rightHalf.length; j++) {
            rightHalf[j] = charArray[midPtr + 1 + j];
        }

        // Create 3 pointers
        int i = 0, j = 0, k = leftPtr;

        // Traverse original array
        while (i < leftHalf.length && j < rightHalf.length) {

            // If A's element is bigger than B's, put B's first
            if (leftHalf[i] >= rightHalf[j]) {
                charArray[k] = rightHalf[j];
                j++;
            }

            // If B's element is bigger than A's, put A's first
            else {
                charArray[k] = leftHalf[i];
                i++;
            }
            
            // Move pointer inside of original array
            k++;
        }

        // Add remaining elements from A to original array
        while (i < leftHalf.length) {
            charArray[k] = leftHalf[i];
            i++;
            k++;
        }

        // Add remaining elements from B to original array
        while (j < rightHalf.length) {
            charArray[k] = rightHalf[j];
            j++;
            k++;
        }
    }

    public static void mergeSort(char[] charArray, int leftPtr, int rightPtr) {

        // OBJECTIVE: Split array by half until 2 arrays of 1 element each is left, then merge

        if (leftPtr < rightPtr) {

            // Calculate midpoint
            int midPtr = (leftPtr + rightPtr) / 2;
            
            // Slice array by half
            mergeSort(charArray, leftPtr, midPtr);
            mergeSort(charArray, midPtr + 1, rightPtr);

            // merge arrays
            merge(charArray, leftPtr, midPtr, rightPtr);
        }
    }

    public static boolean solOne(String strA, String strB) {

        /*
            OBJECTIVE: Assuming both strings are equal length, check if both strings are permutations of another.
            Time complexity: O(n) where n = the length of both strings. It's assume that both strings share the same length
            Space complexity: O(2n log n + n) where n = length of both strings. Both strings will be sorted (2 * (n log n )) and
                                strA will be traversed (n) to compare against strB.
        */

        // Convert string to char array
        char[] charA = strA.toCharArray();
        char[] charB = strB.toCharArray();

        // Sort arrays
        mergeSort(charA, 0, charA.length - 1);
        mergeSort(charB, 0, charB.length - 1);

        for (int i=0; i<strA.length(); i++) {
            if (charA[i] != charB[i]) {return false;}
        }
        return true;
    }

    public static void main(String args[]) {
        System.out.println(solOne("ABC", "BCA"));
    }
}
