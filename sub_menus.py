from example_codes import *
from topics import topics_definition
from try_code import run_user_program
import os

def print_statements():
    while True:
        """< Sub Menu for Print Statements >"""
        print("--------------------- < SUB MENU FOR PRINT STATEMENT > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(1)
        elif select == "2":  printState_example()
        elif select == "3": run_user_program()
        elif select == "4": return False

def variables():
    while True:
        """< Sub Menu for Variables >"""
        print("--------------------- < SUB MENU FOR VARIABLES > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(2)
        elif select == "2":  variables_example()
        elif select == "3": run_user_program()
        elif select == "4": return

def operators():
    while True:
        """< Sub Menu for Operators >"""
        print("--------------------- < SUB MENU FOR OPERATORS > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(3)
        elif select == "2": operators_example()
        elif select == "3": run_user_program()
        elif select == "4": return False
        
def conditionals():
    while True:
        """< Sub Menu for Conditionals >"""
        print("--------------------- < SUB MENU FOR CONDITIONALS > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(4)
        elif select == "2": conditionals_example()
        elif select == "3": run_user_program()
        elif select == "4": return False

def loops():
    while True:
        """< Sub Menu for LOOPS >"""
        print("--------------------- < SUB MENU FOR LOOPS > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(5)
        elif select == "2": loops_example()
        elif select == "3": run_user_program()
        elif select == "4": return False
        
def lists():
    while True:
        """< Sub Menu for Lists >"""
        print("--------------------- < SUB MENU FOR LISTS > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(6)
        elif select == "2": lists_example()
        elif select == "3": run_user_program()
        elif select == "4": return False
        
def functions():
    while True:
        """< Sub Menu for Functions >"""
        print("--------------------- < SUB MENU FOR FUNCTIONS > ---------------------")
        print("\nSelect the option you want to access.")
        print("\n1.) Definition \n2.) Example Code \n3.) Try to code \n4.) Exit\n")
        for x in range(1, 74): print("-", end = "")
        select = input("\nSelect : ")
        os.system('cls')
        if select == "1": topics_definition(7)
        elif select == "2": functions_example()
        elif select == "3": run_user_program()
        elif select == "4": return False
