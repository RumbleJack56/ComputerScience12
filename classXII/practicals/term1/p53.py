#Stacks peeking through a deck of cards

import random as r

stack = []
L = 0
top=None
types  = ["Spades","Clubs","Hearts","Diamonds"]
numbers = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
deck = [a+" of "+b for a in numbers for b in types]

#adding
for card in deck:
    stack.append(card)
    L+=1
    top = L-1

r.shuffle(stack)

#peeking
print("The current card is \"%-12s\""%stack[top])
while True:
    if input("Do you want to see next card? (Y/N)").lower() == "n":
        break
    #removal
    stack.pop(top)
    L-=1
    top = L-1
    print("The new card is \"%-12s\""%stack[top])



