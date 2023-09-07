
print("Welcome to the tip calculator")
bill = float(input("Please enter your bill amount: £"))
tip = int(input("What percentage of tip would you like to give, 10, 12 or 15?"))
people_bill = int(input("How many people will split the bill?"))

tip_float = bill / 100 * tip

result = '{0:.2f}'.format((bill + tip_float) / people_bill)
print(f"You will each pay £ {result}")


