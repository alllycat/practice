# One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.
'''Task 
Read in two integers, aa and bb, and print three lines. 
The first line is the integer division a//ba//b (Remember to import division from __future__). 
The second line is the result of the modulo operator: a%ba%b. 
The third line prints the divmod of aa and bb.

Input Format 
The first line contains the first integer, aa, and the second line contains the second integer, bb.

Output Format 
Print the result as described above.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

a = int(raw_input())
b = int(raw_input())

print(a//b)
print(a%b)
print(divmod(a,b))

