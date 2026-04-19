# python fundamental part 1
# varriable , data types , keyword , operators , type conversion , user input .
# question based on part 1 topic 


#data types 
#integer
#float
#boolean

#operators
#arithmetic operators
a = 4
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a * a )

#relational /comparsion operators

a = 10
b = 10
a == b
print(a != b)

#assianment operator
a = 5
a-= 5
print(a)

a = 5
a+=10
print(a)


a = 5
a*=10
print(a)


#logical opreator
var = False
print(not var)

a = 10
b = 20 
print( not a<b)

name  = "shrajal sahu from majholi"

print(  3<5 or 4>5)

#type conversation

ans = int(1+1.6)
print(type(ans))

#user input

a = input("enter your name")
print("welcome:",a)


a =int (input("enter first number"))
b = int(input("enter second number"))
print("output:",a+b)

a = float(input("enter 1st number"))
b = float(input("enter 2nd number"))
print("avarage of two number:",((a+b)/2))
