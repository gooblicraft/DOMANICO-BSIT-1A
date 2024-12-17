
code1 = """
--------------------- < Creating a List > ---------------------
# An empty list
empty_list = []

# A list of integers
# numbers = [1, 2, 3, 4, 5]

# A list of strings
# fruits = ["apple", "banana", "cherry"]

# A list of mixed data types
mixed_list = [1, "hello", 3.14, True]

--------------------- < This is the Code > ---------------------
                            """

code2 = """
--------------------- < Accessing a List > ---------------------
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

--------------------- < This is the Code > ---------------------
"""
                        
code3 = """
--------------------- < Modifying a List > ---------------------
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  

# Output: ['apple', 'blueberry', 'cherry']

--------------------- < This is the Code > ---------------------
"""

code4 = """
--------------------- < Adding Elements > ---------------------
# Using append()
fruits.append("date")
print(fruits)  

# Output: ['apple', 'blueberry', 'cherry', 'date']

# Using insert()
fruits.insert(1, "blackberry")
print(fruits)  

# Output: ['apple', 'blackberry', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

--------------------- < This is the Code > ---------------------
                    """
                    
code5 = """
--------------------- < Removing Elements > ---------------------
# Using remove()
fruits.remove("cherry")
print(fruits)  

# Output: ['apple', 'blackberry', 'blueberry', 'date', 'elderberry', 'fig']

# Using pop()
fruits.pop(2)
print(fruits)  

# Output: ['apple', 'blackberry', 'date', 'elderberry', 'fig']

# Using del
del fruits[1]
print(fruits)  

# Output: ['apple', 'date', 'elderberry', 'fig']

--------------------- < This is the Code > ---------------------
                    """
                    
code_list = """
--------------------- < Example Code > ---------------------
Code: 

#Creating a list
courses = ["change", "BSIT", "BSSW", "BSA", "DHRS"]         
courses[0] = "BSAIS"                                        

#Adding an element inside a list
courses.append("BSIT_CLONE")                                 
courses.insert(5, "BSED")                                   
print(courses)

#Removing an element inside a list
courses.remove("BSIT_CLONE")                                
print(courses)

#Count the elements inside the list
print("There are : " + str(len(courses)))                   

"""

builtIn_functions = """
--------------------- < Accessing Built-in Functions > ---------------------
Code: 

#sample1
print("hello")          #the print() is a built-in function     

#sample2
num1 = 20
num2 = 10
print(sum(num1,num2))   #sum takes two parameters

#sample3
print(type(num1))       #print the variable type

--------------------------- <                  > ---------------------------             

"""

userDef_functions = """
--------------------- < Creating User Defined Functions > ---------------------
Code: 

#sample
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!


------------------------- <                       > ---------------------------             

"""

example_functions = """
--------------------- < Example Code > ---------------------
Code:

def get_person_info():
    name = "Alice"
    age = 30
    return name, age

person_name = get_person_info()
person_age = get_person_info()
print(person_name)  
print(person_age)   

"""