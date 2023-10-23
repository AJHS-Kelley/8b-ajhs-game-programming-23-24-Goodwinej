# Data types and Operators, Goodwine jermya, v0.3 

# Variable Ruiles
# Cannot start with a NUMBER!!!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use _ to seperate words, all lower case.
# camelCase variables do not use spacaes, 1st word lower, rest uppercase.

# String Literal Examples
playerName = "mangoseed"
emptyString = ""
spaceString = " "
petName = "kiwii"

# integer Data Types
health = 100
extraLives=5
temperature= -17
pethealth = 75

# Floating Point Data Types
pi=3.1245
lapTime = 3.5
velocity = -2.0
speed = .78

# Boolean Data Types
isFIreType= False
weaponEquipped= True
pvpEnabled= False
hungerActivated= True

# Arithmetic Operators
#Pemdas THE SAME AS IN MATH CLASS!
print(319+1) # Addition
print(6-4) # subtraction
print(12*7) # Multiplication 
print(9/3) # Division
print(2**5) # Exponents
print(20%34) # Modulus -- Divides, the returns remainder, most commonly used to determine even/odd
 
 # Comparison Operators
 #Evaluate the expression, then return True or False
print(5>3) #Greater than
print(10>=5) #Greater than or equal to
print(-2<19) #less than
print(0<=7) #Less than or equal to
print(250==250) #Equal to
print(200!=323) #Not equal to

myVariable = "myValue" # Assign variable on the left to the value on the right hand side.
myOtherVariable = (10 + 5)

# Addition Assignment
myWallet = 0
myWallet += 12
myWallet += 12349
print(myWallet)

# Same Effect 
x = 0
x += 1
x += 345638
print(x)

# Logical OPerators
print(3 > 5 and 4 < 3) #AND requires ALL expressions to be true
print(3 > 2 and 4 < 3)
print(3 > 5 and 4 < 3)
print(3 > 5 and 4 < 3 and favColor == "pink" and temp == -5)
# When writing and expressions, put the value most likely to be false first

# Logical OR -- Requires ONE expression to be TRUE.
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combined
print("line 81")
print(3 > 2 and 4 < 3 or 5!= 7)
print(True and False or True)

#while Loop-- Think "MUSICAL CHAIRS" -- Used when you do NOT know how many items are in a loop 
# iteration = one complete trip through a loop
 x = 0
while x < 100:
     print(f"x is currently equal to {x}")
     x += 1
     # () Parentheses
     # [] Square Brackets
     # <> Angle Brackets
     # {} Braces
 # Control c kills a loop

 x is currently equal to 0
x is currently equal to 5
x is currently equal to 10
x is currently equal to 15
x is currently equal to 20
x is currently equal to 25
x is currently equal to 30
x is currently equal to 35
x is currently equal to 40
x is currently equal to 45
x is currently equal to 50
x is currently equal to 55
x is currently equal to 60
x is currently equal to 65
x is currently equal to 70
x is currently equal to 75
x is currently equal to 80
x is currently equal to 85
x is currently equal to 90
x is currently equal to 95

# for Loop -- Thoing 'Go Fish', used when you know number of iterations needed.
for i in range(10): # i = iterable variables
   print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
   print(i)
   if i % 2 == 0:
      print("that number is even dude")
else:
   print("That number is odd!")