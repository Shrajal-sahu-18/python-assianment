while True:
    a = float(input("enter first number:"))
    b = float(input("enter seond number:"))
    op = (input("choose operator (+,-,*,/) or q for quit:"))
    if op == "q":
        print("calculator is stop")
        break
    if op == "+":
        print(f"sum {a+b}")
    elif op == "-":
        print(f"substraction {a-b}")
    elif op == "*":
        print(f"multiplication {a*b}")
    elif op == "/":
        if b != 0:
            print(f"division {a/b}")
        else:
            print("dividing by zero is not allowed")
    else:
        print("wrong operator")