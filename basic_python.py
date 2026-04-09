marks = [14,12,34,34,23,3,23]

print(type(marks))
print(marks[4])
marks[2] = 40
print(marks)
print(marks[1:])

#i.append

list = [1,2,3,4,5,6,0]
list.append(8)
print(list)
list.insert(2,10)
print(list)

list.sort(reverse=True)
list.reverse()
print(list)
for val in list:
    print(val)


list = [1,2,3,4,5,6,7,8,9]
x = 7
count = 0
for var in list:
    if var == x:
        print(f"{x} found in count= {count}")
        break
    count+=1
       
list  = [1,2,3,4,5,6,7,8,9]
x = 7
count = 0
for var in list:
    if var  == x:
        print(f"count of x={7} is {count}")
        break
    count+=1


tup = (1,2,3,4)
print(tup)
print(type(tup))
print(len(tup))


#slicing 
tup = (1,2,3,4,5,6,7)
print(tup[1:4])

tup = (1,2,3,4,5,6,7,8)
sum = 0
for val in tup :
    sum+=val
print(sum)


#t.index

tup = (1,2,2,8,9)
print(tup.index(8))

#tup.count
tup = (1,2,3,4,5,6,7,7)
print(tup.count(7))


tup = (1,2,3,4,5,6)
sum = 0
for val in tup:
    sum+=val
print(sum)

#dictionary

infor = {
    "name":"shrajal ",
    "cgpa":9.2,
    "subject":("math","science"),
    3.14:"pI",


}

print(type(infor))
print(infor)

dict = {
    "name": "shrajal sahu",
    "branch":"AIML",
    "semester":"3rd",
    "cgpa": 6.44,
    "result": "all clear",
}
dict["cgpa"]=9.6
dict["semester"]="4th"
print(dict["cgpa"])
print(dict["semester"])

responce = {
    "status":200,
    "data":{
        "username":"shrajal",
        "followers":1200,
    }
}
print(responce["data"]["username"])


#methods in dictionary

#d.keys

dict = {
    "name":"shrajal",
    "age":20,
    "semester":"3rd",
}
dict_keys = dict.keys()
print(dict_keys)
dict_keys = list(dict.keys())
print(type(dict_keys))

#dictionary.value

dict = {
    "name":"shrajal ",
    "class":"w3",
    "semester":"3rd",
}
dict_val =list (dict.values())
print(dict_val)
print(type(dict_val))

#d.items

dict = {
    "name":"shrajal",
    "age":20,
    "semester":"3rd",

    
}
dict_items =list (dict.items())
print(dict_items)
print(type(dict_items))

#d.get(val)

dict = {
    "name":"shrajal",
    "semester":"3rd",
    "age":20,
}


s = {1,2,3,4,5,6,6,6,6,6,6,6}
s.add(7)
print(s)

#sets methods

#s.add

s = {1,2,3,4,5,6}
s.add(10)
print(s)

#s.remove

s = {1,2,3,4,5,6,7}
s.remove(2)
print(s)

#s.clear

s = {1,2,3,4,5,6,7,8}
s.clear()
print(s)

#s.pop

s = {1,2,3,4,5,6,7,8}
print(s)
s.pop()


info = [
    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english"),
]
unique_courses = set()
for everytuple in info:
    unique_courses.add(everytuple[1])

print(unique_courses)
       



#s.union

s1 = {1,2,3,4,5,6}
s2 = {2,3,4,7,8}
print(s1.union(s2))
print(s1.intersection(s2))

#s.intersection

s1 = {1,2,3,4,5,6,7,8}
s2 = {2,3,4,5,6}
print(s1.intersection(s2))


info = [
    ("shrajal","math"),
    ("shakti","english"),
    ("shani","math"),
    ("tejus","science"),
    ("aditya","english"),
]

unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])
print(unique_courses)


info = [

    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english"),
]
dict = {}
for name,course in info:
    if (dict.get(name) is None):
        dict.update({name:{course}})
    
    else:
        dict[name].add(course)
print(dict)

info = [
    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english"),
]

unique_course = set()
for name,course in info:
    unique_course.add(course)
print(unique_course)
unique_course_list = list(unique_course)
#examiner ask convert into a list
print(unique_course_list)
print(type(unique_course_list))


dict = {}
for name,course in info:
    if (dict.get(name))==None:
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)


# data = [
#     ("amit","math"),
#     ("sumit","math"),
#    ( "amit","english"),
#    ( "sumit","english"),
#     ("amit","math"),
#     ("sumit","math"),
# ]


# dict = {}
# for name,subject in data:
#     if dict.get(name)==None:
#         dict.update({name:set()})
#         dict[name].add(subject)
#     else:
#         dict[name].add(subject)
# print(dict)
