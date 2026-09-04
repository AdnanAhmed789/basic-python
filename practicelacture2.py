ghi = "It's the book\n"
print(ghi)
print(type(ghi))
ypu = "his book is good, \nand you are my best friend"
print(ypu)
print(ghi+ypu)
print(len(ghi))
print(ghi[1])
print(ghi[1:4])
print(ghi[0:len(ghi)])
print(ghi[:4])
print(ghi[5:])
print(len(ypu))
ok = "i love climbing"
print(ok.endswith("kjhuh"))
print(ok.capitalize())
print(ok.replace("g","i"))
print(ok.find("o"))
print(ok.count("i"))
you = input("Write something :")
print(len(you))
hi = "ahfhj$$$$$$"
print(hi.count("$"))
marks = int(input("Enter marks"))
if(marks>=90):
    print("Grade = A")
elif(marks>=80 and marks<90):
    print("Grade = B")
elif(marks>=70 and marks<80):
    print("Grade = C")
else:
    print("Fail")
jack = int(input("Enter number"))
if(jack%2==0):
    print("even")
else:
    print("odd")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c= "))
if(a>b and a>c):
    print("a is greater")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")
d = int(input("Enter number"))
if(d%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")