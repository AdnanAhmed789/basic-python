# set are unordered.
# These are immutable

yet = {23,44,6,2,2}
print(yet)
print("yet is type ")
print(type(yet))
#empty set
tes = set()
print("tes is type")
print(type(tes))
"""
set is mutable
elements of set are immutabe
add method
"""
tes.add(1)
tes.add(55)
print(tes)
# remove method
yet.remove(44)
print(yet)
tes.add("string")
print(tes)
yet.clear()
print(len(yet))
# pop method
collection = {"adnan","your choice","win"}
print(collection.pop())
set1 = {3,3,4,6,7}
set2 = {4,5,9,0,1}
print(set1.union(set2))
print(set1.intersection(set2))