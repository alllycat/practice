'''power --> pow(a,b) or a**b
It's also possible to calculate a*b mod m --> pow(a,b,m)

This is very helpful in computations where you have to print the resultant % mod.

Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.
Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking, we will never use math.pow().

Task 
You are given three integers: aa, bb, and mm, respectively. Print two lines. 
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

print(pow(a,b))
print(pow(a,b,m))
