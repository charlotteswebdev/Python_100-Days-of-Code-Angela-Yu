print("Is it a leap year?")

#on every year that is evenly divisible by 4
#**except** every year that is evenly divisible by 100
#**unless** the year is also evenly divisible by 400

year = int(input("Type in a year: "))
#modular
if year % 400 == 0:
    print("This is a leap year")
elif year % 100 == 0:
    print("This is not a leap year")
elif year % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year\n")
