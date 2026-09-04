marks = int(input(" marks = "))

if(marks>=90):
    grade = "A"
    if(marks>=95):
        grade = "A+"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "fail"

print("grade = ",grade)

num = int(input("number = "))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")
a = 34
b = 43 
c = 45
if(a>=b and a>=c):
    print("a is greater")
elif(b>=c):
    print("b is greater ")
else:
    print(" c is greater")
d = int(input("enter number"))
if(d%7==0):
    print("multiplr by 7")
else:
    print("not multiple by 7")