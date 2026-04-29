while True:
    print("\n calculater:")
    print("1. Add:")
    print("2. Substraction:")
    print("3. Multiply:")
    print("4. divide:")
    print("5. Exit:")

    choice = (input("Enter choice (1-5):"))
    if choice == "5":
        print("calculater stooped")
        break
    if choice == ("1","2","3","4"):
        a = float(input("enter a:"))
        b = float(input("enter b:"))

        if choice == "1":
            print("Result:",a+b)
        elif choice == "2":
            print("Result:",a-b)
        elif choice == "3":
            print("Result:",a*b)
        elif choice == "4":
            if b != 0:
                print("ResultL",a/b)
            else:
                print("Dividing by zero is not allowed")
        else:
            print("Invaild choice")

