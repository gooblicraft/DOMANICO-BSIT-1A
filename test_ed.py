def topics_definition(selected):
    import time, os
    while True:
        os.system('cls')
        print("--------------------- < Definition > ---------------------\n")
        if selected == 1:
            lines = [
            "> The print statement is used to display output to the \nconsole.",
            "> It is one of the most common and essential function in \npython to produce text output."]

            for line in lines:
                for char in line:
                    print(char, end="", flush=True)  # Print each character without a newline
                    time.sleep(0.07)  # Add a delay between characters
                print("\n")  # Add a newline after finishing a line
            for y in range(1, 59): print("-", end = "")
            
            input("\nPress any key to return on the menu...")
            os.system('cls')
            break
        elif selected == 2:
            lines = [
            "> The variable is used to store value to the console.",
            "> To store a value, just simply assign '=' between the \nvariable name and the value."]

            for line in lines:
                for char in line:
                    print(char, end="", flush=True)  # Print each character without a newline
                    time.sleep(0.09)  # Add a delay between characters
                print("\n")  # Add a newline after finishing a line
            for y in range(1, 59): print("-", end = "")
            input("\nPress any key to return on the menu...")
            os.system('cls')
            break
        
        elif selected == 3:
            arithmeticOP = ['+ : Addition', 
                        '- : Subtraction', 
                        '* : Multiplication',
                        '/ : Division',
                        '% : Modulus',
                        '** : Exponentiation',
                        '// : Floor Division']
        
            comparisonOP = ['== : Equal to',
                            '!= : Not equal to',
                            '> : Greater than',
                            '< : Less than',
                            '>= : Greater than or equal to',
                            '<= : Less than or equal to']
            
            assignmentOP = ['= : Assignment',
                            '+= : Add and assign',
                            '-= : Subtract and assign',
                            '*= : Multiply and assign',
                            '/= : Divide and assign',
                            '%= : Modulus and assign',
                            '**= : Exponent and assign',
                            '//= : Floor divide and assign']
            
            logicalOP = ['and : Logical AND',
                        'or : Logical OR',
                        'not : Logical NOT']
            
            membershipOP = ['in : Returns True if a sequence with the specified value is present in the object',
                            'not in : Returns True if a sequence with the specified value is not present in the object']
            
            lines = ['> The operators are categorized depending to their functions.', 
                    '> We have these following type of operators:']
            
            for line in lines:
                for char in line:
                    print(char, end="", flush=True)  # Print each character without a newline
                    time.sleep(0.07)  # Add a delay between characters
                print("\n")  # Add a newline after finishing a line
            
            print("1.) Arithmetic Operators - used to perform mathematical operations"), time.sleep(3)
            print("2.) Comparison Operators - used to compare two values"), time.sleep(3)
            print("3.) Assignment Operators - used to assign values to a variables"), time.sleep(3)
            print("4.) Logical Operators - used to combine conditional statements"), time.sleep(3)
            print("5.) Membership Operators - used to test if it is present in a object\n"), time.sleep(3)
            
            for y in range(1, 59): print("-", end = "")
            ask = input("\nSelect a topic to show list of operators (Press any key to return): ")
            if ask == "1":
                print("--------------------- < Arithmetic Operator > ---------------------")
                for operator in arithmeticOP: print(operator), time.sleep(1)
                for y in range(1, 59): print("-", end = "")
            elif ask == "2":
                print("--------------------- < Comparison Operator > ---------------------")
                for operator in comparisonOP: print(operator), time.sleep(1)
                for y in range(1, 59): print("-", end = "")
            elif ask == "3":
                print("--------------------- < Assignment Operator > ---------------------")
                for operator in assignmentOP: print(operator), time.sleep(1)
                for y in range(1, 59): print("-", end = "")
            elif ask == "4":
                print("--------------------- < Logical Operator > ---------------------")
                for operator in logicalOP: print(operator), time.sleep(1)
                for y in range(1, 59): print("-", end = "")
            elif ask == "5":
                print("--------------------- < Membership Operator > ---------------------")
                for operator in membershipOP: print(operator), time.sleep(1)
            else: return