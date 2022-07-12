import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
amount_of_names = len(names)
payee = random.randint(0,amount_of_names -1)
person_paying = (names[payee])
print(person_paying + " is going to cover the bill today.")

