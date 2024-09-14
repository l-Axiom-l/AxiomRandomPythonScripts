import numpy as np
import matplotlib.pyplot as plt
import sys

def calculateDeckShuffle(maxNumber):
    test = False
    #start with deck1
    deck1 = list(range(1, (maxNumber//2) + 1))
    deck2 = list((range((maxNumber//2) + 1, maxNumber + 1)))

    deckMixTest = deck1 + deck2
    deckhistory = []
    #print(deckMixTest)
    deckMix = []
    deckhistory.append(deckMixTest)
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

        deckhistory.append(deckMix)

        if(deckMix == deckMixTest):
            #deckhistory.append(deckMix)
            test = True
            break

        index += 1
    return (maxNumber, index, deckhistory)

def organizeHistory(deckHistory):

    organizedHistory = []

    for i in range(deckHistory.__len__()):

        history = deckHistory[i]
        tempHistory = []

        for j in range(history.__len__()):
            test = (history[j], j)
            tempHistory.append(test)

        organizedHistory.append(tempHistory)

    return organizedHistory

def createCardHistory(deckHistory):
    cards = {}

    for i in range(deckHistory.__len__()): #i is a repetition
        deck = deckHistory[i]

        for j in range(deck.__len__()): #j is a card

            if not (deck[j] in cards.keys()):
                cards.update({deck[j]:[]})

            cards[deck[j]].append(j)

    return cards

def visualizeDeckShuffle(deckHistory, repetitions):
    cards = createCardHistory(deckHistory)
    #plt.xlim(0, repetitions)
    for key in cards.keys():
        plt.plot(cards[key], label=key)

    plt.show()


def main():
    if(len(sys.argv) < 2):
        print("Please provide the number of cards")
        sys.exit(0)

    cardCount = int(sys.argv[1])

    returnValue = calculateDeckShuffle(cardCount)
    print("Cards : ",cardCount, "> Repetitions : ", returnValue[1])
    visualizeDeckShuffle(returnValue[2], returnValue[1])


if __name__ == '__main__':
    main()