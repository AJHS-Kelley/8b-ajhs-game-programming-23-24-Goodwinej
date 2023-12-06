#Jermya goodwine, Tracksim, v0.0
import random

playerName= input("What should i call you/\n type your name and press enter.\n")
print(f"You want me to call you {playerName}?")

speed = random.randint (0,21)
startquality = random.randint(0, 11)
indurance = random.randint(0, 11)
reactionTime = random.randint(0, 6)
jumpHeight = random.randint(0 , 11)

print ("your speed is")
print(speed)
print ("your start quality is")
print(startquality)
print ("your indurance is")
print(indurance)
print ("your reaction time is")
print(reactionTime)
print ("you jump height is")
print(jumpHeight)



def run(speed, startquality, indurance):
    if startquality >= 6 and speed >= 14.5 and indurance >= 5:
        excellent = True
        print('You got an excellent start!')
    elif startquality >= 5 and speed >= 12 and indurance >= 3:
        good = True
        print('You got a good start')
    else:
        print('Oh no terrible start.')
        excellent = False
        good = False

def hurdles(speed, reactionTime, jumpHeight):
    if jumpHeight >= 5 and reactionTime <= 2.5 and speed >= 14.5:
        excellent = True
        print('That was an amazing jump!')
    elif jumpHeight >= 3 and reactionTime <= 4.5 and speed >= 10.5:
        good = True
        print('pretty good start')
    else:
        excellent = False
        good = False
        print('weak start.. maybe next time.')



hurdles(speed, reactionTime, jumpHeight)

run(speed, startquality, indurance)

        



