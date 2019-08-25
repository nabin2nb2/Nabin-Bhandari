#6.	At Jenny’s birthday party she orders a 32 piece pizza. -
# Have the user (probably Jenny) enter the number of people at the party that -
# will be eating pizza and output the number of slices each one gets.
# As you know the pizza might not divide evenly.  There are two ways to -
# handle this. The first is to ignore the extra pieces and give everyone the-
# same amount.  The second way is to cut up the extra pieces so that everyone -
# gets the same amount.  Your program must output both options. E.g.

# Number of guests: 10
# Option 1: 3 slices each, 2 left over
# Option 2: 3.2 slices each

Guest = input("Enter the number of Guest : ")
print("There are 32 pieces of Pizza Ordered\n")

OPT1 = 32//int(Guest)
AND = 32%int(Guest)

OPT2 = 32/int(Guest)

print("Each guest get " + str(OPT1) + " pieces and " + str(AND) + " Left over")
print("\t\tOR")
print("Each guest get " + str(OPT2.__round__(1)) + " slices each")

