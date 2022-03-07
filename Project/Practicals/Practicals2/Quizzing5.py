from random import shuffle
QA = {"What is 2+2?   ":'4',
"What is binary value of True?   " : '1',
"Can you put a list in a list (Y/N)?   " : 'Y',
"randon is fuction while randint is module (Y/N)?   ": "N",
"Python is a compiled language (Y/N)?   ": "N"}
Q = list(QA.keys())
shuffle(Q)

correct = 0
for x in range(len(Q)):
    ans = input("Q"+str(x+1)+") "+Q[x])
    if ans.upper() == QA[Q[x]]:
        print("Correct , Now next Question")
        correct+=1
    else:
        print("Oh, Wrong, Lets Try Again")
print("Oh oh, we have run out of questions")
print("Final Remarks: ",end="")
if correct==0: print("general knowledge helps")
elif correct==1: print("Need to take Interest")
elif correct==2: print("Needs work, can do better")
elif correct==3: print("Good, but try harder next time")
elif correct==4: print("Well Done")
elif correct==5: print("Perfect")
