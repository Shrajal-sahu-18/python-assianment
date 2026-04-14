data = True
word = "python"
line = 1
with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(f"{word} find in line number {line}")
            break
        print(data)
        line+=1


#exeption handling
try:

    x = int(input("enter x:"))

    ans = 10/x
except ZeroDivisionError:
    print(f"dividing by zero is not allowed")

else:

    print(f"ans = {ans}")



try:
    x = int(input("enter x:"))
    ans = 10/x
except ValueError:
    print("invalid input")

else:
    print("f ans = {ans}")

finally:
    print("end of program")


#list comprehension

sqares = []
for i in range(6):
    sqares.append(i*i)
print(sqares)


sqare = [i*i for  i in range(6) if i % 2!= 0]
print(sqare)


nums = [1,2,3,-1,-2,-3]
nums = [0 if val<0 else val for val in nums]
print(nums)


words = ["hello","python","apna collage"]

words = [val.upper() for val in words]
print(words)



import json

py_obj = {
    "name":"shrajal",
    "isteacher":True
}

json_str = json.dumps(py_obj)
print(type(json_str),json_str)