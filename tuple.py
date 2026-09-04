tup =  (2,3,4,6,4,) 
print(tup)
print(type(tup))
print(tup[2])
# tup[0]=3 not allowed in python
# Tuple is immutable
tuple = (5,)
print(type(tuple))
print(tup[1:4])
print(tup.index(4))
print(tup.count(4))
movies = []
mov1 = input(" Write movie1 name")
mov2 = input("Write movie2 name")
mov3 = input("Write movie3 name")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
# Palindrom list
list = [1,3,5,3,1,]

copy_list = list.copy()
print(copy_list)
copy_list.reverse()

if(copy_list == list):
    print("list is palindrom")
else:
    print("list is not palindrom")
Grades = ("C","D","A","A","B","B","A")
print(Grades)
print(Grades.count("A"))
jack = ["C","D","A","A","B","B","A"]
jack.sort()
print(jack)
a = 25
a = a**(1/2)
print(a)
l = 4
w = 5
area = 1/2*(l*w)
print(area)
c = 5
d = 8
print("c => ",c ,"d => ",d)
f = c
# c = d
d = f
print("c  =>",c)
print("d =>",d)
c,d = d,c
print("c = ",c,"d = ",d)
distance = 55
miles = 0.621*distance
print(miles)
import random
num = random.randint(1,10)
print(num)
fruit = ["apple","mango","bannana","rice"]
duf = random.choice(fruit)
print(duf)
fud = random.random()
print(fud)
h = -3
if(h >= 0):
    print( h , " => h is positive\n ")
else:
    print(h , " => h is negative ")
year = 2003
if(year % 4 == 0  and year % 100 != 0) or (year % 400 ==0 and year % 100 ==0):
    print(year," is a Leap year ")
else:
    print(year,"* is not a leap year")

