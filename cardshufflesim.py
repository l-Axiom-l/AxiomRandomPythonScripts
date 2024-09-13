import numpy as np
import sys

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

if(len(sys.argv) < 2):
    print("Please provide the number of cards")
    sys.exit(0)

cardCount = int(sys.argv[1])
print("Cards : ",cardCount, "> Repetitions : ", calculateDeckShuffle(cardCount)[1])