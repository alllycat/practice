import java.util.*;
import java.io.*;
class Solution{
public static void main(String []argh)
{
    Scanner sc = new Scanner(System.in);
    int t=sc.nextInt();

    for(int i=0;i<t;i++)
    {

        try
        {
            long x=sc.nextLong();
            System.out.println(x+" can be fitted in:");
            if(x>=(long)-128 && x<=(long)127)System.out.println("* byte");
            if(x>=(long)Short.MIN_VALUE && x<=(long)Short.MAX_VALUE)System.out.println("* short");
            if(x>=(long)Integer.MIN_VALUE && x<=(long)Integer.MAX_VALUE)System.out.println("* int");
            if(x>=(long)Long.MIN_VALUE && x<=(long)Long.MAX_VALUE)System.out.println("* long");
            // all ifs and no "else-ifs", because you want it to print out all possible cases in order 
                // use MIN/MAX_VALUE instead of Math.pow because of inconsistent behaviour of primitive types in java
                // when the cast occurs maybe you can lose some information
        }
        catch(Exception e)
        {
            System.out.println(sc.next()+" can't be fitted anywhere.");
        }

    }
}
}
