a = int(input("Write value for a"))
b = int(input("Write value for b"))
print(a+b)
print("Hello World")
num = 169
num = num**(1/2)
print(num)
length = 3
width = 4
area = 1/2*(length * width)
print(area)
x = 5
y = 6
print("value of x is : ",x)
print("value of y is : ",y)
swap = x
print("swap = ",swap)
print("x = ",x)
x = y
print("x = ",x)
y = swap
print("y = ",y)
# swap value without using third value
s = 8
h = 7
s,h = h,s
print("value of s is  ",s)
print("value of h is  ",h)
subjects = ['python','C','Java']
print(subjects )
print(subjects[0])
subjects[0] = "jesfd"
print(subjects)
print(len(subjects))
print(subjects[:3])
subjects.append("C++")
print(subjects)
subjects.sort()
print(subjects)
subjects.sort(reverse = True)
print(subjects)
subjects.reverse()
print(subjects)
subjects.insert(1,"C++")
print(subjects)
subjects.remove('C')
print(subjects)
subjects.pop(2)
print(subjects)
#Tuples
num = (1,2,3,4,)
print(num[2])
print(num)
list = [1,2,3,2,1,4,]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("Palindrom")
else:
    print("not palindrom")
movies = []
mov1 = input("Enter mov1 name")
mov2 = input("Enter mov2 name")
mov3 = input("Enter mov3 name")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)