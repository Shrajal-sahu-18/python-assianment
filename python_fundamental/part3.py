#strings in python

word1 = "python"
word = " is good language for begineer "
print(word1+word)

#slicing in strings
word = "python"
print(word[2:4])

str = "hello i am shrajal sahu from majholi  iam learning python from apna collage "
print(str[11:23])

str = "python"
print(str[-4:-2])

#normal formating
a = 5
b = 5
sum = a+b
print("sum of{}&{}&{}".format(a,b,sum))

#index based formating

a = 5
b = 6
sum = a+b
print("sum of {1} & {0} is {2}".format(a,b,sum))


#value based formating

a = 5
b = 6
sum = a+b
print("sum of {b} & {a} is {s}:".format(a = 5,b = 6,s = sum))


#f - strings 
a = 5
b = 6
print(f"sum of {a} & {b} is {(a+b)/2}")

a = 5
b = 5
c = 6
print(f"sum of {a} & {b} & {c} is {(a+b+c)/3}")