# DNA Replication Game, Jermya Goodwine, v0.0
# Your code identifies a match correctly but does not save the score to a file. 
# Please see the screenshots to fix! 

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

def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time()
    rnaSequence = input("Please enter the matching RNA sequence. LEAVE NO SPACES! Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)

rna = genRNA(dna)
print(rna)

# time.time() returns the number of seconds since
# Tuples are ORDERED -- you can reference items with index.
# Tuples are UNCHANGABLE -- you can't add, modify, or delete after creating
# Tuples CAN have  duplicate values.



