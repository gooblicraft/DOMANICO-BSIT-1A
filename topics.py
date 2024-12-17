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
            print("5.) Membership Operators - used to test if it is present in a object"), time.sleep(3)
            
            for y in range(1, 59): print("-", end = "")
            ask = input("\n\nSelect a topic to show list of operators (Press any key to return): ")
            os.system('cls')
            if ask == "1":
                print("--------------------- < Arithmetic Operator > ---------------------\n")
                for operator in arithmeticOP: print(operator), time.sleep(1)
                print()
                for y in range(1, 59): print("-", end = "")
                print()
                input("Press any key to return... ")
            elif ask == "2":
                print("--------------------- < Comparison Operator > ---------------------\n")
                for operator in comparisonOP: print(operator), time.sleep(1)
                print()
                for y in range(1, 59): print("-", end = "")
                print()
                input("Press any key to return... ")
            elif ask == "3":
                print("--------------------- < Assignment Operator > ---------------------")
                for operator in assignmentOP: print(operator), time.sleep(1)
                print()
                for y in range(1, 59): print("-", end = "")
                print()
                input("Press any key to return... ")
            elif ask == "4":
                print("--------------------- < Logical Operator > ---------------------")
                for operator in logicalOP: print(operator), time.sleep(1)
                print()
                for y in range(1, 59): print("-", end = "")
                print()
                input("Press any key to return... ")
            elif ask == "5":
                print("--------------------- < Membership Operator > ---------------------")
                for operator in membershipOP: print(operator), time.sleep(1)
                print()
                for y in range(1, 59): print("-", end = "")
                print()
                input("Press any key to return... ")
            else: return
        
        elif selected == 4:
            lines = [
            "> Conditionals are used to execute code based on whether \na condition is true or false.\n",
            "> The primary constructs for conditionals are if, elif,\nand else statements."]

            for line in lines:
                for char in line:
                    print(char, end="", flush=True)  # Print each character without a newline
                    time.sleep(0.07)  # Add a delay between characters
                print(" ")  # Add a newline after finishing a line
            print()
            print("\t1.) 'if' statement - used to test a condition.\n\tIf the condition is true, the block of code within \n\tthe if statement is executed.\n"), time.sleep(7)
            print("\t2.) 'elif' statement - used to test multiple \n\tconditions. If the condition for if is False, it checks \n\tthe condition of the elif block.\n"), time.sleep(8)
            print("\t3.) 'else' statement - used to execute a block \n\tof code if none of the preceding conditions are true.\n"), time.sleep(6)
            for y in range(1, 59): print("-", end = "")
            
            input("\nPress any key to return on the menu...")
            os.system('cls')
            break
        
        elif selected == 5:
            lines = [
            "> Loops are used to execute a block of code repeatedly.\n",
            "> The two main types of loops in Python are for loops \nand while loops.\n"]

            for line in lines:
                for char in line:
                    print(char, end="", flush=True)  # Print each character without a newline
                    time.sleep(0.07)  # Add a delay between characters
                print(" ")  # Add a newline after finishing a line
            print("\ta.) 'for' loop - used for iterating over \n\ta sequence (such as a list, tuple, dictionary, \n\tset, or string).\n"), time.sleep(6)
            print("\tb.) 'while' loop - used to execute a block \n\tof code as long as a condition is true.\n"), time.sleep(5)
            
            for y in range(1, 59): print("-", end = "")
            
            input("\nPress any key to return on the menu...")
            os.system('cls')
            break
        
        elif selected == 6:
            lines1 = ["> A list is a mutable, ordered collection of items that \ncan hold a variety of object types, including other lists.\n",
                "> Lists are one of the most versatile and commonly used \ndata types in Python.\n"]

            for line in lines1:
                for char in line:
                    print(char, end="", flush=True)  # Print each character without a newline
                    time.sleep(0.07)  # Add a delay between characters
                print(" ")  # Add a newline after finishing a line
                
            for x in range(1, 59): print("-", end = "")
            ask = input("\nTurn next page (Yes or No): ")
            os.system('cls')
            
            if ask.lower() == "yes":
                from print_codes import code1, code2, code3, code4, code5
                isContinue = True
                while isContinue:
                    print("--------------------- < Definition > ---------------------\n")
                    lines2 = ["1.) Creating a list - created by placing all the items \n(elements) inside square brackets [], separated by commas.\n",
                                "2.) Accessing a List - access elements in a list by \ntheir index (position). Indexing starts at 0.\n",
                                "3.) Modifying elements - Since lists are mutable, you \ncan change their elements.\n",
                                "4.) Adding a list - add elements to a list using methods \nlike append(), extend(), or insert().\n",
                                "5.) Removing Elements - Elements can be removed using methods \nlike remove(), pop(), or del.\n"]
                    
                    for line in lines2:
                        for char in line:
                            print(char, end="", flush=True)  # Print each character without a newline
                            time.sleep(0.05)  # Add a delay between characters
                        print(" ")  # Add a newline after finishing a line
                        
                    for x in range(1, 59): print("-", end = "")
                    isAccess = input("\nSelect option to see the code (press any key to return)... ")
                    os.system('cls')
                    
                    if isAccess == "1": print(code1), input("Press any key to return... "), os.system('cls')
                    elif isAccess == "2": print(code2), input("Press any key to return... "), os.system('cls')
                    elif isAccess == "3": print(code3), input("Press any key to return... "), os.system('cls')
                    elif isAccess == "4": print(code4), input("Press any key to return... "), os.system('cls')
                    elif isAccess == "5": print(code5), input("Press any key to return... "), os.system('cls')
                    else: isContinue = False
            else: break
            
        elif selected == 7:
            from print_codes import builtIn_functions, userDef_functions
            isContinue = True
            
            while isContinue:
                lines = [
                "> Functions are blocks of reusable code that perform \na specific task.\n",
                "> There are two types of functions in Python: built-in \nfunctions and user-defined functions.\n"]

                for line in lines:
                    for char in line:
                        print(char, end="", flush=True)  # Print each character without a newline
                        time.sleep(0.07)  # Add a delay between characters
                    print(" ")  # Add a newline after finishing a line
                print("1.) Built-in Functions - functions that you can use \nwithout any additional setup.\n"), time.sleep(6)
                print("2.) User-Defined Functions - functions that are created \nby the user to perform specific tasks.\n"), time.sleep(5)
                
                for y in range(1, 59): print("-", end = "")
                ask = input("\nSelect the option you want to see more (press any key to return): ")
                os.system('cls')
                
                if ask == "1":
                    print(builtIn_functions), input("Press any key to return... "), os.system('cls'), print("--------------------- < Definition > ---------------------\n")
                elif ask == "2":
                    print(userDef_functions), input("Press any key to return... "), os.system('cls'), print("--------------------- < Definition > ---------------------\n")
                else: isContinue = False
            break