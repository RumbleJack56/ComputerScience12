#12-07-22
import sd, pickle
with open("p42a.txt" , "r+b") as f1:
    with open("p42b.txt" , 'r+b') as f2:
        output = ""
        for word in str(pickle.load(f1)).split() : output+= word+" "
        pickle.dump(output,f2)

with open("p42a.txt" , "r+b") as f1:
    with open("p42b.txt" , 'r+b') as f2:
        print(pickle.load(f1))
        print(pickle.load(f2))