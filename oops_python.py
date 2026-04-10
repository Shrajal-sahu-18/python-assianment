class student:
    subject = "python"
    collage = "abc collage"
    year = "4th year"
    
a = 10
stud1 = student()
stud2 = student()
print(stud1.subject,stud1.collage)
print(stud2.subject,stud2.collage)
print(type(stud1))
l = [1,2]
print(type(l))
s = set()
print(type(s))
tup = (1,2),
print(type(tup))
def fun():
    print("/.....")



#constructor
#init_method


class student:
    def __init__(self):
        print("constructor is called")

stud1 = student()
stud2 = student()
stud3 = student()


class student:
    def __init__(self,name):
        self.name=name
stud1 = student("rahul")
stud2 = student("urvashi")
stud3 = student("shradhha")
print(stud1.name)

print(stud2.name)
print(stud3.name)