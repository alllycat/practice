// given a string of any length s and a substring of length k, finds the lexicographically smallest + largest substring of length k

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k = sc.nextInt();
        String max = s.substring(0,k);
        String min = s.substring(0,k);
        
        for (int i=0; i+k<=s.length(); i++){
            
            if (s.substring(i,i+k).compareTo(min) < 0){
                min = s.substring(i,i+k);
            }
            if (s.substring(i,i+k).compareTo(max) > 0){
                max = s.substring(i,i+k);
            }
            }
        System.out.println(min);
        System.out.println(max);
        
        }
    }
