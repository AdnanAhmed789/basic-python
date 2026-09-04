get = (9,5,10,4,5)
print(type(get))
print(get[0])
print(get[0:3])
movie1 = input("Enter first movie name ")
movie2 = input("Enter movie second ")
movie3 = input("Enter movie third ")
allmovies = []
allmovies.append(movie1)
allmovies.append(movie2)
allmovies.append(movie3)
print(allmovies)
print(type(allmovies))
# Using copy methond
take = [1,2,3,2,]
print(take[::4])
take_copy = take.copy()
take_copy.reverse()
if(take == take_copy):
    print("it's palindrom")
else:
    print("it is not palindrom")
# Without copy method
if(take == take[::-1]):
    print("palindrom")
else:
    print("not palindrom")
print(take.count(2))
jack = [4,3,7,1]
jack.sort()
print(jack)