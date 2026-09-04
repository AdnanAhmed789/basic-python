number = [3.4,3,"value","in sequence"]
print(number)
print(number[0])
print(number[0 : 2])
number[0] = "tuo"
print(number)
number.append(509)
print(number)
jack = [2,3,1,8,4,10]
jack.reverse()
print(jack)
jack.sort()
print(jack)
jack.sort(reverse = True)
print(jack)
jack.insert(2,"add")
print(jack)
jack.remove("add")
print(jack )
jack.pop(2)
print(jack)
you = [1,3,2,4,9]
print(you)
get = (input("Enter some number that will added to list"))
print(len(get))
print(you[0])
print(you[4])
you.append(3)
print(you)
you.insert(3,5)
print(you)
you.remove(4)
print(you)
print(len(you))
you.pop(2)
print(you)
check = [6,5,4,8,9,3]
check.sort()
print(check)
list1 = [2,1,4,2,6,3]
list2 = [3,2,7,4,9]
merged = list1 + list2
print(merged)
print(merged.count(3))
take  = [1,2,2,3,4,5,6,8,7]
mid = len(take)//2
list_2 = take[mid:]
list_1 = take[:mid]
print("list 1 =",list_1)
print("list 2 =",list_2)