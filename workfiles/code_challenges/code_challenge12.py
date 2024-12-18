def code_C12():
    print("------------------- < Loops > -------------------\n")
    #for loop complete range
    for x in range(1 , 6): 
        for a in range (6, x , -1):
            print(" ",end = " ")
        for b in range (0, x):
            print("*", end = " ")
        for c in range (0, x ):
            print("*", end = " ")
        
        print()
        # dapat bukod na for loop as individual

    for y in range(1, 6):
        for d in range(0, y):
            print(" ", end = " ")
        for e in range (5, y , -1):
            print(" ",end = " ")
        for f in range (0, 2):
            print("*",end = " ")
        print()
