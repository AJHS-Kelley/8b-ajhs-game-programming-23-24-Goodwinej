#Jermya goodwine, Tracksim, v0.0
import random

def starterPistol():
    input("are you ready?\n press enter")
    print("1..")
    print("2..")
    print("3!!!")
    print("**WHistle sound**")
    return

def run(speed, startquality, indurance):
    if startquality >= 6 and speed >= 14.5 and indurance >= 5:
        firstPlace = True
        print('You got first place, what an amazing runner!')
    elif startquality >= 5 and speed >= 12 and indurance >= 3:
        secondPlace = True
        print('You got second place, congrats on coming second!')
    else:
        print('Oh no last place ig.')
        firstPlace = False
        secondPlace = False

def hurdles(speed, reactionTime, jumpHeight):
    if jumpHeight >= 10 and reactionTime <= 2.5 and speed >= 14.5:
        firstPLace= True
        



