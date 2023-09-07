height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

square_height = float(height)**2
calc_weight = float(weight)
bmi = round((calc_weight / square_height),2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
        print (f"Your BMI is {bmi}, you are a normal weight")
elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese")
else:
    print (f"Your BMI is {bmi}, you are clinically obese")

#round(), floor division //, PEMDASLR
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

