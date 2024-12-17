def print_statements():
    from test_ed import topics_definition
    from example_codes import printState_example
    from try_code import run_user_program
    import os
    
    while True:
        """< Sub Menu for Print Statements >"""
        print("--------------------- < SUB MENU FOR PRINT STATEMENT > ---------------------")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 77): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(1)
        elif select == "2":  printState_example()
        elif select == "3": run_user_program()
        elif select == "4": return False

def variables():
    from test_ed import topics_definition
    from example_codes import variables_example #aayusin
    from try_code import run_user_program
    import os
    
    while True:
        """< Sub Menu for Variables >"""
        print("--------------------- < SUB MENU FOR VARIABLES > ---------------------")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 77): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(2)
        elif select == "2":  variables_example()
        elif select == "3": run_user_program()
        elif select == "4": return False

variables()

