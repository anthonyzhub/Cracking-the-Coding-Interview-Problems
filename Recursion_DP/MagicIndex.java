// Cracking the Coding Interview - pp. 135 - q. 8.3
package Recursion_DP.Java
public class MagicIndex {
    
    static int binarySearch(int[] magic, int leftPtr, int rightPtr) {

        if (leftPtr <= rightPtr) {

            // Create mid pointer
            int midPtr = (int) (leftPtr + rightPtr) / 2;

            // If element at midPtr equals to midPtr, return index
            if (magic[midPtr] == midPtr) {
                return midPtr;
            }

            // If element at midPtr is greater than midPtr, search left half of array
            else if (magic[midPtr] > midPtr) {
                return binarySearch(magic, leftPtr, midPtr - 1);
            }

            // If element at midPtr is smaller than midPtr, search right half of array
            else {
                return binarySearch(magic, midPtr + 1, rightPtr);
            }
        }
        return -1;
    }

    static int magic(int[] magic) {

        // If magic is empty, return -1
        if (magic.length == 0) {return -1;}

        return binarySearch(magic, 0, magic.length - 1);
    }

    public static void main(String[] args) {
        
        int[] magicArray = {0, 5, 4, 1, 2, 3};
        // int[] magicArray = {4, 1, 0, 3, 5, 2};
        // int[] magicArray = {0, 1, 2, 3, 4, 5};

        System.out.println(magic(magicArray));
    }
}