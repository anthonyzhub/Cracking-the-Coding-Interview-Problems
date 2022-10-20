// Cracking the Coding Interview - pp. 134 - q. 8.1

import java.util.*;

public class TripleStep {
    
    int stepsHelper(int nth, int[] res) {

        // If n is less than 0, return 0
        if (nth < 0) {
            return 0;
        }

        else if (nth == 0) {
            return 1;
        }

        else if (res[nth] > -1) {
            return res[nth];
        }

        else {

            // Make a recursive call and save output to memo
            res[nth] = stepsHelper(nth - 1, res) + stepsHelper(nth - 2, res) + stepsHelper(nth - 3, res);

            return res[nth];
        }
    }

    void steps(int stairs) {

        /*
         * OBJECTIVE: Calculate how many ways there are to reach n steps
         * 
         * Time Complexity: O(1) because no looping was used in this algorithm
         * 
         * Space Complexity: O(n) where n = steps because stepHelper() is making recursive calls, so each call adds on to
         *                      the memory stack. Also, if the execution was outlined as a tree, the tree's height is n levels tall.
         */

        // Create an array filled with -1's
        int[] res = new int[stairs + 1];
        Arrays.fill(res, -1);

        // Create all possibilities
        stepsHelper(stairs, res);

        for (int i: res) {
            System.out.printf("%d ", i);
        }
    }
}
