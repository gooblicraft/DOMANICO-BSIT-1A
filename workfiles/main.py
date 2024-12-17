def access_workfiles():
    from .my_functions import query_activities, query_code_challenges
    import os
    import webbrowser as open_web

    #prompt for running the program
    isRun = True
    while isRun:
        print("--------------------- < MAIN MENU OF DOMANICO'S PROJECT > ---------------------\n")
        print("1.) Activities \n2.) Code Challenges \n3.) Github Contributions \n4.) Exit ")
                
        for x in range(1,80): print("-", end="")
        isAsk = input("\nSelect the number do you want to access: ")
        os.system('cls')
                
        if isAsk == "1":query_activities()
        elif isAsk == "2": query_code_challenges()
        elif isAsk == "3":open_web.open("https://github.com/gooblicraft")
        elif isAsk == "4": break
        else:
            continue
