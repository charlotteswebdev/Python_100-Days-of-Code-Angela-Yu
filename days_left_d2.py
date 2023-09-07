#Program that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")

age_as_int = int(age)
years_left = 90 - age_as_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

#fstring
message = f"You have {days_left} days, {weeks_left} weeks, {months_left} months left"
print(message)