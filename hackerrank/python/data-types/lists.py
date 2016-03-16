# assumes user does not mistype a command
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

# The method strip() returns a copy of the string in which all chars have been stripped from the beginning and the end of the string 
# (default whitespace characters)

T = int(raw_input().strip())

L = []
for t in range(T):
    args = raw_input().strip().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print L
        
#OR, use getattr(Object, Function)(Vars) - replicate the ability to call a function via a name stored in a variable

T = int(raw_input().strip())
L = []
for t in range(T):
    args = raw_input().strip().split(" ")
    if args[0] == "print":
        print L
    elif len(args) == 3:
        getattr(L, args[0])(int(args[1]), int(args[2]))
    elif len(args) == 2:
        getattr(L, args[0])(int(args[1]))
    else:
        getattr(L, args[0])()

