correct_username = "admin"
currect_password = "1234"
attempts = 3
while attempts > 0:
    username = (input("enter username:"))
    password = (input("enter password:"))

    if username == correct_username and password == currect_password:
        print("login successfull")
        break
    elif username != correct_username and password != currect_password:
        print("Both username  and password wrong")
    elif username != correct_username:
        print("wrong username")
    elif password != currect_password:
        print("wrong password")
    attempts -=1
    print(f"attempts left {attempts}")
else:
    print("account is locked (too many attempts)")