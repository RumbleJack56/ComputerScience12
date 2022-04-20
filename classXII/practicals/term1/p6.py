import random
subj = ["Computer Science", "IP", "Physics", "Maths"]

#random method 1
print(random.choice(subj))

#random method 2
print(subj[random.randrange(3)])

#random method 3
random.shuffle(subj)
print(subj[0])
