# data = True
# word = "python"
# line = 1
# with open("sample.txt","r") as f:
#     while data:
#         data = f.readline()
#         if word in data:
#             print(f"{word} find in line number {line}")
#             break
#         print(data)
#         line+=1


#exeption handlin
try:

    x = int(input("enter x:"))

    ans = 10/x
except ZeroDivisionError:
    print(f"dividing by zero is not allowed")

else:

    print(f"ans = {ans}")
