//exploring length(), compareTo(), substring(), toUppercase()

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        
        // prints summed length of string A and B
        System.out.println(A.length() + B.length());
        
        // determines if string A is lexicographically larger than B (does B come before A in the dictionary?)
        if(A.compareTo(B) > 0){ // method compareTo compares two strings lexicographically
            // compareTo: returns 0 if lexicographically equal, > 0 if larger, < 0 if smaller
            System.out.println("Yes");
        } 
        else {
            System.out.println("No");
        }
        
        // Prints capatalized strings A and B (first letter of string A and B), printing out both separated by a space
        // use SUBSTRINGS:  method that returns a new string that is a substring of this string
        // substring begins with the character at the specified index and extends to the end of this string or up to endIndex - 1            if second argument is given.
   
        A = (A.substring(0,1)).toUpperCase() + A.substring(1); // concatenates uppercase substring of first character + rest of string   
        B = (B.substring(0,1)).toUpperCase() + B.substring(1);
        System.out.println(A + " " + B);   
        
        
    }
}
