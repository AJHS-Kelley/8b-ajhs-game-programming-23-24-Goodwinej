#Hangman Game by Jermya Goodwine
import random
words ='big ink kid tin cat dog hot men ice red cactus judge smart larger marker equal pulp smoke easy magical conjunctively extemporizing dactylography electroencephalographically hyperimmunize physicalizing maximizations yellowjackets methylbenzene tranquillizer alphabetizing'.split()
#
#
#

word = {'Colors':'red orange yellow green blue indigovioklet fuschia teal garnet gold black whit esilver gold'.split(),
        'Animals': 'cat cow dog fish moose goose wombat wolverine giraffe hippopotamus lion alligatpr'.split(),
      'Shapes':'square triangle circle rhombus parallelogram trapezoid diamond dodecahedron'.split(),
      'Food': 'hamburger hotdog potato waffle pancake escargot oysters chips steak'.splt()}
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

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')    
    print()

    blanks = '_' * len(secretWord)

    # Replace Blanks with correct Letters.
    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks [:i] + secretWord[i] + blanks[i+1:]
            
    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
     while True:
          print('Please guess a letter and press enter')
          guess = input()


# i = 0
# while i < 100:
#    word= getRandomWord(words)
#    print(word)
#    i += 1