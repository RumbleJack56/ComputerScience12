# import random

# initial = round(100000 * random.random())
# while True:
#     print("number is: ",initial)
    
#     print("Higher or lower\n")
#     new = round(100000 * random.random())
#     input()
#     if new>initial:
#         print('its higher')

#     if new<initial:
#         print('its lower')

#     initial = new



import random

initial = round(100000 * random.random())
while True:
    print("number is: ",initial)
    
    print("Higher or lower\n")
    c = 1
    while True:
        factorx = random.randint(10000,60000) 
        new = initial + round(factorx * random.random()) - factorx/2
        if new>0 and new<100000: c = 1
        else: c=0

        if c == 1: break
    input()
    if new>initial:
        print('its higher')

    if new<initial:
        print('its lower')

    initial = new


