import numpy as np
import random

def calculateDeckShuffle(maxNumber):
    test = False
    #start with deck1
    deck1 = list(range(1, (maxNumber//2) + 1))
    deck2 = list((range((maxNumber//2) + 1, maxNumber + 1)))

    deckMixTest = deck1 + deck2
    #print(deckMixTest)
    deckMix = []
    index = 1

    while not test:
        if(deckMix.__len__() > 0):
            deck1 = deckMix[:deckMix.__len__()//2]
            deck2 = deckMix[deckMix.__len__()//2:]

        deckMix = []

        for i in range(deck1.__len__()):
            deckMix.append(deck2[i])
            deckMix.append(deck1[i])
            #print(deckMix)

        if(deckMix == deckMixTest):
            test = True
            break

        index += 1

    #print("Number of iterations: ", index)
    #print("Final deck: ", deckMix)
    return (maxNumber, index)

print("Cards : 4 > ", "Repetitions : ", calculateDeckShuffle(4)[1])
print("Cards : 6 > ", "Repetitions : ", calculateDeckShuffle(6)[1])
print("Cards : 8 > ", "Repetitions : ", calculateDeckShuffle(8)[1])
print("Cards : 10 > ", "Repetitions : ", calculateDeckShuffle(10)[1])
print("Cards : 12 > ", "Repetitions : ", calculateDeckShuffle(12)[1])
print("Cards : 14 > ", "Repetitions : ", calculateDeckShuffle(14)[1])
print("Cards : 16 > ", "Repetitions : ", calculateDeckShuffle(16)[1])
print("Cards : 18 > ", "Repetitions : ", calculateDeckShuffle(18)[1])
print("Cards : 20 > ", "Repetitions : ", calculateDeckShuffle(20)[1])
print("Cards : 22 > ", "Repetitions : ", calculateDeckShuffle(22)[1])
print("Cards : 24 > ", "Repetitions : ", calculateDeckShuffle(24)[1])
print("Cards : 26 > ", "Repetitions : ", calculateDeckShuffle(26)[1])
print("Cards : 28 > ", "Repetitions : ", calculateDeckShuffle(28)[1])
print("Cards : 30 > ", "Repetitions : ", calculateDeckShuffle(30)[1])