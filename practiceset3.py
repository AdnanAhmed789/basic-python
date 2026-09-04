a = int(input("Write value for a"))

if(a%8==0):
    print(a," is divided by 8")
else:
    print(a," is not divided by 8 ")

if(a%9==0):
    print("this number is divided by ",a," This number")
else:
    print("this number is not divided by ",a," This number")
"""
list are built-in data type and store set of values
It can store value of different data types
list are mutable
"""
marks = [34,50,67,45,33,23]
print(marks[3])
print(marks)
print(type(marks))
print(len(marks))
marks[3] = 67 #List are mutable
print(marks) 
str = "Adnan"
print(str)
# str[1] = "c"  string is immutable
print(str)
print(marks[1:4]) #Slicing
print(marks[-4:-1])
# Methods in python
marks.append(42)
print(marks)
print(marks.append(32))# not return something
marks.sort()
print(marks)
marks.sort(reverse = True)
print(marks)
marks.reverse()
print(marks)
str = ["Adnan","siddique","Waseem","Badal"]
str.sort()
print(str)
str.sort(reverse = True)
print(str)
str.reverse()
print(str)
list = [1,2,3,4,5]
list.insert(0, 7)
print(list)
list.remove(7)
print(list)
list.pop(0)
print(list)
list[2] = 9 # Allowed in python
print(list) 