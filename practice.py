a = int(input("write value for a :"))
b = int(input("write another, value for b :"))
sum = (a + b)
print("sum is => ",sum)
side = float(input(" Enter value for side => "))
area = side * side
print("area => ",area)
g = int (input("Enter value for g => "))
s = int (input("Enter value for s => "))
print("g>=s => ",g>=s)
d = input("Enter name of movie 1 => ")
h = input("Enter name of movie 2 => ")
j = input("Enter name of movie 3 => ")
list = [d,h,j]
print(list)
name = [1,2,4,2,1]
name_1 = name.copy()
print(name)
name.reverse()
if(name == name_1):
    print("palindrom")
else:
    print("not palindrom")
"""
WAP to count the number of students with the "A"  grade
in the following tuple.
"""
lsit = ["C","D","A","A","B","B","A"]
print(lsit.count("A"))
lsit.sort()
print(lsit)
dic = {
    "subject" : {
        "physics" : 30,
        "English" : 90,
        "Science" : 67
    },
    "department": {
        "tup" : (1,2,3,2,1),
        "list" : [1,3,4,5]
    },
    "university" : "University of Sindh"
}
print(dic)
import pprint
pprint.pprint(dic)
