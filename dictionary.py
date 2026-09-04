dict = {
    "name" : "Adnan Ahmed",
    "cast" : "Talpur",
    "province" : "Sindh" ,
    "age" : 20,
    "tup" : ("mango","apple",'graps'),
    34 : "age"
    }
print(dict)
print(dict["name"])
print(dict["cast"])
print(dict["province"])
print(dict["age"]) 
print(dict["tup"])
print(dict[34])
print(type(dict))
dict["age"] = 21
dict["jack"] = "slow"# dictionary are muteable
print(dict)
room = {
    "subject" : ["hindi","sindhi","urdu","english",],
    "name_1" : ("Adnan","Sultan","Shahid","Aftab","Shazad"),
    "name_2" : {"Adnan","Sultan","Shazad","Shahid","Aftab"},
    20 : "age" 
}
print(room)
print(room["name_1"])
print(room["name_2"])
"""
In name_2 you can see {} are present so it is not
list or tuples but it is called set so set has 
not any order so sometimes 1st number comes in 3
or others comes in other order
"""
nul_dict = {}
print(nul_dict)
nul_dict['name'] = "Adnan"
print(nul_dict)
nul_dict[45] = 354
print(nul_dict)
students = {
    "subjects" : {
        "english" : 45,
        "Botany" : 56,
        "zoology" : 78,
    },
     "role no" : 16,
     "current field" : "Pre-Medical"
}     
print(students)
print(students.keys())
print(students.items())
print(list(students.items()))
pair = (list(students.items()))
print(pair[0])
print(pair[2])
print(students.get("subjects"))
students.update({"city" : "Badin"})
print(students)
students["you"] = "me"
print(students.keys())