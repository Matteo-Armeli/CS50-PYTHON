#import modules for coin toss
import random

coin = random.choice(["heads", "tails"])
print(coin)

#alternative import with from
from random import choice

coin = choice(["heads", "tails"])
print(coin)


#random.randint(a, b) dice roll
import random

number = random.randint(1,10)
print(number)

#random.shuffle(x) cards
import random

cards = ["jack", "queen", "king"] 
random.shuffle(cards)
for card in cards:
    print(card)