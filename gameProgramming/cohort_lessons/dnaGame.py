# DNA Replication Game, Jermya Goodwine, v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime

#Import Specific Methods -- Get the specific tool.
from random import choice

# store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("please enter a positive interger number of bases to create.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1        
    return dnaSequence

dna = genDNA()
print(dna)
