#conditional statement

age = int(input("enter your age"))
if age>=22:
    print("you can vote")
    print("ypu can drive")
else:
    print("you can't vote")    

colour= (input("enter colour:"))
if colour == "red":
    print("stop")
elif colour ==" yellow":
    print("wait")
elif colour == "green":
    print("you will go")
else:
    print("wrong colour for traffic light")




username =(input("enter username:"))
password = (input("enter password:"))
if( username == "admin" and password == "pass"):
    print("login successfull")
elif (username!="admin"):
    print("wrong username")
else:
    print("wrong password")


num = int(input("enter number"))
if (num % 5==0):
    print("multiple of 5")
else:
    print("not a multiple of 5")

num = int(input("enter number"))

if (num%18==0):
    print("multiple of 18")
else:
    print("Not a multiple of 18")


num  = int(input("enter number:"))
if (num % 2==0):
    print("even number:")
else:
    print("odd number:")


# nesting 


username = (input("enter username"))
password = (input("enter password"))
if(username=="admin" and password== "pass"):
    print("success")
else:
    if(username!="admin"):
        print("wrong username")
    else:
        print("wrong password")    
