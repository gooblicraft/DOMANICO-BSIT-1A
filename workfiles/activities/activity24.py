#This will only run on main.py since the activity23 and activity 24 is relative from the activities folder, the import method use '.' representing as relative import

from .activity23 import add

def act24():
    print("(Activity 24 is all about understanding the import and Doc String)\n")
    add(21,21)
    help(add) # the docstring
