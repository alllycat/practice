#Lists

Lists in Python are very versatile. You can add almost anything in a Python list.

In Python, you can create a list of any objects: strings, integers, or even lists. You can even add multiple types in a single list!

Let's look at some of the methods you can use on list.

####1.) append(x) 
Adds a single element ′x′′x′ to the end of a list.

```python
>>> arr.append(9)   
>>> print arr  
[1, 2, 3, 9]
```

####2.) extend(L) 
Merges another list ′L′′L′ to the end.

```python
>>> arr.extend([10,11])
>>> print arr
[1, 2, 3, 9, 10, 11]
```

####3.) insert(i,x) 
Inserts element ′x′′x′ at position ′i′′i′.

```python
>>> arr.insert(3,7)
>>> print arr
[1, 2, 3, 7, 9, 10, 11]
```

####4.) remove(x) 
Removes the first occurrence of element ′x′′x′.

```python
>>> arr.remove(10)  
>>> arr  
[1, 2, 3, 7, 9, 11]
```

####5.) pop() 
Removes the last element of a list. If an argument is passed, that index item is popped out.

```python
>>> temp = arr.pop()
>>> print temp 
11
```

####6.) index(x) 
Returns the first index of a value in the list. Throws an error if it's not found.

```python
>>> temp = arr.index(3)
>>> print temp
2
```

####7.) count(x) 
Counts the number of occurrences of an element ′x′′x′.

```python
>>> temp = arr.count(1)
>>> print temp
1
```

####8.) sort() 
Sorts the list.

```python
>>> arr.sort()
>>> print arr
[1, 2, 3, 7, 9]
```

####9.) reverse() 
Reverses the list.

```python
>>> arr.reverse()
>>> print arr
[9, 7, 3, 2, 1]
```
##Functional Programming Tools for Lists

There are three built-in functions that are very useful when used with lists: **filter(), map(),** and **reduce()**.

####1.) filter(function, sequence) 
returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list. For example, to compute a sequence of numbers divisible by 3 or 5:

```python
>>>
>>> def f(x): return x % 3 == 0 or x % 5 == 0
...
>>> filter(f, range(2, 25))
[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
```


####2.) map(function, sequence) 
calls function(item) for each of the sequence’s items and returns a list of the return values. For example, to compute some cubes:

```python
>>>
>>> def cube(x): return x*x*x
...
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

More than one sequence may be passed; the function must then have as many arguments as there are sequences and is called with the corresponding item from each sequence (or None if some sequence is shorter than another). For example:

```python
>>>
>>> seq = range(8)
>>> def add(x, y): return x+y
...
>>> map(add, seq, seq)
[0, 2, 4, 6, 8, 10, 12, 14]
```


####3.) reduce(function, sequence) 
returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. For example, to compute the sum of the numbers 1 through 10:

```python
>>>
>>> def add(x,y): return x+y
...
>>> reduce(add, range(1, 11))
55
```

If there’s only one item in the sequence, its value is returned; if the sequence is empty, an exception is raised.

A third argument can be passed to indicate the starting value. In this case the starting value is returned for an empty sequence, and the function is first applied to the starting value and the first sequence item, then to the result and the next item, and so on. For example,

```python
>>>
>>> def sum(seq):
...     def add(x,y): return x+y
...     return reduce(add, seq, 0)
...
>>> sum(range(1, 11))
55
>>> sum([])
0
```
* Don’t use this example’s definition of sum(): since summing numbers is such a common need, a built-in function sum(sequence) is already provided, and works exactly like this.

#Tuples

**Tuples** are a data structure like a list. The main difference is that tuples are *immutable*. Once created, tuples cannot be modified. This restricts their use because we cannot add, remove, or assign values. However, it gives us an advantage in space and time complexities.

A common tuple use is swapping two numbers:

```python
a,b = b,a 
```

* Here **a,b** is a tuple, and it assigns itself the values of **b,a**.

Another awesome use of tuples is *as keys in a dictionary*. In other words, *tuples are _hashable_*.
