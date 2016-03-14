'''
Concept
A tuple is similar to a list. However, a tuple is immutable. It cannot be changed. Once you assign some value to a tuple, it cannot be changed. Also, no additional members can be added once a tuple is assigned.

Task
You are given two integers. Store them into two variables and then exchange them. Rather than using any fancy logic, make sure to use a tuple to do the task. Print the two numbers.

Input Format

Two integers on separate lines.

Output Format

Two integers on separate lines.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input())
b = int(raw_input())
tuple = (a,b)

print(tuple[1])
print(tuple[0])

