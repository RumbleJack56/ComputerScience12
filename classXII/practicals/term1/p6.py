#8/4/22

import random
subj = ["Computer Science", "IP", "Physics", "Maths"]

#Method 1:
print(random.choice(subj))

#Method 2:
print(subj[random.randrange(3)])

#Method 3:
random.shuffle(subj)
print(subj[0])
