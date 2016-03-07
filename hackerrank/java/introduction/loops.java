import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for (int i=0; i<t; i++){
            
            if (t>=0 && t<=500){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            
            if (a>=0 && b<=50 && n>=1 && n<=15){
                
                for (int j=0; j<n; j++){ //format: for(initialization; Boolean_expression; update)
                a = a + (int)((Math.pow(2,j))*b); // Math.pow returned a double, converted to int with (int)
                    // 2^j IS NOT "2 to the power of j" -- exponentiation is done using the math library (import java.math.*;)
                
                System.out.print(a + " "); //prints results in one line
            }
                System.out.println();
                
        }
            
            }
            
            
            
        }
    }
}
