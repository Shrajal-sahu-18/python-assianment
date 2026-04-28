number = [10,20,30,35,45,40,50,60]
count_even = 0
count_odd = 0
total_sum = 0
for num in number:
    total_sum += num
    if num % 2 == 0:
        count_even +=1
    else:
        count_odd +=1
print("even count:",count_even)
print("odd count:",count_odd)
print("total sum:",total_sum)