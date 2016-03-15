'''Task 
You have to initialize your list L = [] and follow the N commands given in N lines.

Each command will be 1 of the 8 commands given above. The method extend(L) will not be used. Each command will have its own value(s) separated by a space.

For example:

Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

Sample Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]'''

L = []
L.insert(0,5)
L.insert(1,10)
L.insert(0,6)
print(L)
L.remove(6)
L.append(9)
L.append(1)
L.sort()
print(L)
L.pop()
L.reverse()
print(L)

