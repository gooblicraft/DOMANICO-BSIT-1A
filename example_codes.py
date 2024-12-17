import os

def printState_example():
    print("--------------------- < Example Code > ---------------------\n")

    print("Code:")
    print('print("Your code")\n')

    print("Example Code:")
    print('print("Hello Programmer")\n')
    for y in range(1, 61): print("-", end = "")

    print('\nOutput:')
    print('Hello Programmer\n')
    for y in range(1, 61): print("-", end = "")
    
    input("\nPress any key to return on the menu...")
    os.system('cls')
    
def variables_example():
    print("--------------------- < Example Code > ---------------------\n")

    print("Code:")
    print('variable_name = value')

    print("Example Code:\n")
    print('name = "user1")\n')
    print('print(name)\n')
    for y in range(1, 61): print("-", end = "")

    print('\nOutput:')
    print('user1\n')
    for y in range(1, 61): print("-", end = "")
    
    input("\nPress any key to return on the menu...")
    os.system('cls')
    
def operators_example():
    print("--------------------- < Example Code > ---------------------\n")

    print("Code:")
    print("sum = 0")
    print('sum += 1      #Check the definition of operators to see the operators you can use')
    print("print(sum)\n")
    for y in range(1, 61): print("-", end = "")

    print('\nOutput:')
    print('1\n')
    for y in range(1, 61): print("-", end = "")
    
    input("\nPress any key to return on the menu...")
    os.system('cls')
    
def conditionals_example():
    print("--------------------- < Example Code > ---------------------\n")

    print("Code:")
    print("x = 7")
    print('if x > 10:\n     print("x is greater than 10")')
    print('elif x > 5:\n     print("x is greater than 5 but less than or equal to 10")')
    print('else:\n     print("x is 5 or less")\n')
    for y in range(1, 61): print("-", end = "")

    print('\nOutput:')
    print('x is greater than 5 but less than or equal to 10\n')
    for y in range(1, 61): print("-", end = "")
    
    input("\nPress any key to return on the menu...")
    os.system('cls')
    
def loops_example():
    print("--------------------- < Example Code > ---------------------\n")

    print("Code:")
    print("#for loop\n")
    print('fruits = ["apple, "banana", "mango"]')
    print('\nfor fruit in fruits:\n    print(fruit)\n')
    for y in range(1, 61): print("-", end = "")

    print('\nOutput:')
    print('appple\nbanana\nmango\n')
    for y in range(1, 61): print("-", end = "")
    
    input("\nPress any key to return on the menu...")
    os.system('cls')

def lists_example():
    from print_codes import code_list
    print(code_list)
    
    for y in range(1, 61): print("-", end = "")
    print('\nOutput:')
    
    code_list_output = """
['BSAIS', 'BSIT', 'BSSW', 'BSA', 'DHRS', 'BSED', 'BSIT_CLONE']
['BSAIS', 'BSIT', 'BSSW', 'BSA', 'DHRS', 'BSED']
There are : 6
"""
    print(code_list_output)
    
    for y in range(1, 61): print("-", end = "")
    input("\nPress any key to return on the menu...")
    os.system('cls')

def functions_example():
    from print_codes import example_functions
    print(example_functions)
    
    for y in range(1, 61): print("-", end = "")
    print('\nOutput:')
    print("Alice\n30")
    
    for y in range(1, 61): print("-", end = "")
    input("\nPress any key to return on the menu...")
    os.system('cls')
    