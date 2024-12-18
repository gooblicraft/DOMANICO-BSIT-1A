import os

#SIMPLE INPUT THAT RETURNS NOTHING HAHAHA
def ask_pass():
    for i in range(1,120): print("-", end="")
    input("\nPress any key to proceed to menu... ")

#DICTIONARIES FOR ACTIVITIES
def dict_activities():
    '''
                                            The Output Should Looks Like This

    1: Activity 1           6: Activity 6           11: Activity 11         16: Activity 16         21: Activity 21
    2: Activity 2           7: Activity 7           12: Activity 12         17: Activity 17         22: Activity 22
    3: Activity 3           8: Activity 8           13: Activity 13         18: Activity 18         23: Activity 23
    4: Activity 4           9: Activity 9           14: Activity 14         19: Activity 19         24: Activity 24
    5: Activity 5           10: Activity 10         15: Activity 15         20: Activity 20         25: Activity 25
    '''
    
    activities = {1: "Activity 1", 2: "Activity 2", 3: "Activity 3", 4: "Activity 4", 5: "Activity 5",
            6: "Activity 6", 7: "Activity 7", 8: "Activity 8", 9: "Activity 9", 10: "Activity 10",
            11: "Activity 11", 12: "Activity 12", 13: "Activity 13", 14: "Activity 14", 15: "Activity 15",
            16: "Activity 16", 17: "Activity 17", 18: "Activity 18", 19: "Activity 19", 20: "Activity 20",
            21: "Activity 21", 22: "Activity 22", 23: "Activity 23", 24: "Activity 24", 25: "Activity 25"}

    # Mas nagets koto HAHAHA
    print("\t\t\t\t\t\t< Domanico's Activities Challenges >\n")
    for i in range(1, 6):  # Column keys (1-5)
        first_col = f"{i}: {activities[i]}"
        second_col = f"{i + 5}: {activities[i + 5]}"
        third_col = f"{i + 10}: {activities[i + 10]}"
        fourth_col = f"{i + 15}: {activities[i + 15]}"
        fifth_col = f"{i + 20}: {activities[i + 20]}"
        print(f"{first_col}\t\t{second_col}\t\t{third_col}\t\t{fourth_col}\t\t{fifth_col}")

def dict_code_challenges():
    '''
                                            The Output Should Looks Like This
                                            
    1: Code Challenge 1             5: Code Challenge 5             9: Code Challenge 9             13: Code Challenge 13
    2: Code Challenge 2             6: Code Challenge 6             10: Code Challenge 10           14: Code Challenge 14
    3: Code Challenge 3             7: Code Challenge 7             11: Code Challenge 11           15: Code Challenge 15
    4: Code Challenge 4             8: Code Challenge 8             12: Code Challenge 12           16: Code Challenge 16
    '''
    
    activities = {1: "Code Challenge 1", 2: "Code Challenge 2", 3: "Code Challenge 3", 4: "Code Challenge 4",
                5: "Code Challenge 5", 6: "Code Challenge 6", 7: "Code Challenge 7", 8: "Code Challenge 8", 
                9: "Code Challenge 9", 10: "Code Challenge 10",11: "Code Challenge 11", 12: "Code Challenge 12", 
                13: "Code Challenge 13", 14: "Code Challenge 14", 15: "Code Challenge 15", 16: "Code Challenge 16"}

    # Eyyy, Pakak
    print("\t\t\t\t\t\t< Domanico's Code Challenges >\n")
    for i in range(1, 5):  # Column keys (1-4)
        first_col = f"{i}: {activities[i]}"
        second_col = f"{i + 4}: {activities[i + 4]}"
        third_col = f"{i + 8}: {activities[i + 8]}"
        fourth_col = f"{i + 12}: {activities[i + 12]}"

        print(f"{first_col}\t\t{second_col}\t\t{third_col}\t\t{fourth_col}")

#Query that opens activities done from August 5 to December 16 2024 first Semester in DLL of Domanico
from activities import act2, act3, act4, act5, act6, act7, act8, act9, act10, act11, act12, act13, act14, act15, act16, act17, act18, act19, act20, act21, act22, add as act23, act24, act25
def query_activities():
    while True:
        for i in range(1,120): print("-", end="")
        print(" ")
        dict_activities()
        to_open = input("\nSelect the activity to open (any key to 'exit') --> ")
        os.system('cls')
        
        if to_open == "1":print("The activity 1 is a typing test... ")
        if to_open == "2":act2(), ask_pass()
        elif to_open == "3":act3(), ask_pass()
        elif to_open == "4":act4(), ask_pass()
        elif to_open == "5":act5(), ask_pass()
        elif to_open == "6":act6(), ask_pass()
        elif to_open == "7":act7(), ask_pass()
        elif to_open == "8":act8(), ask_pass()
        elif to_open == "9":act9(), ask_pass()
        elif to_open == "10":act10(), ask_pass()
        elif to_open == "11":act11(), ask_pass()
        elif to_open == "12":act12(), ask_pass()
        elif to_open == "13":act13(), ask_pass()
        elif to_open == "14":act14(), ask_pass()
        elif to_open == "15":act15(), ask_pass()
        elif to_open == "16":act16(), ask_pass()
        elif to_open == "17":act17(), ask_pass()
        elif to_open == "18":act18(), ask_pass()
        elif to_open == "19":act19(), ask_pass()
        elif to_open == "20":act20(), ask_pass()
        elif to_open == "21":act21(), ask_pass()
        elif to_open == "22":act22(), ask_pass()
        elif to_open == "23":
            num1 = eval(input("Enter the first number ---> "))
            num2 = eval(input("Enter the second number ---> "))
            act23(num1, num2), ask_pass()
        elif to_open == "24":act24(), ask_pass()
        elif to_open == "25":act25(), ask_pass()
        else: return False
        os.system('cls')

#Query that opens code_challenges done from August 5 to December 16 2024 first Semester in DLL of Domanico
from code_challenges import code_C1,code_C2, code_C4, code_C5, code_C6, code_C7, code_C8, code_C9, code_C10, code_C11, code_C12, code_C13, code_C14, code_C15, code_C16
def query_code_challenges():
    for i in range(1,120): print("-", end="")
    print(" ")
    dict_code_challenges()
    to_open = input("\nSelect the code challenge to open (any key to 'exit') --> ")
    os.system('cls')
    
    if to_open == "1":code_C1(), ask_pass()
    if to_open == "2":code_C2(), ask_pass()
    elif to_open == "3":act3(), ask_pass()
    elif to_open == "4":code_C4(), ask_pass()
    elif to_open == "5":code_C5(), ask_pass()
    elif to_open == "6":code_C6(), ask_pass()
    elif to_open == "7":code_C7(), ask_pass()
    elif to_open == "8":code_C8(), ask_pass()
    elif to_open == "9":code_C9(), ask_pass()
    elif to_open == "10":code_C10(), ask_pass()
    elif to_open == "11":code_C11(), ask_pass()
    elif to_open == "12":code_C12(), ask_pass()
    elif to_open == "13":code_C13(), ask_pass()
    elif to_open == "14":code_C14(), ask_pass()
    elif to_open == "15":code_C15(), ask_pass()
    elif to_open == "16":code_C16(), ask_pass()
    os.system('cls')
