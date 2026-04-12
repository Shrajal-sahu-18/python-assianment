# class student:
#     subject = "python"
#     collage = "abc collage"
#     year = "4th year"
    
# a = 10
# stud1 = student()
# stud2 = student()
# print(stud1.subject,stud1.collage)
# print(stud2.subject,stud2.collage)
# print(type(stud1))
# l = [1,2]
# print(type(l))
# s = set()
# print(type(s))
# tup = (1,2),
# print(type(tup))
# def fun():
#     print("/.....")



# #constructor
# #init_method


# class student:
#     def __init__(self):
#         print("constructor is called")

# stud1 = student()
# stud2 = student()
# stud3 = student()


# class student:
#     def __init__(self,name):
#         self.name=name
# stud1 = student("rahul")
# stud2 = student("urvashi")
# stud3 = student("shradhha")
# print(stud1.name)

# print(stud2.name)
# print(stud3.name)


# class student:
#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa

# stud1 = student("shrajal,",9.44)
# stud2 = student("urvashi",9.0)
# stud3 = student("shreya",8.8)

# print(stud1.name,stud1.cgpa)
# print(stud2.name,stud2.cgpa)
# print(stud3.name,stud3.cgpa)



# class student:
#     def __init__(self,name,cgpa):
#         self.cgpa = cgpa
#         self.name = name


#     def get_cgpa(self):
#         return self.cgpa
# stud1 = student("sahil",9.9)
# stud2 = student("shradha",9.9)
# print(stud1.get_cgpa())
# print(f"{stud1.name}has cgpa = {stud1.get_cgpa()}")
# print(f"{stud2.name} has cgpa = {stud2.cgpa}")
# print(f"{stud2.name} has cgpa = {stud2.get_cgpa()}")


# class student:
#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa
#     def get_name(self):
#         return self.name
#     def get_cgpa(self):
#         return self.cgpa
    
# stud1 = student("sahil",9.9)
# stud2 = student("anuradha",9.9)

# print(stud1.get_name())
# print(stud2.get_name())
# print(stud1.get_cgpa())



# #class attribute
# #instance attribute 


# class student:
#     collage_name = "global engennring"

#     def __init__(self,name):
#         self.name = name
# stud1 = student("shrajal")

# print(stud1.collage_name)
    
# print(student.collage_name)


# #instance method


# class laptop:
#     storage_type = "ssd"

#     def __init__(self,ram,storage):
#         self.ram = ram
#         self.storage = storage

# #class method
# @classmethod
# def get_storage_type(cls):
#         print(f"storage type = {cls.storage_type}")
# def get_info(self):
#     print(f"the laptop has {self.ram} & {self.storage}")



#     @staticmethod

#     def cal_discount(price,discount):
#         final_price = price-((price*discount)/100)
#         print(f"discounted price ={final_price} ")



    

# l1 = laptop("16gb","512gb")
# l2 = laptop("8gb","256gb")

# l1.get_info()

# l1.get_storage_type()
# l1.cal_discount(40000,10)



# class student:
#     def __init__(self,name,cgpa):
#         self.cgpa = cgpa
#         self.name = name
#         #print("constructor was called")
#     def get_cgpa(self):
#         return self.cgpa
# stud1 = student("shakti",9.88)
# stud2 = student("shreya",9.77)
# stud3 = student("shradha ",9.66)

# print(stud1.name,stud1.cgpa)
# print(stud2.name,stud2.cgpa)
# print(stud3.name,stud3.cgpa)
# print(stud1.get_cgpa()
# )



# #encapsulation

# class bank_account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance#protected#__ = private

#     def get_balance(self):
#             return self.__balance
    
#     def set_balance(self,newbalance):
#         self.__balance = newbalance


# accc1 = bank_account("rahul kumar",100_000)

# # print(accc1.name,accc1.get_balance())
# accc1.set_balance(10000)
# # print(accc1._bank_account__balance)



# # #inheriatence

# class employee:
#      start_time = "10am"
#      end_time = "6pm"

#      def change_time(self,new_balance):
#           self.end_time = new_balance

    
     
# class teacher(employee):
#      def __init__(self,subject):
#           self.subject = subject


# class adminsatff(employee):
#      def __init__(self,role):
#           self.role = role

     
# # t1 = teacher("math")
# # t1.change_time("10pm")
# # print(t1.subject,t1.start_time,t1.end_time)
# staff1 = adminsatff("manager")
# print(staff1.start_time,staff1.end_time)
# print(staff1.role)



# #muti_level inheriatene
# class employee:
#      start_time = "10am"
#      end_time = "10pm"

# class adminstaff(employee):
#      def __init__(self,role):
#           self.role = role

# class accountant(adminstaff):
#      def __init__(self,salary,role):
#           super().__init__(role)
#           self.salary = salary

# acc1 = accountant(25_000,"manager")
# print(acc1.start_time,acc1.salary,acc1.role)



# #multiple inheriatence

# class teacher:
#      def __init__(self,salary):
#           self.salary = salary

# class student:
#      def __init__(self,gpa):
#           self.gpa = gpa

# class ta(teacher,student):
#      def __init__(self,salary,gpa,name):
#           super().__init__(salary)
#           student.__init__(self,gpa)
#           self.name = name

# ta1 = ta(15_000,9.3,"shrajal")
# print(ta1.salary,ta1.gpa,ta1.name)


# #Abstraction


# from abc import ABC,abstractmethod

# class animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class lion(animal):
#     def make_sound(self):
#         print("roor")

# class cow(animal):
#     def make_sound(self):
#         print("moo!")

# c1 = cow()
# c1.make_sound()
# l1 = lion()
# l1.make_sound()



# #polymorphism


# class employeee:
#     def get_desigintion(self):
#         print("desigination = employeee")

# class teacher:
#     def get_desigintion(self):
#         print("desigintion = teacher")

# t1 = teacher()
# t1.get_desigintion()


# #duck typing

# class teacher:
#     def get_desigination(self):
#         print("desiginaton = teacher")
# class accountant:
#     def get_desigination(self):
#         print("desigintion = accountant")

# t1 = teacher()
# acc1= accountant()
# acc1.get_desigination()


# #practice problem

# class bank_account:
#     def __init__(self,account_number,owner_name,balance = 0):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance+=amount
#         print("deposited",amount)

#     def withdrawal(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("withdrawal",amount)
#         else:
#             print("insufficient balance")
    
#     def check_balance(self):
#         print("current_balance",self.balance)


# acc1 = bank_account(12345,"shrajal sahu",10_000)
# acc1.deposit(50_000)
# acc1.withdrawal(10_000)
# acc1.check_balance()
# print(acc1.owner_name,acc1.account_number,acc1.balance)


# class book:
#     def __init__(self,tittle,author):
#         self.tittle = tittle
#         self.author = author
#         self.reviews = []

#     def add_review(self,review):
#         self.reviews.append(review)

#     def count_review(self):
#         return len(self.reviews)
    
#     def display_review(self):
#         if not self.reviews:
#             print("nothing to yet")
#         else:
#             for i, review in enumerate(self.reviews,1):
#                 print(i,review)

# b1 = book("python","shrajal")
# b1.add_review("good for learning")
# b1.add_review("good for study")
# b1.display_review()
# print("total",b1.count_review())
# print(b1.reviews)
# print(b1.tittle)



# class student:
#     def __init__(self,name,roll_no,marks):
#         self._name = name
#         self._roll_no = roll_no
#         self._marks = marks
#     def get_name(self):
#         return self._name
#     def get_roll_no(self):
#         return self._roll_no
#     def get_marks(self):
#         return self._marks
    
#     def set_name(self,name):
#         if name != "":
#             self._name = name
            
#         else:
#             print("empty name is not allowed")
    
#     def set_roll_no(self,roll_no):
#         if 1<= roll_no <=100:
#             self._roll_no = roll_no
            
#         else:
#             print("invaliad roll no")
    
#     def set_marks(self,marks):
#         if marks>=0:
#             self._marks = marks
            
#         else:
#             print("negative marks not allowed")

# s1 = student("shrajal",12,90)
# print(s1.get_name())
# print(s1.get_roll_no())
# print(s1.get_marks())
# s1.set_marks(80)
# s1.set_roll_no(1000)
# s1.set_name("")
# s1.set_marks(-1)



# class shape:
#     def area(self):
#         print("area method (base class)")

# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius*self.radius

# class rectangle(shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width

# class traingle(shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5*self.base*self.height

# c = circle(5)
# r = rectangle(3,5)
# t = traingle(4,5)
# print(c.area())
# print(r.area())
# print(t.area())


# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     def __init__(self,model,brand):
#         self.model = model
#         self.brand = brand
#     @abstractmethod
#     def show_details(self):
#         pass

# class car(vehicle):
#     def __init__(self,model,brand,seats):
#         super().__init__(brand,model)
#         self.seats = seats
#     def show_details(self):
#         print(f"{self.model},{self.brand},{self.seats}")

# class bike(vehicle):
#     def __init__(self,model,brand,engine_cc):
#         super().__init__(brand,model)
#         self.engine_cc = engine_cc
#     def show_details(self):
#         print(f"{self.model},{self.brand},{self.engine_cc}")

# c1  = car("fortuner","toyota",7)
# b1 = bike("rx-100","yamaha","98cc")

# c1.show_details()
# b1.show_details()




# from abc import ABC,abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Intern(Employee):
#     def __init__(self,stipend):
#         self.stipend = stipend
#     def calculate_salary(self):
#         return self.stipend

# class Fulltimeemployee(Employee):
#     def __init__(self,base_salary,bonus):
#         self.base_salary = base_salary
#         self.bonus = bonus
    
#     def calculate_salary(self):
#         return self.base_salary+self.bonus
    
# class contractemployee(Employee):
#     def __init__(self,hourly_rate,hours):
#         self.hourly_rate = hourly_rate
#         self.hours = hours

#     def calculate_salary(self):
#         return self.hourly_rate*self.hours


# c1 = Intern(10_000)
# F1 = Fulltimeemployee(60_000,20_00)
# co = contractemployee(300,5)

# print(c1.calculate_salary())
# print(F1.calculate_salary())
# print(co.calculate_salary())




class person:
    def __init__(self,name = None,age = None,address = None):
        self.name =name
        self.age = age
        self.address = address
    def display(self):
        print(self.name)
        print(self.age)
        print(self.address)

p1 = person(name = "abc")
p1.display()
p2 = person(name = "abc",age = 20)
p2.display()
p3 = person(name = "abc",age = 20,address = "abc colony")
p3.display()