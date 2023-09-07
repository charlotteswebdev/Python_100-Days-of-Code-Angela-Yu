print("Welcome to the rollercoaster ride!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 18:
        bill = 6
        print("Child tickets are £6")
    elif age <=21:
        bill = 6.5
        print("Youth tickets are £6.5")
    elif age >=45 and age <=55:
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        bill = 8
        print("Adult tickets are £8")
    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        #bill = bill + 3
        bill += 3
    print(f"Your final bill is £{bill}")
else:
    print("Sorry! You need to be taller than 120cm to ride")