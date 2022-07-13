#12/7/22
#to and the counter
import sd 
with open("p44a.txt", 'r+') as f1:
    data = [k.rstrip("\n") for k in f1.readlines()]
    ans = len(["" for k in data for word in k.split() if word.lower() in ("the","to")])
    print(ans)

