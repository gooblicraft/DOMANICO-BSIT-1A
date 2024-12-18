#Fahrenheit
def act5():
    print("------------------- < Operators > -------------------\n")
    temp = int(input("Enter temperature in farenheit: "))
    cel = (temp - 32) * 5/9
    roundedCel = (round(cel, 2))
    print(f"The conversion of {temp} degrees farenheit is {roundedCel}")