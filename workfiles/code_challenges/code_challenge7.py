def code_C7():
    isBuy = input("Did you buy a grocery (yes/no): ")
    
    if isBuy.lower() == "yes":        
        nameItem = input("NAME OF THE ITEM: ")
        priceItem = float(input("PRICE OF THE ITEM: "))
        age = int(input("AGE: "))
        amount = float(input("AMOUNT GIVEN: "))
            
        if age >= 60:
            discount = priceItem * 0.052
            total = priceItem - discount
            change = amount - total
            print(f"TOTAL AFTER DISCOUNT: {total:.2f}")
            print(f"CHANGE: {change:.2f}")
        else:
            pass	#need i fix
    else:
        print("Thank you for using the program.")
    print("Thank you for your purchase.")