def code_C11():
    print("------------------- < Loops > -------------------\n")
    #for loop complete range
    for x in range(1 , 4): 
        for a in range (4, x , -1):
            print(" ",end = " ")
        for b in range (0, x):
            print("*", end = " ")
        for c in range (0, x - 1):
            print("*", end = " ")
        print()
    for z in range(0,7):
        print("*", end = " ")
        # dapat bukod na for loop as individual
    print()
    for y in range(1, 4):
        for d in range(0, y):
            print(" ", end = " ")
        for e in range (4, y , -1):
            print("*",end = " ")
        for f in range (4, y +1, -1):
            print("*",end = " ")
        
        print()