import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
#always one less as list value starts at zero

person_who_pays = names[random_choice]

print(f"The person who pays the bill is {person_who_pays}")

#another option is the choice tool
# person_who_pays = random.choice(names)