import random as rd

cards = ["jack", "queen", "king", "ace"]
rd.shuffle(cards)
for card in cards:
    print(card)
