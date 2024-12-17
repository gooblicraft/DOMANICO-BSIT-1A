import os, sys
import webbrowser as open_web
from try_code import run_user_program
from sub_menus import *
from workfiles import main  # Import main.py

# Get the absolute path of the project root directory
project_root = os.path.abspath(os.path.join(os.getcwd(), 'FINAL PROJECT - Domanico IT1A'))

# Add the 'workfiles' folder to sys.path
sys.path.append(os.path.join(project_root, 'workfiles'))

isRun = True
while isRun:
    isAccess = input("Do you want to access Domanico's Project (yes/no)? ")
    os.system('cls')
    
    if isAccess.lower() == "no":
        print("Hope you enjoy my Simple Program for my Finals Project in First Semester")
        isRun = False
    elif isAccess.lower() == "yes":
        while True:
            print("--------------------- < MAIN MENU OF DOMANICO'S PROJECT > ---------------------\n")
            print("Select the option you want to access.\n")
            options = {1: "Print Statements", 2: "Variables", 3: "Operators", 4: "Conditionals", 5: "Loops", 6: "Lists", 7: "Functions", 8: "1st Sem Workfiles", 9: "Run your own program", 10: "Github Profile"}

            # Display options in two columns
            for i in range(1, 6):  # First column keys (1-5)
                first_col = f"{i}: {options[i]}"
                second_col = f"{i + 5}: {options[i + 5]}" if i + 5 in options else ""
                print(f"{first_col:<30} {second_col}")
                
            print("\nPress any key to return...")
            for x in range(1, 79): print("-", end = "")
            isAsk = input("\nSelect : ")
            os.system('cls')
            
            if isAsk == "1":
                print_statements()
            elif isAsk == "2":
                variables()
            elif isAsk == "3":
                operators()
            elif isAsk == "4":
                conditionals()
            elif isAsk == "5":
                loops()
            elif isAsk == "6":
                lists()
            elif isAsk == "7":
                functions()
            elif isAsk == "8":
                # Run the main.py script from workfiles
                main.access_workfiles()  # Call the main() function from main.py
            elif isAsk == "9":
                run_user_program()
            elif isAsk == "10":
                open_web.open("https://github.com/gooblicraft")
            else: break
