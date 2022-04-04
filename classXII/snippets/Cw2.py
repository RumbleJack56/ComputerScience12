import random

initial = round(100000 * random.random())
while True:
    print("number is: ",initial)
    
    print("Higher or lower\n")
    new = round(100000 * random.random())
    input()
    if new>initial:
        print('its higher')

    if new<initial:
        print('its lower')

    initial = new

