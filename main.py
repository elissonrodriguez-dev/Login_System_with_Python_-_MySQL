from auth import register_user, login_user

while True:
    option = input("1. Register | 2. Login | q. Exit")
    
    if option == "1":
        register_user(
            input("User: "),
            input("Password: ")
        )
    elif option == "2":
        login_user(
            input("User: "),
            input("Password: ")
        )
    elif option == "q":
        break