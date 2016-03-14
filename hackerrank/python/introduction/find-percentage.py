# UNFINISHED

'''Concept
A dictionary is a data type which stores values in pairs. For each element in the dictionary, there is a unique key that points to a value. A dictionary is mutable. It can be changed. 
For example:
>> a = {'one': 1} # Here 'one' is the key. 

Task
You have a record of NN students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer NN followed by the names and marks for NN students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer NN, the number of students. The next NN lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.'''

a = int(input())
studentInfo = input() 
myDict = {}

for i in range(a): 
    infoArray = studentInfo.split(" ") 
    summedScores = float(infoArray[1]) + float(infoArray[2]) + float(infoArray[3]) 
    avgScore = float(summedScores/3)
    myDict[studentInfo[0]] = avg
    e = input()
    
print(myDict[e])
