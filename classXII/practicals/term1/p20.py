#4/6/22

import math, random
def dist():
    return str(random.randrange(1,15)*50)


print("Treasure map Hunting")
print("This generates a set of instructions for you to follow")

cardinalDirL = ["North" , "South"]
cardinalDirB = ["East", "West"]
localDirL = ["Forward" , "backward" ]
localDirB = ["Left", "Right"]
type = ["cardinal" , "local"]
#cardinal is north south east west
#local is left right forward backward


mapno = int(input("Enter Map Number: "))
random.seed(mapno)

steps = random.randrange(10)
path = ""
for k in range(steps):
    random.shuffle(type)
    if type[0]=="cardinal":
        mode = random.choice(["axis" , 'diagonal'])
        if mode == "axis":
            path+=str(k+1)+") Go " + dist() + "m " + random.choice( cardinalDirB + cardinalDirL )
        if mode == "diagonal":
            path+=str(k+1)+") Go " + dist() + "m " + random.choice( cardinalDirL) + "-" + random.choice( cardinalDirB)
    
    if type[0]=="local":
        mode = random.choice(["axis" , 'diagonal'])
        if mode == "axis":
            path+=str(k+1)+") Go " + dist() + "m " + random.choice( localDirB + localDirL )
        if mode == "diagonal":
            path+=str(k+1)+") Go " + dist() + "m " + random.choice( localDirL) + "-" + random.choice( localDirB)
    path+="\n"
print(path)      