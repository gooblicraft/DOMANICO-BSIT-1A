#INTRODUCTION TO CONDITIONAL STATEMENTS

def act7():
    print("------------------- < Conditionals > -------------------\n")
    gold = 0
    miner = input("Hi, What is your name? ")
    isGold = input("Is the mineral gold? ")
    
    if isGold.lower() == "yes":
        gold = 1
        print(f"Hi {miner}, Your total number of gold is {gold}")
    else:
        print(f"Hi {miner}, Your total number of gold is {gold}")