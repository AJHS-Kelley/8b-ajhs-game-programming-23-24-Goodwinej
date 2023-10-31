#Hangman Game by Jermya Goodwine
import random
words ='big ink kid tin cat dog hot men ice red cactus judge smart larger marker equal pulp smoke easy magical conjunctively extemporizing dactylography electroencephalographically hyperimmunize physicalizing maximizations yellowjackets methylbenzene tranquillizer alphabetizing'.split()

# VARIABLE_NAMES IN ALL-CAPS ARE CONSTANTS THAT DON"T CHANGE
HANGMAN_BOARD = ['''
    +---+             
        |        
        |
        |         
   ==========''','''
    +---+             
    0   |        
        |
        |
   ==========''','''
    +---+             
    0   |        
    |   |
        |
   ==========''','''
    +---+             
    0   |        
   /|   |
        |
   ==========''','''
    +---+             
    0   |        
   /|\  |
        |
   ==========''','''
    +---+             
    0   |        
   /|\  |
   /    |
   ==========''','''
    +---+             
    0   |        
   /|\  |
   / \  |
   ==========''']

#PICK Word from the list
def getRandomWord(wordList): # return a radom word from the list.
   wordIndex = random.randint(0, len(wordList) - 1)
   # len(Listname) -1 is EXTREMLY COMMON FOR WORKING WITH LISTS.
   return wordList[wordIndex]

def displayBOard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')

# i = 0
# while i < 100:
#    word= getRandomWord(words)
#    print(word)
#    i += 1