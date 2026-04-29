marks = []
for i in range(5):
    m = float(input(f"enter marks of subject {i+1}:"))
    marks.append(m)
#percentage & sum calculate
total = sum(marks)
percentage = total / 5

#Grade
if percentage >= 90:
    Grade = "A"
elif percentage >= 75:
    Grade = "B"
elif percentage >=50:
    Grade = "C"
else:
    Grade = "Fail"

print("mars:",marks)
print("percentage:",percentage)
print("Grade:",Grade)