// INCOMPLETE 

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for (int i=0; i<t; i++){
            
            if (t>=1 && t<=Math.pow(10, 5)){
            int n = sc.nextInt();
            
            if (n>=1 && n<=Math.pow(10, 3)){
                int sum = 0;
		        for (int j = 0; j < 1000; j++) 
			         if (n % 3 == 0 || n % 5 == 0){
                        sum += n;  
                }
				System.out.println(sum);
            }

                
            }
            
    }
}
}
