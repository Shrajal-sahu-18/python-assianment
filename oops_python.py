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


class student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

stud1 = student("shrajal,",9.44)
stud2 = student("urvashi",9.0)
stud3 = student("shreya",8.8)

print(stud1.name,stud1.cgpa)
print(stud2.name,stud2.cgpa)
print(stud3.name,stud3.cgpa)



class student:
    def __init__(self,name,cgpa):
        self.cgpa = cgpa
        self.name = name


    def get_cgpa(self):
        return self.cgpa
stud1 = student("shrajal",9.9)
stud2 = student("shreya",9.9)
print(stud1.get_cgpa())
print(f"{stud1.name}has cgpa = {stud1.get_cgpa()}")
print(f"{stud2.name} has cgpa = {stud2.cgpa}")
print(f"{stud2.name} has cgpa = {stud2.get_cgpa()}")