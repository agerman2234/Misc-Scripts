
import random

def Shuffle():
    #maybe try doing this with OOP in the future?
    Suit=["C","S","H","D"]
    Rank= ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    Suit_len, Rank_len = 4, 13
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
        #need to put an iff statement in in case the x and why randomly pick the same
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
