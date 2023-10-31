#Hangman Game by Jermya Goodwine

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

i = 0
while i< len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1
    