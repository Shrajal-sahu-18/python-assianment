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
stud1 = student("sahil",9.9)
stud2 = student("shradha",9.9)
print(stud1.get_cgpa())
print(f"{stud1.name}has cgpa = {stud1.get_cgpa()}")
print(f"{stud2.name} has cgpa = {stud2.cgpa}")
print(f"{stud2.name} has cgpa = {stud2.get_cgpa()}")


class student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
    def get_name(self):
        return self.name
    def get_cgpa(self):
        return self.cgpa
    
stud1 = student("sahil",9.9)
stud2 = student("anuradha",9.9)

print(stud1.get_name())
print(stud2.get_name())
print(stud1.get_cgpa())



#class attribute
#instance attribute 


class student:
    collage_name = "global engennring"

    def __init__(self,name):
        self.name = name
stud1 = student("shrajal")

print(stud1.collage_name)
    
print(student.collage_name)


#instance method


class laptop:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

#class method
@classmethod
def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")
def get_info(self):
    print(f"the laptop has {self.ram} & {self.storage}")



    @staticmethod

    def cal_discount(price,discount):
        final_price = price-((price*discount)/100)
        print(f"discounted price ={final_price} ")



    

l1 = laptop("16gb","512gb")
l2 = laptop("8gb","256gb")

l1.get_info()

l1.get_storage_type()
l1.cal_discount(40000,10)



# class student:
#     def __init__(self,name,cgpa):
#         self.cgpa = cgpa
#         self.name = name
#         #print("constructor was called")
#     def get_cgpa(self):
#         return self.cgpa
# stud1 = student("shrajal",9.88)
# stud2 = student("shreya",9.77)
# stud3 = student("shreya goutam",9.66)

# print(stud1.name,stud1.cgpa)
# print(stud2.name,stud2.cgpa)
# print(stud3.name,stud3.cgpa)
# print(stud1.get_cgpa()
# )