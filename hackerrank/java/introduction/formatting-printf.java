import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt();
                System.out.printf("%-15s%03d%n", s1, x); //prints 2 columns
                // %-15s = Each String is left-justified with trailing whitespace through the first 15 characters, leading digit of the integer is the 16th character
                // %03d = each integer that was less than 33 digits now has leading zeroes
                // %n = By using %n in your format string, you tell Java to use the value returned by System.getProperty("line.separator")
            }
            System.out.println("================================");

    }
}
