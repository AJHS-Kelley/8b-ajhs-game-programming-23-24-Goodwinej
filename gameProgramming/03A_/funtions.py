import random
# # FUNCTION -- a named peice of code that can be reused easily.
# # FUNCTION SIGNATURE -- syntax for creating a new fumction.
# def exampleFunctionA(): # NO PARAMETERS
#   count = 0
#   num = int(input("How many times do you want to wish a happy birthday?\n"))
#   while count < num:
#     print("Happy birthday\n")
#     count += 1

# def exampleFunctionB(num, count):# PARAMETERS
#   while count < num:
#     print("Happy Birthday!!!\n")
    # count += 1
#     exampleFunctionA()
  
# IF YOU CODE REQIURES PARAMETERS IT WILL CRASH WITHOUT THEM

#
#
#
def rollDice(numDice, sizeDice):
    numRolled = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        print(f"Roll: {roll}\n")
        numRolled += 1

rollDice(1, 20)
rollDice(1, 25)        

