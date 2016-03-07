//end of file exercise

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lineNumber = 1; // starts at one
        while (sc.hasNext()){ // returns true if this scanner (sc) has another token in its input
            String readLine = sc.nextLine(); // sets readLine to the next string line
            System.out.println(lineNumber + " " + readLine); 
            lineNumber++; // increments lineNumber by one
        }
    }
}
