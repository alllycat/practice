#two types of loops in python: for, while

'''Task 
Read an integer N. For all non-negative integers i<N, print i2. See the sample for details.

Input Format 
The first and only line contains the integer, N.

Constraints 
1≤N≤20

Output Format 
Print N lines, one corresponding to each i.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
i=0
for i in range(0,N):
    print(pow(i,2))

#OR

while i<N:
    print(pow(i,2))
    i+=1
