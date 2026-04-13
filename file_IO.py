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