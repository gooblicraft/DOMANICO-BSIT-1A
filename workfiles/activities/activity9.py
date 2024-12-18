
def act9():
    print("------------------- < Conditionals > -------------------\n")
    
    # Input name and age
    user = input("ENTER NAME : ")
    try:
        age = int(input("ENTER AGE : "))  # Use int() for safe type conversion
    except ValueError:
        print("Invalid age input. Please enter a valid number.")
        return

    # Check age conditions
    if 1 <= age <= 7:
        print(f"Hi {user}, you are a toddler.")
    elif 8 <= age <= 13:
        print(f"Hi {user}, you are a pre-teen.")
    elif 14 <= age <= 18:
        print(f"Hi {user}, you are a teenager.")
    elif 19 <= age <= 31:
        print(f"Hi {user}, you are in early adulthood.")
    elif 32 <= age <= 45:
        print(f"Hi {user}, you are in mid adulthood.")
    elif 46 <= age <= 59:
        print(f"Hi {user}, you are in late adulthood.")
    elif 60 <= age <= 100:
        print(f"Hi {user}, you are a senior.")
    else:
        print(f"Impossible! You're alive, {user}?!")

