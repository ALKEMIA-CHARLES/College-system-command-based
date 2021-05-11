def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new student")
        print("2. Register new Teacher")
        print("3. logout")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("Register New Student")
            username = input(str("Student username: "))
            password = input(str("Student password: "))
            query_vals = (username, password)
            # command_handler.execute("Insert INTO users (username,password,privilege) VALUES (%s, %s,'student')", query_vals)
            # db.commit()
            print(username + " " + "has been registered as a student")

        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username: "))
            password = input(str("Teacher password: "))
            query_vals = (username, password)
            # command_handler.execute("Insert INTO users (username,password,privilege) VALUES (%s, %s,'student')", query_vals)
            # db.commit()
            print(username + " " + "has been registered as a teacher")
        
        elif user_option == "3":
            break
        else:
            print("No valid option selected")

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")

def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option = input(str("Option :"))
        if user_option == "1":
            print("Student Login")
        elif user_option == "2":
            print("Teacher Login")
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option was selected")

main()
