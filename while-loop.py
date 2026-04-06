#infinite loop
 
while True:
    print("hello world")


#while 

count = 1 #iterator
while(count<=10):
    print("hello world",count)
    count +=1

print("after loop count value:", count)

count = 1
while(count<=5):
    print(count)
    count+=1
print("after loop break count value :",count)


count = 5
while(count>=1):
    print(count)
    count-=1


count = 10
while(count>=1):
    print(count)
    count-=1

#multiplication table of any number

n = int(input("enter the number"))
i = 1
while(i<=10):
    print(n*i)
    i+=1

n = int(input("enter the number"))
i = 0
while(i<10):
    print(n*(i+1))
    i+=1


