#Lists

Lists in Python are very versatile. You can add almost anything in a Python list.

In Python, you can create a list of any objects: strings, integers, or even lists. You can even add multiple types in a single list!

Let's look at some of the methods you can use on list.

###1.) append(x) 
Adds a single element ′x′′x′ to the end of a list.

```python
>>> arr.append(9)   
>>> print arr  
[1, 2, 3, 9]
```

###2.) extend(L) 
Merges another list ′L′′L′ to the end.

```python
>>> arr.extend([10,11])
>>> print arr
[1, 2, 3, 9, 10, 11]
```

###3.) insert(i,x) 
Inserts element ′x′′x′ at position ′i′′i′.

```python
>>> arr.insert(3,7)
>>> print arr
[1, 2, 3, 7, 9, 10, 11]
```

###4.) remove(x) 
Removes the first occurrence of element ′x′′x′.

```python
>>> arr.remove(10)  
>>> arr  
[1, 2, 3, 7, 9, 11]
```

###5.) pop() 
Removes the last element of a list. If an argument is passed, that index item is popped out.

```python
>>> temp = arr.pop()
>>> print temp 
11
```

###6.) index(x) 
Returns the first index of a value in the list. Throws an error if it's not found.

```python
>>> temp = arr.index(3)
>>> print temp
2
```

###7.) count(x) 
Counts the number of occurrences of an element ′x′′x′.

```python
>>> temp = arr.count(1)
>>> print temp
1
```

###8.) sort() 
Sorts the list.

```python
>>> arr.sort()
>>> print arr
[1, 2, 3, 7, 9]
```

###9.) reverse() 
Reverses the list.

```python
>>> arr.reverse()
>>> print arr
[9, 7, 3, 2, 1]
```
