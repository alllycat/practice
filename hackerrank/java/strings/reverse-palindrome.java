// Given a string AA, print "Yes" if it is a palindrome, print "No" otherwise. 
// The strings will consist lower case english letters only. The strings will have at most 50 characters

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        int len = A.length();
        String reversedString = "";
        
        for (int i=len-1; i>=0; i--){
            reversedString = reversedString + A.charAt(i);
        } 
        
        System.out.println((A.equals(reversedString) ? "Yes" : "No")); //one-liner that compares strings and prints out result (like if/else)
        }
        
    }
