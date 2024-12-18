def act8():
    print("------------------- < Conditionals > -------------------\n")
    
    # Input password from user
    password = input("PASSWORD : ")

    # Check the password conditions
    if password == "secret":
        print("Successfully Logged in")
        print("System finished")
    elif password == "hatdog":
        print("Cheesedog Logged in")
    else:
        print("Incorrect password please try again...")


