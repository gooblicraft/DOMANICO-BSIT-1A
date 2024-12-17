def run_user_program():
    import os
    
    """Allows the user to input and run their Python code."""
    
    print("--------------------- < Try to Code ! > ---------------------\n")
    print("Type your code below. To finish, press any key.\n")
    
    user_code = []
    while True:
        line = input()
        
        if line.strip() == "":
            for x in range(1, 62): 
                print("-", end = "")
            print()
            print("OUTPUT:")
            break
        user_code.append(line)
    try:
        exec("\n".join(user_code))
    except Exception as e:
        print(f"Error executing your code: {e}")
        
    for x in range(1, 62): print("-", end = "")
    input("\nPress 'Any Key' to return to the main menu... ")
    os.system('cls')

