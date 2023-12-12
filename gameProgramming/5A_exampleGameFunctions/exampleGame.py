#Jermya goodwine, Tracksim, v0.0
import random

playerName= input("What should i call you?\n type your name and press enter.\n")
print(f"You want me to call you {playerName}?")
print(f"hi {playerName}")

speed = random.randint (0,21)
startquality = random.randint(0, 20)
indurance = random.randint(0, 10)
reactionTime = random.randint(0, 10)
jumpHeight = random.randint(0 , 20)
release = random.randint(0, 10)
ThrowQuality = random.randint(0, 20)


print ("your speed is")
print(speed)
print ("your start quality is")
print(startquality)
print ("your endurance is")
print(indurance)
print ("your reaction time is")
print(reactionTime)
print ("your jump height is")
print(jumpHeight)
print('your release quality')
print(release)



def run(speed, startquality, indurance):
    if startquality >= 6 and speed >= 14.5 and indurance >= 5:
        excellent = True
        print('You got an excellent start! Top runner!')
    elif startquality >= 5 and speed > 9 and indurance <5:
        good = True
        print('You got a good start; amazing run')
    else:
        print('Oh no terrible start, maybe next time you will get a better run.')
        excellent = False
        good = False

def hurdles(speed, reactionTime, jumpHeight):
    if jumpHeight >= 5 and reactionTime <= 2.5 and speed >= 14.5:
        excellent = True
        print('That was an amazing jump!')
    elif jumpHeight >= 3 and reactionTime <= 4.5 and speed >= 10.5:
        good = True
        print('pretty good starting jump')
    else:
        excellent = False
        good = False
        print('weak starting jump bud.. maybe next time.')
def javelion(throwQuality, reactionTime, release):
    if throwQuality >=  8 and reactionTime <= 5 and release >= 5:
        print ('amazing throw!')
    elif throwQuality <= 7 and reactionTime > 5 and release <= 4:
        print ('That was an okay throw')
    else: print ("BOOOOO! did you even try!?")

        



hurdles(speed, reactionTime, jumpHeight)

run(speed, startquality, indurance)

javelion(ThrowQuality, reactionTime, release)

        



