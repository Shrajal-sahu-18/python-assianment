marks = [14,12,34,34,23,3,23]

print(type(marks))
print(marks[4])
marks[2] = 40
print(marks)
print(marks[1:])

#i.append

list = [1,2,3,4,5,6,0]
list.append(8)
print(list)
list.insert(2,10)
print(list)

list.sort(reverse=True)
list.reverse()
print(list)
for val in list:
    print(val)


list = [1,2,3,4,5,6,7,8,9]
x = 7
count = 0
for var in list:
    if var == x:
        print(f"{x} found in count= {count}")
        break
    count+=1
       
list  = [1,2,3,4,5,6,7,8,9]
x = 7
count = 0
for var in list:
    if var  == x:
        print(f"count of x={7} is {count}")
        break
    count+=1