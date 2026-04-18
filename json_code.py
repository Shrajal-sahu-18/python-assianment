with open("sample.txt","w") as f:
    for i in range(5):
        name = input(f"enter name{i+1}")
        f.write(name +"\n")
with open("sample.txt","r") as f:
    print("\n names in files")
    for line in f:
        print(line.strip())

with open("sample.txt","a") as f:
    data = f.write("program run successfull\n")
with open("sample.txt","r") as f:
    data = f.read()
    print("logs:\n")
    print(data)