
import random

def Shuffle():

    Suit=["C","S","H","D"]
    Suit_len = len(Suit)
    Rank= ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    Rank_len = len(Rank)
    Deck= []

    i=0
    while i < (Rank_len):
        j=0
        while j < (Suit_len):
            Deck.append([Rank[i],Suit[j]])
            j += 1
        i += 1

    #print(Deck)
    #input("Press ENTER to shuffle")

    i=0
    while i < 500:

        x = random.randrange(0,52,1)
        y = random.randrange(0,52,1)
        #print(x)
        #print(y)
        z = Deck[x]
        Deck[x] = Deck[y]
        Deck[y] = z

        i += 1

    print(Deck)


def Card_Val():
    print("This is the card Value functon")

def Winning_Hand():

def Texas_Holdem_Deal():
    



Shuffle()

