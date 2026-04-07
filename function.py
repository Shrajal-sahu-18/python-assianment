def hello():
    print("hello world")
hello()
hello()


#sum of two number
def sum(a,b):
    s = a+b
    return s
#argument
ans = sum(23,45)
anss = sum(19999,13848)
print(ans)
print(anss)


#avarage of three num 

def avg(a,b,c):
    sum = (a+b+c)/3
    return sum
print(avg(2,2,2))
print(avg(2,2,8))

def avg(a,b=1):
    return a+b
print(avg(3,8))
